import src.sql.db as datas


def create_user(username, password):
    print("creating user...")
    theaterdb = datas.db()
    theaterdb.cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}');")
    theaterdb.db.commit()


def create_show(name, director_id, genre, date_time, salon_id, duration):
    print("creating show...")
    theaterdb = datas.db()
    theaterdb.cursor.execute(f"INSERT INTO shows ( name, director_id, genre, date_time, place_id, duration) VALUES ('{name}', {director_id}, '{genre}', '{date_time}', {salon_id}, '{duration}');")
    theaterdb.db.commit()
        
    

def create_salon(name, address, parkinglot, srow, scolumn, extra = 0):
    print("creating salon...")
    theaterdb = datas.db()
    theaterdb.cursor.execute(f"INSERT INTO salons (name, address, parkinglot, srow, scolumn, extra ) VALUES ('{name}', '{address}', {parkinglot}, {srow}, {scolumn}, {extra});")
    theaterdb.db.commit()

def create_ticket(user_id, show_id, n0):
    print("creating ticket...")
    theaterdb = datas.db()
    theaterdb.cursor.execute(f"INSERT INTO tickets (user_id, show_id, n0) VALUES ({user_id}, {show_id}, {n0});")
    theaterdb.db.commit()

# def get_my_tickets(user_id, show_id):


