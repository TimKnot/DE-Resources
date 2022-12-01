import pandas as pd
from sql_utils import setup_db_connection, create_db_tables, create_engine_for_load_step


### EXTRACT

# 1. Read the sales_data.csv
df = pd.read_csv('sales_data.csv')


### TRANSFORM

# 2. Clean that data (minimum requirement is to remove any rows that contain null cells).
df = df.dropna()

# 3. Filter data for the period 1 December 2020 - 5 December 2020 (generally good to apply date filter early so we don't waste compute)
start_date = '2020-12-01'
end_date = '2020-12-05'
df = df.loc[(df['purchase_date'] > start_date) & (df['purchase_date'] <= end_date)]

# 4. Calculate each customer's total spend
total_spend = df.groupby(['customer_id']).sum().rename(columns={"purchase_amount": "total_spend"})

# 5. Calculate each customer's average spend
avg_spend = df.groupby(['customer_id']).mean().rename(columns={"purchase_amount": "average_spend"})

customer_spend = avg_spend.merge(total_spend, on='customer_id')

# 6. Calculate how many times each customer has purchased a specific item
customer_products = df.groupby(by=["customer_id","product_id"], as_index=False, dropna=False).count()\
    .rename(columns={"purchase_date": "quantity"})\
    .drop(columns=['purchase_amount'])

## LOAD

engine = create_engine_for_load_step()
connection, cursor = setup_db_connection()
create_db_tables(connection, cursor)

# 7. Load the transformed data to the created tables
df.to_sql('sales_data', engine, index=False, if_exists='replace')
customer_spend.to_sql('customer_spend', engine, index=False, if_exists='replace')
customer_products.to_sql('customer_products', engine, index=False, if_exists='replace')
