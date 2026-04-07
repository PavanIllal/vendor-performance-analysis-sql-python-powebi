import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

# create logs folder if not exists
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename='logs/ingestion_db.log',
    level=logging.INFO,
    format='%(asctime)s-%(levelname)s-%(message)s',
    filemode='w'
)

# remove old database to avoid duplicates
if os.path.exists("inventory.db"):
    os.remove("inventory.db")

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine):
    '''this function will ingest the dataframe into database table'''
    df.to_sql(table_name, con=engine, if_exists='append', index=False)


'''this function will load the CSVs as dataframe and ingest into db'''

def load_raw_data():

    path = r'C:\Users\Pavan\data'
    start = time.time()

    for file in os.listdir(path):

        if file.endswith('.csv'):

            rows = 0
            cols = None

            filepath = os.path.join(path, file)

            for chunk in pd.read_csv(filepath, chunksize=50000):

                rows += len(chunk)
                cols = chunk.shape[1]

                ingest_db(chunk, file[:-4], engine)

            logging.info((rows, cols))
            logging.info(f'Ingesting {file} in db')
            logging.info('------------Ingestion Complete-------------')

    end = time.time()
    total_time = (end - start) / 60

    logging.info(f'Total Time Taken: {total_time:.2f} minutes')


if __name__ == '__main__':
    load_raw_data()