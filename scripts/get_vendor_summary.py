import sqlite3
import pandas as pd
import logging
from sqlalchemy import create_engine
import time

logging.basicConfig(
    filename='logs/get_vendor_summary.log',
    level=logging.DEBUG,
    format='%(asctime)s-%(levelname)s-%(message)s',
    filemode='a'
)

# create database engine
engine = create_engine('sqlite:///inventory.db')


def ingest_db(df, table_name):
    '''ingest dataframe into database (replace old table to avoid duplicates)'''
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)


def create_vendor_summary(conn):
    '''merge tables to create vendor summary'''

    vendor_sales_summary = pd.read_sql_query("""
    WITH FreightSummary AS (
        SELECT
            VENDORNUMBER,
            SUM(Freight) AS FreightCost
        FROM vendor_invoice
        GROUP BY VENDORNUMBER
    ),

    PurchaseSummary AS (
        SELECT 
            p.VENDORNUMBER,
            p.VENDORNAME,
            p.BRAND,
            p.DESCRIPTION,
            p.PURCHASEPRICE,
            pp.PRICE AS ActualPrice,
            pp.VOLUME,
            SUM(p.QUANTITY) AS TotalPurchaseQuantity,
            SUM(p.DOLLARS) AS TotalPurchaseDollars
        FROM purchases p
        JOIN purchase_prices pp
            ON p.BRAND = pp.BRAND
        WHERE p.PURCHASEPRICE > 0
        GROUP BY 
            p.VENDORNUMBER,
            p.VENDORNAME,
            p.BRAND,
            p.DESCRIPTION,
            p.PURCHASEPRICE,
            pp.PRICE,
            pp.VOLUME
    ),

    SalesSummary AS (
        SELECT 
            VENDORNO,
            BRAND,
            SUM(SalesQuantity) AS TotalSalesQuantity,
            SUM(SalesDollars) AS TotalSalesDollars,
            SUM(SalesPrice) AS TotalSalesPrice,
            SUM(ExciseTax) AS TotalExciseTax
        FROM sales
        GROUP BY VENDORNO, BRAND
    )

    SELECT 
        ps.VENDORNUMBER,
        ps.VENDORNAME,
        ps.BRAND,
        ps.DESCRIPTION,
        ps.PURCHASEPRICE,
        ps.ActualPrice,
        ps.VOLUME,
        ps.TotalPurchaseQuantity,
        ps.TotalPurchaseDollars,
        ss.TotalSalesQuantity,
        ss.TotalSalesDollars,
        ss.TotalSalesPrice,
        ss.TotalExciseTax,
        fs.FreightCost
    FROM PurchaseSummary ps
    LEFT JOIN SalesSummary ss
        ON ps.VENDORNUMBER = ss.VENDORNO
        AND ps.BRAND = ss.BRAND
    LEFT JOIN FreightSummary fs
        ON ps.VENDORNUMBER = fs.VENDORNUMBER
    ORDER BY ps.TotalPurchaseDollars DESC
    """, conn)

    return vendor_sales_summary


def clean_data(df):
    '''clean dataframe and create analysis metrics'''

    df['VOLUME'] = df['VOLUME'].astype(float)

    df.fillna(0, inplace=True)

    df['VENDORNAME'] = df['VENDORNAME'].str.strip()
    df['DESCRIPTION'] = df['DESCRIPTION'].str.strip()

    # new analysis columns
    df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']

    df['ProfitMargin'] = (df['GrossProfit'] / df['TotalSalesDollars']) * 100

    df['StockTurnover'] = df['TotalSalesQuantity'] / df['TotalPurchaseQuantity']

    df['SalesToPurchaseRatio'] = df['TotalSalesDollars'] / df['TotalPurchaseDollars']

    return df


if __name__ == '__main__':

    start = time.time()

    conn = sqlite3.connect('inventory.db')

    logging.info("Starting Vendor Summary Creation")

    summary_df = create_vendor_summary(conn)
    logging.info("Vendor summary created")

    clean_df = clean_data(summary_df)
    logging.info("Data cleaned")

    ingest_db(clean_df, 'vendor_sales_summary')
    logging.info("Table stored in database")

    end = time.time()
    total_time = (end - start) / 60

    logging.info(f"Total Time Taken: {total_time:.2f} minutes")
    logging.info("Process Completed")