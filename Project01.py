#Database
import mysql.connector
CREATE USER 'Anis'@'%' IDENTIFIED BY '1234'

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  password="mypassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
