import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                                user="root", #input("please enter your username for mysql: \n"),
                                password = "mynewpassword")  #input("and your password: \n"))


mycursor = mydb.cursor()

with open("src/sql/create.sql") as f :
    ex = []
    temp = ""
    for line in f :
        if line[0:2] == "--":
            pass
        else:
            temp += line
            if  ";" in temp:
                ex.append(temp)
                temp = ""

for n, item in enumerate(ex):
    mycursor.execute(item)
    print(item[0:30])
    if "INSERT" in item :
        mydb.commit()
