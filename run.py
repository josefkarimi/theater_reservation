import src.sql
import src.clas

ali = src.clas.users("ali", "leyla")
gholi = src.clas.users("ali", "hatami")
hasan = src.clas.users("kachal", "chenaze")
farhang = src.clas.salons("farhang", "shariati", 1, 14, 11)
tame_gilas = src.clas.shows("tamegilas",ali,"drama","2022-12-12 20:00:00", farhang,"00:50:00")
josefticket1 = src.clas.tickets(hasan, tame_gilas,6)
josefticket2 = src.clas.tickets(hasan,tame_gilas,7)
# print(farhang.id, tame_gilas.director, tame_gilas.salon,josefticket1.n0)
# print(hasan.mytickets, hasan.myshows)
# for item in src.sql.select.all_shows():
#     print(item,"\n", "-"*100 )
for item in src.sql.allusers:
    print("item is :", item.username)
print(src.sql.select.get_object("ali"))