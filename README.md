# Enterprise AI Pipeline — Real-Time NYC Taxi Demand Forecasting


This repo contains an end-to-end pipeline scaffold for large-scale taxi demand forecasting.


## Quickstart (local)
1. Install python deps: `pip install -r requirements.txt`
2. Prepare data: `python etl/data_prep.py --input_csv <path-to-csv> --out_dir ./data` (use --nrows for testing)
3. Train: `python train/train.py --input_parquet ./data/hourly_aggregated.parquet --out_dir ./train_out`
4. Run: `docker build -t taxi-pipeline . && docker run -p 8000:8000 taxi-pipeline`
5. Test: `curl -X POST http://localhost:8000/predict -H 'Content-Type: application/json' -d '{"pickup_zone":"1","date":"2023-01-01","hour":8,"passengers":1,"avg_passengers":1.0}'`


## CI/CD
Configured GitHub Actions to run tests and build Docker image on push.


## Monitoring
Expose