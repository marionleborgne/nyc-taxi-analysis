# NYC taxis analysis

A quick look into the impact of data aggregation on anomaly detection results.

### Problem statement
When using slightly re-sampled data, the HTM seems to be missing some anomalies.
![nyc taxi data aggregations](https://raw.githubusercontent.com/marionleborgne/nyc-taxi-analysis/master/assets/problem.png)


### Usage
The script `run.py` will generate re-sampled CSVs based on the original data 
`original_data/nyc_taxi_30m.csv`. This data comes from [NAB](https://github.com/numenta/NAB/blob/master/data/realKnownCause/nyc_taxi.csv) and is sampled every 30m.
![nyc taxi data aggregations](https://raw.githubusercontent.com/marionleborgne/nyc-taxi-analysis/master/assets/nyc-aggregations.png)


