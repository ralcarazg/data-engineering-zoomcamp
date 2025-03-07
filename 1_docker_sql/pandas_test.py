import pandas as pd

import sqlalchemy

from sqlalchemy import create_engine

engine = create_engine('postgresql://root:password@localhost:5432/ny_taxi')

engine.connect()


df_iter = pd.read_csv('1_docker_sql/yellow_tripdata_2021-01.csv', iterator=True, chunksize=10000)


while True:
    df = next(df_iter)
    df.tpep_pickup_datetime = pd.to_datetime(df['tpep_pickup_datetime'])
    df.tpep_dropoff_datetime = pd.to_datetime(df['tpep_dropoff_datetime'])
    df.to_sql('yellow_taxi_data', engine, if_exists='append')
    print('writing to database')







