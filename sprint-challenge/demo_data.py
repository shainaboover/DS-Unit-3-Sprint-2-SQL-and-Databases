
import sqlite3


# open connection and cursor
connection = sqlite3.connect('demo_data.sqlite3')
cursor = connection.cursor()


# create a table and execute
create_table = """CREATE TABLE demo (s TEXT, x NUMERIC, y NUMERIC);"""
cursor.execute(create_table)


# insert rows into table
cursor.execute("""INSERT INTO demo VALUES ('g', 3, 9);""")
cursor.execute("""INSERT INTO demo VALUES ('v', 5, 7);""")
cursor.execute("""INSERT INTO demo VALUES ('f', 8, 7);""")


#check work
cursor.execute("""SELECT * FROM demo;""")

print(
  'Data check:', 
  cursor.fetchall()
)


# save connection
connection.commit()


# How many rows?
cursor.execute(
  """SELECT COUNT(*) FROM demo;"""
)

print(
  'There are', 
  cursor.fetchone() [0], 
  'rows.'
)


# How many rows where `x` and `y` are at least 5?
cursor.execute(
  """SELECT COUNT(*) FROM demo
    WHERE x >= 5
    AND y >= 5;"""
)

print(
  'There are', 
  cursor.fetchone() [0], 
  'rows where x and y are at least 5.'
)


# How many unique values of `y` are there?
cursor.execute(
  """SELECT COUNT(DISTINCT y) FROM demo;"""
)

print(
  'There are', 
  cursor.fetchone() [0], 
  'unique values of y.'
)
