import mysql.connector


dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password'
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#Create a database
cursorObject.execute("CREATE DATABASE dcrmdb")

print("Database Created!")
