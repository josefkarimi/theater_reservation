#GUI
from tkinter import *
import customtkinter
import src.sql
import src.clas

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')
test = src.clas.users("a","a")

#Objects
mostafa = src.clas.users('Mostafa', 'Farahani')
molavi = src.clas.salons('Molavi', 'Enghelab Street',0,8,8)
hioshima = src.clas.shows('Hioshima',mostafa,'Historic','2022-8-2 20:00',molavi,'01:15:00')

nil = src.clas.users('Nil','Simon')
nofel = src.clas.salons('Nofel Loshato','Hafez Street',2,10,6,extra=10)
lastlover = src.clas.shows('Last Lover',nil,'Romance','2022-8-5 19:30',nofel,'01:20:00')

roya = src.clas.users('Roya','Kakakhani')
theatershahr = src.clas.salons('Theater-Shahr , Qashqaei ','4rah Valiasr',1,7,6,extra=15)
fever = src.clas.shows('Fever',roya,'Social','2022-8-7 20:30',theatershahr,'01:10:00')

neda = src.clas.users('Neda','Taslimian')
ruberu = src.clas.salons('Ru be Ru Mansion','Enghelab Street',0,9,5)
narenjaki = src.clas.shows('Narenjaki',neda,'Drama','2022-8-11 18:30',ruberu,'00:45:00')

parsa = src.clas.users('Parsa','Mohammadzadeh')
simorq = src.clas.salons('Simorq','Hafez Street',0,5,6,extra=8)
passive = src.clas.shows('From Passive To Passive',parsa,'Drama','2022-8-15 17:30',simorq,'00:50:00')

def register():
    
    global register_screen
    register_screen = Toplevel(main_screen) 
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    username = StringVar()
    global password
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    
    global username_entry
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
   
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()

    global password_entry
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    Label(register_screen, text="").pack()

    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()

def login():
    
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title('Login')
    login_screen.geometry('300x250')

    Label(login_screen, text = 'Please enter details below to login').pack()
    Label(login_screen, text = '').pack()

    global username_verify
    username_verify = StringVar()
    global password_verify
    password_verify = StringVar()

    Label(login_screen, text = 'Username * ').pack()
    
    global username_login_entry
    username_login_entry = Entry(login_screen, textvariable = username_verify)
    username_login_entry.pack()

    Label(login_screen, text = '').pack()
    Label(login_screen, text = 'Password * ').pack()

    global password_login_entry
    password_login_entry = Entry(login_screen, textvariable = password_verify , show = '*')
    password_login_entry.pack()

    Label(login_screen, text = '').pack()
    Button(login_screen, text = 'Login', width = 10, height = 1,bg="blue", command = login_verify).pack()

def register_user():
    
    global username_info
    global password_info
    username_info = username.get()
    password_info = password.get()
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    src.clas.users(username_info,password_info)
    print(src.sql.allusers)
    register_screen.destroy()

def login_verify():
    old_username = username_verify.get()
    old_password = password_verify.get()

    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    # set_of_users = {('anis','1234')}
    global user
    user = src.sql.select.get_object(old_username)

    
    if old_username == "" or old_password == "" :
        wrong_entry()
    elif user != None:
        if user.username == old_username and old_password == user.password :
            login_success()

        elif user.username == old_username and old_password != user.password :
            incorrect_password()
    elif user == None :
        user_not_found()
        
    else :
        print("WTF")
    
def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title('Success')
    login_success_screen.geometry('150x100')

    Label(login_success_screen, text = 'Login Succeed').pack()

    Button(login_success_screen, text = 'Go to my panel',bg="green", command = user_panel).pack()
    Button(login_success_screen, text = 'OK , EXIT',bg="red", command = delete_login_success).pack()
    
def incorrect_password():
    global inc_password_screen
    inc_password_screen = Toplevel(login_screen)
    inc_password_screen.title('Error')
    inc_password_screen.geometry('150x100')

    Label(inc_password_screen, text = 'Invalid Password',bg="yellow").pack()

    Button(inc_password_screen, text = 'OK', command = delete_incorrect_password).pack()

def wrong_entry():
    global none_entry_screen
    none_entry_screen = Toplevel(login_screen)
    none_entry_screen.title('Empty Box')
    none_entry_screen.geometry('150x100')

    Label(none_entry_screen, text = 'Wrong Input',bg="yellow").pack()

    Button(none_entry_screen, text = 'OK', command = delete_wrong_entry).pack()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title('Nothing')
    user_not_found_screen.geometry("150x100")
    
    Label(user_not_found_screen, text="User Not Found",bg="yellow").pack()
    
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_login_success():
    login_success_screen.destroy()

def delete_incorrect_password():
    inc_password_screen.destroy()

def delete_wrong_entry():
    none_entry_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def user_panel():
    
    global panel_screen
    panel_screen = Toplevel(login_success_screen)
    panel_screen.title('Your Panel')
    panel_screen.geometry('300x250')

    Label(panel_screen, text = 'Shows available', bg="green").pack()
    Label(text="").pack()
    Button(panel_screen, text = hioshima.name ,bg="grey", command = show_h_detail).pack()
    Label(text="").pack()
    Button(panel_screen, text = lastlover.name ,bg="grey", command = show_l_detail).pack()
    Label(text="").pack()
    Button(panel_screen, text = fever.name ,bg="grey", command = show_f_detail).pack()
    Label(text="").pack()
    Button(panel_screen, text = narenjaki.name ,bg="grey", command = show_n_detail).pack()
    Label(text="").pack()
    Button(panel_screen, text = passive.name ,bg="grey", command = show_p_detail).pack()
    Label(text="").pack()
    Button(panel_screen, text = 'Show my tickets', bg='pink', command = show_my_tickets).pack()
    
def show_h_detail():
    
    global detail_h_screen
    detail_h_screen = Toplevel(panel_screen)
    detail_h_screen.title(hioshima.name + ' details')
    detail_h_screen.geometry('300x250')

    Label(detail_h_screen, text = hioshima.name + '\n' + f'Directed by {hioshima.director.username} {hioshima.director.password}' + '\n' + hioshima.genre + '\n' + str(hioshima.date_time) + '\n' + f'In the {hioshima.salon.name} salon : {hioshima.salon.address} \n ' + 'Nearby Parkinglots : ' + str(hioshima.salon.parkinglot) + '\n' + 'Duration : ' + str(hioshima.duration),bg="pink").pack()
    
    Button(detail_h_screen, text = 'Buy ticket' ,bg="purple", command = seat_selection).pack()
    Button(detail_h_screen, text = 'Go back' ,bg="grey", command = delete_h_details).pack()
    global z
    z = hioshima
    
def show_l_detail():
    
    global detail_l_screen
    detail_l_screen = Toplevel(panel_screen)
    detail_l_screen.title(lastlover.name + ' details')
    detail_l_screen.geometry('300x250')

    Label(detail_l_screen, text = lastlover.name + '\n' + f'Directed by {lastlover.director.username} {lastlover.director.password}' + '\n' + lastlover.genre + '\n' + str(lastlover.date_time) + '\n' + f'In the {lastlover.salon.name} salon : {lastlover.salon.address} \n ' + 'Nearby Parkinglots : ' + str(lastlover.salon.parkinglot) + '\n' + 'Duration : ' + str(lastlover.duration),bg="pink").pack()
    
    Button(detail_l_screen, text = 'Buy ticket' ,bg="purple", command = seat_selection).pack()
    Button(detail_l_screen, text = 'Go back' ,bg="grey", command = delete_l_details).pack()
    global z
    z = lastlover

def show_f_detail():
    
    global detail_f_screen
    detail_f_screen = Toplevel(panel_screen)
    detail_f_screen.title(fever.name + ' details')
    detail_f_screen.geometry('300x250')

    Label(detail_f_screen, text = fever.name + '\n' + f'Directed by {fever.director.username} {fever.director.password}' + '\n' + fever.genre + '\n' + str(fever.date_time) + '\n' + f'In the {fever.salon.name} salon : {fever.salon.address} \n ' + 'Nearby Parkinglots : ' + str(fever.salon.parkinglot) + '\n' + 'Duration : ' + str(fever.duration),bg="pink").pack()
    
    Button(detail_f_screen, text = 'Buy ticket' ,bg="purple", command = seat_selection).pack()
    Button(detail_f_screen, text = 'Go back' ,bg="grey", command = delete_f_details).pack()
    global z
    z = fever

def show_n_detail():
    
    global detail_n_screen
    detail_n_screen = Toplevel(panel_screen)
    detail_n_screen.title(narenjaki.name + ' details')
    detail_n_screen.geometry('300x250')

    Label(detail_n_screen, text = narenjaki.name + '\n' + f'Directed by {narenjaki.director.username} {narenjaki.director.password}' + '\n' + narenjaki.genre + '\n' + str(narenjaki.date_time) + '\n' + f'In the {narenjaki.salon.name} salon : {narenjaki.salon.address} \n ' + 'Nearby Parkinglots : ' + str(narenjaki.salon.parkinglot) + '\n' + 'Duration : ' + str(narenjaki.duration),bg="pink").pack()
    
    Button(detail_n_screen, text = 'Buy ticket' ,bg="purple", command = seat_selection).pack()
    Button(detail_n_screen, text = 'Go back' ,bg="grey", command = delete_n_details).pack()
    global z
    z = narenjaki
    
def show_p_detail():
    
    global detail_p_screen
    detail_p_screen = Toplevel(panel_screen)
    detail_p_screen.title(passive.name + ' details')
    detail_p_screen.geometry('300x250')
    Label(detail_p_screen, text = passive.name + '\n' + f'Directed by {passive.director.username} {passive.director.password}' + '\n' + passive.genre + '\n' + str(passive.date_time) + '\n' + f'In the {passive.salon.name} salon : {passive.salon.address} \n ' + 'Nearby Parkinglots : ' + str(passive.salon.parkinglot) + '\n' + 'Duration : ' + str(passive.duration),bg="pink").pack()
    
    Button(detail_p_screen, text = 'Buy ticket' ,bg="purple", command = seat_selection).pack()
    Button(detail_p_screen, text = 'Go back' ,bg="grey", command = delete_p_details).pack()
    global z
    z = passive
 
def delete_h_details():
    detail_h_screen.destroy()    

def delete_l_details():
    detail_l_screen.destroy()

def delete_f_details():
    detail_f_screen.destroy()

def delete_n_details():
    detail_n_screen.destroy()
    
def delete_p_details():
    detail_p_screen.destroy()    

def seat_selection():
    global seat_screen
    seat_screen = Toplevel(panel_screen)
    seat_screen.title('Seat Selection')
    seat_screen.geometry('450x600')

    Label(seat_screen, text = 'SEATS', bg='red').grid(column=5, row=0)
    
    Button(seat_screen,text="*Stage*", bg='pink').grid(column=5, row=1)
    
    global row_capacity
    row_capacity = 8
    global column_capacity
    column_capacity = 11
    for i in range(row_capacity):
        global x
        x = i+1
        for j in range(column_capacity):
            global y
            y = j+1 
            newButton = Button(seat_screen, text = f'{x}.{y}' ,height="2", width="4",bg='grey', activebackground='cyan').grid(column=j, row=i+2)
    
    global row
    row = IntVar()
    global column
    column = IntVar()
    
    row_lable = Label(seat_screen, text="Row * ").grid(column=1,row=12)
    Label(seat_screen, text="").grid(column=1,row=13)
    
    global row_entry
    row_entry = Entry(seat_screen, textvariable=row ,width="4")
    row_entry.grid(column=2,row=12)
    
    column_lable = Label(seat_screen, text="Column * ").grid(column=1,row=14)
    Label(seat_screen, text="").grid(column=1,row=15)
    
    global column_entry
    column_entry = Entry(seat_screen, textvariable=column ,width="4")
    column_entry.grid(column=2,row=14)
    
    Button(seat_screen, text="OK", width=4, height=1, bg="blue", command=confirm_selection).grid(column=4,row=14)
    
def confirm_selection():
    global row_info
    global column_info
    row_info = row.get()
    column_info = column.get()
    if int(row_info) <= row_capacity and int(column_info) <= column_capacity :
        global confirm_screen
        confirm_screen = Toplevel(seat_screen)
        confirm_screen.title('Confirm your ticket')
        confirm_screen.geometry('200x200')
        
        Label(confirm_screen, text = f'Ticket number {row_info}.{column_info}').grid(column=2,row=1)
        
        Button(confirm_screen, text = 'YES', bg='green', command = ticket_bought).grid(column=1,row=3)
        Button(confirm_screen, text = 'NO', bg='red', command = delete_confirmation).grid(column=3,row=3)
        
        
def ticket_bought():
    n0 = int(row_info)*10 + int(column_info)
    for item in src.sql.select.all_tickets():
        print(item)
        
        if z.id == item[2] and n0 == item[3]:
            print("you cant buy this ticket ! ")
            break
    else : 
        src.clas.tickets(user,z,n0)
    
    print(user.username,' ',user.mytickets)
    
    
    if row_info == "0" or column_info == "0" :
        wrong_entry()

# def show_my_tickets():
#     global see_tickets_screen
#     see_tickets_screen = Toplevel(confirm_screen)
#     see_tickets_screen.title('Your Tickets')
#     see_tickets_screen.geometry('200x200')
    
#     Label(see_tickets_screen, text = f'user {user.username} has {user.mytickets} tickets .').pack()
#     Button(see_tickets_screen, text = 'OK , Go Back', command=delete_see_tickets_screen)
    
#     print(user.username,' ',user.mytickets)

def delete_see_tickets_screen():
    see_tickets_screen.destroy()
            
def delete_ticket_not_available_screen():
    ticket_not_available_screen.destroy()    
            
def delete_confirmation():
    confirm_screen.destroy()

def main_account_screen():
    
    global main_screen
    main_screen = customtkinter.CTk()  
    main_screen.geometry("300x250") 
    main_screen.title("Account Login")
         
    Label(text="Choose Login Or Register", bg="blue", width="300", height="2", font=("Calibri", 13)).pack() 
    Label(text="",bg='black').pack() 

    Button(text="Login", height="2", width="30", command = login).pack() 
    
    Label(text="",bg='black').pack() 
    
    Button(main_screen, text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop() 

main_account_screen()
