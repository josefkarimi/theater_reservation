import src.sql.db as datas

def get_user_id(user):
    print("getting user id...")
    theaterdb = datas.db()
    theaterdb.cursor.execute(f"SELECT id from users WHERE fname = '{user.fname}' AND lname = '{user.lname}' AND password = '{user.password}';")
    return theaterdb.cursor.fetchone()[0]