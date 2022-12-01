import csv
from sql_utils import setup_db_connection, create_db_tables


# Notes on the information/insights they should see from the data transformations:
# 2194 - low frequency spends, large amounts, buys the same product each time
# 5632 - medium frequency spends, medium amounts, buys three products
# 7365 - high frequency spends, small amounts, buys a different product each time

def extract_and_clean_sales_data():
    sales_data = []

    try:
        with open('sales_data.csv', 'r') as file:
            source_file = csv.DictReader(file, fieldnames=['customer_id', 'purchase_date', 'purchase_amount', 'product_id'], delimiter=',')
            next(source_file) #ignore the header row
            for row in source_file:
                if '' not in row.values():
                    sales_data.append(row)
    except Exception as error:
        print("An error occurred: " + str(error))

    return sales_data

connection, cursor = setup_db_connection()

#create the tables for the data
create_db_tables(connection, cursor) # set up the sql tables that we will be loading to

# extract and clean the data
cleaned_sales_data = extract_and_clean_sales_data()


# Load the cleaned raw data
connection, cursor = setup_db_connection()
for data_row in cleaned_sales_data:
    data_row_insert_sql = f"""INSERT INTO sales_data(customer_id,purchase_date,purchase_amount,product_id)
            VALUES('{data_row['customer_id']}', '{data_row['purchase_date']}', 
            {data_row['purchase_amount']}, '{data_row['product_id']}')"""    
    cursor.execute(data_row_insert_sql)



# Get the spend values
customer_spend_sql = """INSERT INTO customer_spend 
          SELECT customer_id, AVG(purchase_amount), SUM(purchase_amount) 
          FROM sales_data 
          WHERE purchase_date between '2020-12-01' and '2020-12-05'
          GROUP BY customer_id"""
cursor.execute(customer_spend_sql)

# get the product quantity values
customer_product_sql = """INSERT INTO customer_products 
          SELECT customer_id, product_id, count(*) 
          FROM sales_data 
          WHERE purchase_date between '2020-12-01' and '2020-12-05'
          GROUP BY customer_id, product_id 
          ORDER BY customer_id"""
cursor.execute(customer_product_sql)
connection.commit()

cursor.close()
connection.close()
