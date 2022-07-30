#Database
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="theater"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE theater")
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)

#mycursor.execute("CREATE TABLE users (id INTEGER AUTO_INCREMENT PRIMARY KEY,  username VARCHAR(255), password VARCHAR(255))")
# mycursor.execute("CREATE TABLE tickets (id INT AUTO_INCREMENT PRIMARY KEY,  user_id int , FOREIGN KEY (user_id) REFERENCES users(id))")
sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
val = ("anis", "1234")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

sql = "INSERT INTO tickets (user_id) VALUES (%s)"
val = ([1])
mycursor.execute(sql, val)

mycursor.execute("select * from users join tickets on tickets.user_id = users.id")

# mycursor.execute("SHOW TABLES")

for x in mycursor:
  print("tables:", x)

