import src.sql

class users:
    def __init__(self, fname, lname, password):
        self.fname = fname
        self.lname = lname
        self.password = password
        src.sql.creating.create_user(self.fname, self.lname, self.password)
        self.id = src.sql.select.get_user_id(self)


class places:
    def __init__(self, name, address, parkinglot, srow, scolumn, *, extra = 0):
        self.name = name
        self.address = address
        self.parkinglot = parkinglot
        self.srow = srow
        self.scolumn = scolumn
        self.extra = extra
        self.capacity = self.capacity(extra)
        src.sql.creating.create_salon(self.name, self.address, self.parkinglot, self.srow, self.scolumn, self.extra)
        self.id = src.sql.select.get_salon_id(self)
    def capacity(self, extra = 0) :
        return self.scolumn * self.srow + self.extra
    