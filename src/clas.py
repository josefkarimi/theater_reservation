import src.sql

class users:
    def __init__(self, fname, lname, password):
        self.fname = fname
        self.lname = lname
        self.password = password
        src.sql.creating.create_user(self.fname, self.lname, self.password)
        self.id = src.sql.select.get_user_id(self)