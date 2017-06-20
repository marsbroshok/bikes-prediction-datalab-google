from google.cloud import bigquery
import json
import urllib2

# Bikes data
strJSON = urllib2.urlopen("https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&rows=202&start=0" + "&facet=nom&facet=commune").read()
data = json.loads(strJSON)

# Weather data
strJSON = urllib2.urlopen("https://api.apixu.com/v1/current.json?key=0b3e3daaeaf6432f858101713170806&q=Lille").read()
weather = json.loads(strJSON)
temperature = weather.get("current", {}).get("temp_c", -99)

# Connect to BQ
bigquery_client = bigquery.Client(project="gcp-data-cirruseo")
dataset = bigquery_client.dataset("aus_velill_demo")
table = dataset.table("vlilleRealtime")
table.reload()

# Prepare data to insert
rows = [
    [k["recordid"], k["record_timestamp"], k["fields"]["libelle"], k["fields"]["etatConnexion"], k["fields"]["etat"],
     k["fields"]["adresse"], k["fields"]["commune"], k["fields"]["geo"][0], k["fields"]["geo"][1], k["fields"]["type"],
     k["fields"]["nbPlacesDispo"], k["fields"]["nbVelosDispo"], temperature] for k in data["records"]]
# print rows

# Insert to BQ table and report results
errors = table.insert_data(rows)
if not errors:
    print('Loaded {} row'.format(len(rows)))
else:
    print('Errors:')
    pprint(errors)
