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

def getError():
  return mysql.connector