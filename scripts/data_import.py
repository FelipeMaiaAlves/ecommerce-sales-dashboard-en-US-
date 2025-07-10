import pandas as pd
from sqlalchemy import create_engine

# 1. Read the CSV file
df = pd.read_csv("sales.csv")

# 2. Cleaning
df.dropna(inplace=True)
df['data'] = pd.to_datetime(df['data'])

# 3. MySQL Connection
user = "root"  # your MySQL username
password = "password"  # change this to your MySQL password
host = "localhost:3306"
database = "sales"

# Connection String
engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306/sales")
conn = engine.connect()

# 4. Send data to SQL table
df.to_sql("sales_ecommerce", con=engine, if_exists="replace", index=False)

print("Data import successful.")
