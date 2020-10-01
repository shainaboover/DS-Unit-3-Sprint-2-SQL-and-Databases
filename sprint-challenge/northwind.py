
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
# 10 most expensive items [('C⌠te de Blaye',), ('Thⁿringer Rostbratwurst',),
# ('Mishi Kobe Niku',), ("Sir Rodney's Marmalade",), ('Carnarvon Tigers',), 
# ('Raclette Courdavault',), ('Manjimup Dried Apples',), ('Tarte au sucre',), 
# ('Ipoh Coffee',), ('R÷ssle Sauerkraut')]


# What is the average age of an employee at the time of their hiring?
query_2 = """SELECT
    AVG(HireDate - BirthDate) AverageAge
    FROM Employee;"""

result_2 = cursor.execute(query_2).fetchall()
print('Employee average hire age', result_2)
# Employee average hire age [(37.22222222222222,)]


# PART 2

# What are the ten most expensive items and their suppliers?
query_3 = """SELECT 
    ProductName, SupplierId FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;"""

result_3 = cursor.execute(query_3).fetchall()
print('10 most expensive and supplier', result_3)
# 10 most expensive and supplier [('C⌠te de Blaye', 18), ('Thⁿringer Rostbratwurst', 12), 
# ('Mishi Kobe Niku', 4), ("Sir Rodney's Marmalade", 8), ('Carnarvon Tigers', 7), 
# ('Raclette Courdavault', 28), ('Manjimup Dried Apples', 24), ('Tarte au sucre', 29), 
# ('Ipoh Coffee', 20), ('R÷ssle Sauerkraut', 12)]


# What is the largest category (by number of unique products in it)?
query_4 = """SELECT 
    CategoryName, MAX(Items) FROM
    (SELECT Category.CategoryName, COUNT(Product.Id) AS Items
    FROM Category, Product
    WHERE Category.Id = Product.CategoryId
    GROUP BY Category.Id);"""

result_4 = cursor.execute(query_4).fetchall()
print('Largest category', result_4)
# Largest category [('Confections', 13)]
