# gcp-datalake

## Summary
1. [About](#about)
2. [Tools](#tools)

## About
The main idea of this project is the creation of a Datalake using public data.

All the content, tasks and tools used were inspired by the livestream series from [Téo Calvo channel](twitch.tv/teomewhy) and [GCP BigLake introduction](https://medium.com/google-cloud/gcp-biglake-introduction-570fb88be132).

You can check the progress of the project through the issues.

## Tools
The main tools that I used to make this project is provided by Google.

It is intended to use the free tier quota of each tool.

1. Google Cloud Storage (GCS) - Where all our data will be stored, either .csv, .parquet or .json files.
2. Big Query - This engine will help us to have a data warehouse nested to our datalake.
3. Apache Spark - Processing engine of data. This tool will be responsible for processing our data and leading them to more refined layers.
4. Looker - Data Visualization tool - It is important to provide the results and have the possibility of generate dashboards and support decision making.
