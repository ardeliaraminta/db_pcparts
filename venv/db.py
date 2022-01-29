from mysql.connector import connect
import datetime as dt

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
    "Stock INT(6) UNSIGNED NOT NULL,"
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

def insert_product(name, price, category_id,stock):
  '''Enters a new product into the database'''
  __db = getDb()
  cursor = __db.cursor()

  query = ("INSERT INTO Products (product_name, price, category_id, Stock) values ("
  f"'{name}', '{price}', '{category_id}', {stock}"
  ")")
  cursor.execute(query)
  __db.commit()


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
  __db.commit()
  print(query)

def insert_order_transaction(customer_id, product_id, quantity, payment_type, order_date, tax, total_amount):
  '''Enters a new order transaction into the database'''
  __db = getDb()
  cursor = __db.cursor()

  query = ("INSERT INTO Order_Transaction (Customer_ID, Product_ID, quantity, Payment_type, Order_Date, Tax, total_amount) values ("
  f"'{customer_id}', '{product_id}', '{quantity}', '{payment_type}', '{order_date}', '{tax}', '{total_amount}'"
  ")")
  cursor.execute(query)
  __db.commit()

def get_all_categories():
  '''Returns all categories in the database'''
  __db = getDb()
  cursor = __db.cursor()

  query = "SELECT * FROM Category"
  cursor.execute(query)

  return cursor.fetchall()

def get_all_products():
  '''Returns all products in the database'''
  __db = getDb()
  cursor = __db.cursor()

  query = "SELECT * FROM Products"
  cursor.execute(query)

  return cursor.fetchall()

def get_history_order(customer_id):
  '''Returns all order transactions in the database'''
  __db = getDb()
  cursor = __db.cursor()

  query = f"SELECT * FROM Order_Transaction WHERE Customer_ID = {customer_id}"
  cursor.execute(query)

  return cursor.fetchall()

def get_all_orders_of_customers():
  '''Returns all order transactions in the database'''
  __db = getDb()
  cursor = __db.cursor()

  query = "SELECT * FROM Order_Transaction"
  cursor.execute(query)

  return cursor.fetchall()

def search_products(name):
  '''Returns all products in the database'''
  __db = getDb()
  cursor = __db.cursor()

  query = f"SELECT id,product_name,price FROM Products WHERE product_name LIKE '%{name}%'"
  cursor.execute(query)

  return cursor.fetchall()

def get_all_customers():
  '''Returns all customers in the database'''
  __db = getDb()
  cursor = __db.cursor()

  query = "SELECT * FROM Customers"
  cursor.execute(query)

  return cursor.fetchall()

def get_tax(product_id):
  '''Returns the tax of a product'''
  __db = getDb()
  cursor = __db.cursor()

  query = f"SELECT price FROM Products WHERE id = {product_id}"
  cursor.execute(query)
  price = cursor.fetchone()
  tax = price[0]*0.08
  return tax

def get_total_amount(product_id,quantity):
  '''Returns the total amount of a product'''
  __db = getDb()
  cursor = __db.cursor()

  query = f"SELECT price FROM Products WHERE id = {product_id}"
  cursor.execute(query)
  price = cursor.fetchone()
  tax=get_tax(product_id)
  total = (price[0]*quantity)+tax
  return total

def create_order_transaction(product_id,customer_id,quantity,payment_type,order_date):
  '''Creates an order transaction'''
  __db = getDb()
  cursor = __db.cursor()

  query_check_stock=f"SELECT Stock FROM Products WHERE id = {product_id}"
  cursor.execute(query_check_stock)
  stock=cursor.fetchone()

  if stock[0]==0:
    return "Out of stock"
  elif stock[0]<quantity:
    return "Stock left"+str(stock[0])
  else:
    query = ("INSERT INTO Order_Transaction (Customer_ID, Product_ID, quantity, Payment_type, Order_Date, Tax, total_amount) values ("
    f"'{customer_id}', '{product_id}', '{quantity}', '{payment_type}', '{order_date}', '{get_tax(product_id)}', '{get_total_amount(product_id,quantity)}'"
    ")")
    cursor.execute(query)
    query_to_update_stock = f"UPDATE Products SET Stock = Stock - {quantity} WHERE id = {product_id}"
    cursor.execute(query_to_update_stock)
    __db.commit()

def delete_product_from_order(product_id,order_id):
  '''Deletes a product from an order'''
  __db = getDb()
  cursor = __db.cursor()

  query = f"DELETE FROM Order_Transaction WHERE Product_ID = {product_id} AND id = {order_id}"
  cursor.execute(query)
  __db.commit()


def receipt(first_name,last_name):
  '''Returns a receipt of an order'''
  __db = getDb()
  cursor = __db.cursor()

  query = "SELECT c.first_Name, c.last_Name, c.email, p.product_name, p.price, o.quantity, o.Payment_type, o.Order_Date, o.Tax, o.total_amount, t.name, s.first_name, s.last_name, m.manufacturer FROM Customers c INNER JOIN Order_Transaction o on c.id=o.Customer_ID INNER JOIN Products p on o.Product_ID=p.id INNER JOIN Category t on p.category_id=t.id INNER JOIN staff s on s.id=o.staff_id INNER JOIN Manufacturers m on m.product_id=p.id "
  query+=f" WHERE c.first_Name='{first_name}' AND c.last_Name='{last_name}'"
  cursor.execute(query)

  return cursor.fetchall()

def get_total_receipt(first_name, last_name):
  '''Returns a receipt of an order'''
  __db = getDb()
  cursor = __db.cursor()

  query = "SELECT o.total_amount FROM Customers c INNER JOIN Order_Transaction o on c.id=o.Customer_ID INNER JOIN Products p on o.Product_ID=p.id INNER JOIN Category t on p.category_id=t.id "
  query+=f" WHERE c.first_Name='{first_name}' AND c.last_Name='{last_name}'"
  cursor.execute(query)
  total_list=cursor.fetchall()
  total=0
  for cost in total_list:
    total+=cost[0]
  return total




def get_products_per_category(category_name):
  '''Returns all products in a category'''
  __db = getDb()
  cursor = __db.cursor()

  query = f"SELECT p.product_name, p.price, c.name FROM Products p INNER JOIN Category c on p.category_id=c.id WHERE c.name = '{category_name}'"
  cursor.execute(query)

  return cursor.fetchall()


def get_products_by_ascending_price():
  '''Returns all products in a category'''
  __db = getDb()
  cursor = __db.cursor()

  query = f"SELECT p.product_name, p.price, c.name FROM Products p INNER JOIN Category c on p.category_id=c.id ORDER BY p.price ASC"
  cursor.execute(query)

  return cursor.fetchall()

def get_products_by_descending_price():
  '''Returns all products in a category'''
  __db = getDb()
  cursor = __db.cursor()

  query = f"SELECT p.product_name, p.price, c.name FROM Products p INNER JOIN Category c on p.category_id=c.id ORDER BY p.price DESC"
  cursor.execute(query)

  return cursor.fetchall()

def get_products_by_price_range(price_range_min,price_range_max):
  '''Returns all products in a category'''
  __db = getDb()
  cursor = __db.cursor()

  query = f"SELECT p.product_name, p.price, c.name FROM Products p INNER JOIN Category c on p.category_id=c.id WHERE p.price BETWEEN {price_range_min} AND {price_range_max}"
  cursor.execute(query)

  return cursor.fetchall()

def get_all_manufacturer():
  '''Returns all manufacturers in the database'''
  __db = getDb()
  cursor = __db.cursor()

  query = "SELECT * FROM Manufacturers"
  cursor.execute(query)

  return cursor.fetchall()

def get_all_staff():
  '''Returns all staff in the database'''
  __db = getDb()
  cursor = __db.cursor()

  query = "SELECT * FROM staff"
  cursor.execute(query)

  return cursor.fetchall()

def get_orders_of_staff(first_name,last_name):
  '''Returns all orders of a staff'''
  __db = getDb()
  cursor = __db.cursor()

  query = f"SELECT * FROM Order_Transaction WHERE staff_id = (SELECT id FROM staff WHERE first_name = '{first_name}' AND last_name = '{last_name}')"
  cursor.execute(query)

  return cursor.fetchall()

def count_duplicate_staff(first_name, last_name,contact_number,address):
  '''Counts duplicate staff'''
  __db = getDb()
  cursor = __db.cursor()

  query = f"SELECT COUNT(*) FROM staff WHERE first_name = '{first_name}' AND last_name = '{last_name}' AND contact_number = '{contact_number}' AND address = '{address}'"
  cursor.execute(query)

  return cursor.fetchall()

def add_staff(first_name, last_name,contact_number,address):
  '''Adds a staff to the database'''
  if count_duplicate_staff(first_name,last_name,contact_number, address)[0]>1:
    return "Staff already exists"
  else:
    __db = getDb()
    cursor = __db.cursor()

    query = f"INSERT INTO staff (first_name, last_name, contact_number, address) VALUES ('{first_name}', '{last_name}', '{contact_number}', '{address}')"
    cursor.execute(query)
    __db.commit()

def delete_duplicate_staff():
  '''Deletes duplicate staff'''
  __db = getDb()
  cursor = __db.cursor()

  query = f"DELETE t1 FROM staff t1 INNER JOIN staff t2 WHERE t1.id < t2.id AND t1.first_name = t2.first_name AND t1.last_name=t2.last_name AND t1.contact_number=t2.contact_number AND t1.address=t2.address;"
  cursor.execute(query)
  __db.commit()

def get_products_by_manufacturer(manufacturer_name):
  '''Returns all products of a manufacturer'''
  __db = getDb()
  cursor = __db.cursor()

  query = f"SELECT p.product_name, p.price, c.name FROM Products p INNER JOIN Category c on p.category_id=c.id INNER JOIN Manufacturers m on p.id=product_id WHERE m.manufacturer = '{manufacturer_name}'"
  cursor.execute(query)

  return cursor.fetchall()



print(receipt('John','gagsg'))
def get_products_by_category(category_name):
  __db = getDb()
  cursor = __db.cursor()

  query = f"SELECT * from Products p INNER JOIN Category cat ON p.category_id = cat.id WHERE cat.name ='{category_name}'"
  cursor.execute(query)

  return cursor.fetchall()

print(get_products_by_category("RAM"))
