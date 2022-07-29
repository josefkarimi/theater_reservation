import src.sql

class users:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        try:
            src.sql.creating.create_user(self.username, self.password)
        except :
            print("You cant enter this username...")
            return
        self.id = src.sql.select.get_user_id(self)
        self.mytickets = {}
        self.myshows = []
        src.sql.allusers.add(self)
    
    def buyticket(self, show_id, n0):
        try:
            self.mytickets[show_id].append(n0)
        except:
            self.mytickets.update({show_id:[n0]})
        finally:
            self.myshows = list(self.mytickets.keys())


class salons:
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
        src.sql.allsalons.add(self)
    
    def capacity(self, extra = 0) :
        return self.scolumn * self.srow + self.extra
    

class shows:
    def __init__ (self, name, director, genre, date_time, salon, duration):
        self.name = name 
        self.director = director
        self.genre = genre
        self.date_time = date_time
        self.salon = salon
        self.duration = duration
        src.sql.creating.create_show(self.name, self.director.id, self.genre, self.date_time, self.salon.id, self.duration)
        self.id = src.sql.select.get_show_id(self)
        src.sql.allshows.add(self)
class tickets :
    def __init__(self, user, show, n0):
        self.user = user
        self.show = show
        self.n0 = n0
        src.sql.creating.create_ticket(self.user.id, self.show.id, self.n0)
        users.buyticket(self.user, self.show.id, self.n0)