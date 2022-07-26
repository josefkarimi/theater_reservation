import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mynewpassword",
  database = "theater"
)

mycursor = mydb.cursor()
mycursor.execute
mycursor.execute("CREATE TABLE users (id int auto_increment PRIMARY Key , username varc 
