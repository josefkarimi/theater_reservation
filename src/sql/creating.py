import src.sql.db as datas


def create_user(fname, lname, password):
    print("creating user...")
    theaterdb = datas.db()
    theaterdb.cursor.execute(f"INSERT INTO users (fname, lname, password) VALUES ('{fname}', '{lname}', '{password}');")
    theaterdb.db.commit()


def create_show():
    pass

def create_salon(name, address, parkinglot, srow, scolumn, extra = 0):
    print("creating salon...")
    theaterdb = datas.db()
    theaterdb.cursor.execute(f"INSERT INTO salons (name, address, parkinglot, srow, scolumn, extra ) VALUES ('{name}', '{address}', {parkinglot}, {srow}, {scolumn}, {extra});")
    theaterdb.db.commit()

def create_ticket():
    pass