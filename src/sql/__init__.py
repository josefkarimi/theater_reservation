import mysql.connector
import src.sql.db as datas
import src.sql.creating
import src.sql.select

print("import compelete ...")
theaterdb = datas.db()

create_database = (input("do you want to create database? \n")).lower()
if create_database == "y" or create_database == "yes":
    with open("src/sql/initial.sql") as f :
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
        theaterdb.cursor.execute(item)
        print(item[0:30])
        if "INSERT" in item :
            theaterdb.db.commit()

allusers = set()
allsalons = set()
allshows = set()
