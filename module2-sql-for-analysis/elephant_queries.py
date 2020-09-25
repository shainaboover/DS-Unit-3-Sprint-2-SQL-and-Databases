import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import json

load_dotenv() #> loads contents of the .env file into the script's environment

# save credentials to environment variables for security and shareability
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

print(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST)

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

cursor.execute('SELECT * from test_table;')

result = cursor.fetchall()
print(result)


# use execute_values statement to add to database
# data must be in a list of tuples
my_dict = { "A": '1', "B": ["dog", "cat", '42'], "c": 'true' }

table_name = 'test_table'

insertion_query = "INSERT INTO test_table (name, data) VALUES %s"

execute_values(cursor, insertion_query, [
  ('A rowww','null'),
  ("another row with json", json.dumps(my_dict)),
  ('third row', '3')
])

# commit the query 
connection.commit()

# close the cursor
cursor.close()

# close the connection
connection.close()



