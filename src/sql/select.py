import src.sql.db as datas

def get_user_id(user):
    print("getting user id...")
    theaterdb = datas.db()
    theaterdb.cursor.execute(f"SELECT id from users WHERE username = '{user.username}' AND password = '{user.password}';")
    return theaterdb.cursor.fetchone()[0]

def get_user(id):
    print("getting username...")
    theaterdb = datas.db()
    theaterdb.cursor.execute(f"SELECT username from users WHERE id = '{id}';")
    return theaterdb.cursor.fetchone()[0]

def get_salon_id(salon):
    print("getting salon id...")
    theaterdb = datas.db()
    theaterdb.cursor.execute(f"SELECT id from salons WHERE name = '{salon.name}' AND address = '{salon.address}';")
    return theaterdb.cursor.fetchone()[0]

def get_salon(id):
    print("getting salon name...")
    theaterdb = datas.db()
    theaterdb.cursor.execute(f"SELECT name from salons WHERE id = '{id}';")
    return theaterdb.cursor.fetchone()[0]


def get_show_id(show):
    print("getting show id...")
    theaterdb = datas.db()
    theaterdb.cursor.execute(f"SELECT id from shows WHERE name = '{show.name}' AND date_time = '{show.date_time}';")
    return theaterdb.cursor.fetchone()[0]

def get_show(id):
    print("getting show name...")
    theaterdb = datas.db()
    theaterdb.cursor.execute(f"SELECT name from shows WHERE id = '{id}';")
    return theaterdb.cursor.fetchone()[0]


def all_shows():
    theaterdb = datas.db()
    theaterdb.cursor.execute(f"SELECT * from shows;")
    return theaterdb.cursor.fetchall()        