from mysql.connector import connect
import mysql.connector

__db = connect(
    host="sigma.jasoncoding.com",
    user="ardeliaraminta",
    password="lunathemoonchild", 
    database='pcparts_db',
    port=5555
)

def getDb():
  if not __db.is_connected():
    __db.reconnect()
  return __db


def create_tables():
  '''Create tables if they do not exist yet'''

  cursor = __db.cursor()

  query = ("CREATE TABLE IF NOT EXISTS Category ("
    "id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, "
    "name VARCHAR(50) NOT NULL)")
  cursor.execute(query)

  query = ("CREATE TABLE IF NOT EXISTS Products ("
    "id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
    "product_name VARCHAR(50) NOT NULL,"
    "price FLOAT NOT NULL,"
    "category_id INT(6) UNSIGNED NOT NULL,"
    "FOREIGN KEY (category_id) REFERENCES Category (id) ON UPDATE CASCADE"
    ")")
  cursor.execute(query)

# 0-0 <3
  query = ("CREATE TABLE IF NOT EXISTS Customers ("
    "id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
    "first_Name VARCHAR(50) NOT NULL,"
    "last_Name VARCHAR(50) NOT NULL,"
    "email VARCHAR(50) NOT NULL,"
    "contact_number VARCHAR(20) NOT NULL,"
    "address VARCHAR(50) NOT NULL,"
    "city VARCHAR(50) NOT NULL,"
    "State VARCHAR(50) NOT NULL,"
    "zip INT(6)"
    ")")
  cursor.execute(query)

  query = ("CREATE TABLE IF NOT EXISTS Order_Transaction ("
    "id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
    "Customer_ID INT(6) UNSIGNED NOT NULL,"
    "Product_ID INT(6) UNSIGNED NOT NULL,"
    "quantity INT(6) UNSIGNED NOT NULL,"
    "Payment_type VARCHAR(50) NOT NULL,"
    "Order_Date DATE NOT NULL,"
    "Tax FLOAT UNSIGNED NOT NULL,"
    "total_amount FLOAT UNSIGNED NOT NULL,"
    "FOREIGN KEY (Customer_ID) REFERENCES Customers (id) ON UPDATE CASCADE,"
    "FOREIGN KEY (Product_ID) REFERENCES Products (id) ON UPDATE CASCADE"
    ")")
  cursor.execute(query)

def insert_category(name):
  ''''Enters a new category into the database'''
  __db = getDb()
  cursor = __db.cursor()

  query = (f"INSERT INTO Category (name) values ('{name}')")
  cursor.execute(query)

def insert_product(name, price, category_id):
  '''Enters a new product into the database'''
  __db = getDb()
  cursor = __db.cursor()

  query = ("INSERT INTO Products (product_name, price, category_id) values ("
  f"'{name}', '{price}', '{category_id}'"
  ")")
  cursor.execute(query)

def insert_customer(first_name, email, contact_number, address, city, state, last_name=None, zip_code=None):
  '''Enters a new customer into the database'''
  __db = getDb()
  cursor = __db.cursor()

  query = "INSERT INTO Customers (first_Name,"
  if last_name != None:
    query += "last_Name,"
  query += f" email, contact_number, address, city, State"
  if zip_code != None:
    query += ", zip"
  query += f") values ('{first_name}',"
  if last_name != None:
    query += f"'{last_name}',"
  query += f"'{email}', '{contact_number}', '{address}', '{city}', '{state}'"
  if zip_code != None:
    query += f", {zip_code}"
  query += ")"
  
  cursor.execute(query)

def insert_order_transaction(customer_id, product_id, quantity, payment_type, order_date, tax, total_amount):
  '''Enters a new order transaction into the database'''
  __db = getDb()
  cursor = __db.cursor()

  query = ("INSERT INTO Order_Transaction (Customer_ID, Product_ID, quantity, Payment_type, Order_Date, Tax, total_amount) values ("
  f"'{customer_id}', '{product_id}', '{quantity}', '{payment_type}', '{order_date}', '{tax}', '{total_amount}'"
  ")")
  cursor.execute(query)

# create_tables()
insert_category('CPU')