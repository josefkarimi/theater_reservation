import src.sql.db as datas


def create_user(fname, lname, password):
    print("creating user...")
    theaterdb = datas.db()
    theaterdb.cursor.execute(f"INSERT INTO users (fname, lname, password) VALUES ('{fname}', '{lname}', '{password}');")
    theaterdb.db.commit()


def create_show():
    pass

def create_salon():
    pass

def create_ticket():
    pass