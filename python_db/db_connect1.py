import mysql.connector
db=mysql.connector.connect (
    host="localhost",
    user="root",
    password="Password@123"

)
print(db)

cursor=db.cursor()


query="create database animal"
cursor.execute(query)