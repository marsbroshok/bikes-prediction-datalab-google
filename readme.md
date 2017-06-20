
# Data Analysis with Google Cloud Platform
## [V'Lille Data exploration with Google Datalab](https://github.com/marsbroshok/bikes-prediction-datalab-google/blob/master/VLille%20Datalab%20Example.ipynb)

In this repository you could find python script, Datalab Notebook and supporting files to explore V'Lille bicycles usage statistics.

Data about usage statistics of Lille's public bicycles are available on [data.gouv.fr](https://www.data.gouv.fr/en/datasets/vlille-disponibilite-en-temps-reel/)

We will use that data and information about weather to show how to perform data analysis in Google Datalab environment.

### Data Extraction Setup
To run the code in this repository you need to:

1) Activate your [Google Platform Free Trial](https://cloud.google.com/free/).

2) Create BigQuery table to store historical data of VLille bikes availability ([Create BigQuery Dataset](https://cloud.google.com/bigquery/quickstart-web-ui#create_a_dataset))

3) Create small Compute Engine VM instance  ([Create GCE Instance](https://cloud.google.com/compute/docs/instances/create-start-instance))

4) Add `velillBQ.py`python script to that machine (you can copy it in SSH Web UI) and change permitions to 'execute' (like `chmod 755 velillBQ.py`)

5) Update `velillBQ.py` script with your BigQuery dataset parameters

6) Add cron task to run python script every minute. In VM ssh terminal run `crontab -e`and add the line `* * * * * python $YOUR_PATH_HERE/velillBQ.py`

Congrats! You are done with synchronizing VLille data with your historical storage in BigQuery dataset.

### Data Exploration
Follow descriptions in Google Datalab Notebook [VLille Datalab Example](https://github.com/marsbroshok/bikes-prediction-datalab-google/blob/master/VLille%20Datalab%20Example.ipynb) to perform of verifiy how to:

* Query data from Google BigQuery table
* Visualize data using Google Charts in Datalab
* Build Machine Learning model to perform prediction for bicycle's availablity
* Publish trained ML model to Google ML Engine as API

------
Alexander.Usoltsev(at)cirruseo.com, 2017
