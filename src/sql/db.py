import mysql.connector
class db:
    def __init__(self, host="localhost", user="root", password="mynewpassword", database="theater"):
        self.db = mysql.connector.connect(host='localhost',
                                user="root", #input("please enter your username for mysql: \n"),
                                password = "",
                                database = "theater")  #input("and your password: \n"))
        self.cursor = self.db.cursor()
