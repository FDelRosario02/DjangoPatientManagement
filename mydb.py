import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Admin.1234',
)
#prepare a cursor Object
cursorObject = dataBase.cursor()

#Create a Database
cursorObject.execute("CREATE DATABASE pmdp")

print("Creado")