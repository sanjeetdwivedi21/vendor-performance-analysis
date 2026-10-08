import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

#logging.basicConfig(
  #  filename="logs/ingestion_db.log",
#    level=logging.DEBUG,
#    format="%(asctime)s - %(levelname)s - %(message)s",
 #   filemode="a"
#)

engine = create_engine('sqlite:///inventory.db')
def ingest_db(df, table_name, engine):
    df.to_sql(
        table_name,
        con=engine,
        if_exists='replace',
        index=False,
        chunksize=10000
    )
def load_raw_data():
    "this function will load the CSVs as dataframe and ingest into db"
    start = time.time()
    for file in os.listdir("data"):
        if file.endswith(".csv"):
         first = True
        for chunk in pd.read_csv(f"data/{file}", chunksize=50000):
            chunk.to_sql(
                file[:-4],
                con=engine,
                if_exists="replace" if first else "append",
                index=False
            )
            first = False
            logging.info(f'Ingesting {file} in db')
    end = time.time()
    total_time = (end - start)/60
    logging.info('------------Ingestion Complete------------')
    logging.info(f'Total Time Taken: {total_time} minutes')
if __name__ == '__main__':
    load_raw_data()