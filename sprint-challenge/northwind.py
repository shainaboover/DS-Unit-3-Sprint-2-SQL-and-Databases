
import os
import sqlite3

# construct path to database
# DB_FILEPATH = "northwind_small.sqlite3"

# open connection and cursor
connection = sqlite3.connect('northwind_small.sqlite3')
cursor = connection.cursor()


# PART 1

# What are the ten most expensive items?
query_1 = """SELECT 
    ProductName FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;"""

result_1 = cursor.execute(query_1).fetchall()
print("10 most expensive items", result_1)


# What is the average age of an employee at the time of their hiring?
query_2 = """SELECT
    AVG(HireDate - BirthDate) AverageAge
    FROM Employee;"""

result_2 = cursor.execute(query_2).fetchall()
print('Employee average hire age', result_2)


# PART 2

# What are the ten most expensive items and their suppliers?
query_3 = """SELECT 
    ProductName, SupplierId FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;"""

result_3 = cursor.execute(query_3).fetchall()
print('10 most expensive and supplier', result_3)


# What is the largest category (by number of unique products in it)?
query_4 = """SELECT 
    CategoryName, MAX(Items) FROM
    (SELECT Category.CategoryName, COUNT(Product.Id) AS Items
    FROM Category, Product
    WHERE Category.Id = Product.CategoryId
    GROUP BY Category.Id);"""

result_4 = cursor.execute(query_4).fetchall()
print('Largest category', result_4)