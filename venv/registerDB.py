from db import getDB
from bcrypt import gensalt, hashpw

def register_user(username,password):
    db = getDB()
    cursor = db.cursor()

    query = "INSERT INTO users ( username, password) VALUES (%s, %s)"
    new_pass = hashpw

    values = (username, password)
    

 