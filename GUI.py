#GUI
from tkinter import *
import src.sql
import src.clas

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
    Button(login_screen, text = 'Login', width = 10, height = 1, command = login_verify).pack()

def register_user():
    
    username_info = username.get()
    password_info = password.get()
    # Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    # src.clas.users(username_info,password_info)
    # print(src.sql.allusers)

def login_verify():
    old_username = username_verify.get()
    old_password = password_verify.get()

    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    set_of_users = {('anis','1234')}

    for item in set_of_users :
        if old_username in item[0] and old_password in item[1] :
            login_success()

        elif old_username in item[0] and old_password not in item[1] :
            incorrect_password()
        
        elif old_username == '' or old_password == '' :
            wrong_entry()

        else :
            user_not_found()
    
def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title('Success')
    login_success_screen.geometry('150x100')

    Label(login_success_screen, text = 'Login Succeed').pack()

    Button(login_success_screen, text = 'Go to my panel', command = user_panel).pack()
    Button(login_success_screen, text = 'OK , EXIT', command = delete_login_success).pack()
    
def incorrect_password():
    global inc_password_screen
    inc_password_screen = Toplevel(login_screen)
    inc_password_screen.title('Error')
    inc_password_screen.geometry('150x100')

    Label(inc_password_screen, text = 'Invalid Password').pack()

    Button(inc_password_screen, text = 'OK', command = delete_incorrect_password).pack()

def wrong_entry():
    global none_entry_screen
    none_entry_screen = Toplevel(login_screen)
    none_entry_screen.title('Empty Box')
    none_entry_screen.geometry('150x100')

    Label(none_entry_screen, text = 'Wrong Input').pack()

    Button(none_entry_screen, text = 'OK', command = delete_wrong_entry).pack()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title('Nothing')
    user_not_found_screen.geometry("150x100")
    
    Label(user_not_found_screen, text="User Not Found").pack()
    
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

    Button(panel_screen, text = 'The Boxer', command = seat_selection).pack()

def seat_selection():
    global seat_screen
    seat_screen = Toplevel(panel_screen)
    seat_screen.title('Seat Selection')
    seat_screen.geometry('400x600')

    Label(seat_screen, text = 'SEATS', height="4", width="10", bg='red').grid(column=2, row=0)
    
    # global capacity
    # capacity = 5
    # for i in range(capacity):
    #     newButton = Button(seat_screen, text = str(i+1), command=lambda j=i+1: Board.playColumn(j, Board.getCurrentPlayer())).pack(side = TOP)
    Button(seat_screen,text="*Stage*", bg='pink', height="4", width="10").grid(column=2, row=1)
    
    global capacity
    row_capacity = 5
    column_capacity = 10
    for i in range(row_capacity):
        for j in range(column_capacity):
            newButton = Button(seat_screen, text = f'{j+1}.{i+1}',height="2", width="10",bg='grey', activebackground='cyan', command=confirm_selection(j,i)).grid(column=i, row=j+2)

def confirm_selection(x,y):
    global confirm_screen
    confirm_screen = Toplevel(seat_screen)
    confirm_screen.title('Confirm your ticket')
    confirm_screen.geometry('200x200')

    Label(confirm_screen, text = 'Are you sure ?').pack()
    Button(confirm_screen, text = 'YES', bg='green', command = print(f'The {x+1}.{y+1} ticket is yours')).pack()

def main_account_screen():
    
    global main_screen
    main_screen = Tk()  
    main_screen.geometry("300x250") 
    main_screen.title("Account Login") 
         
    Label(text="Choose Login Or Register", bg="blue", width="300", height="2", font=("Calibri", 13)).pack() 
    Label(text="").pack() 

    Button(text="Login", height="2", width="30", command = login).pack() 
    Label(text="").pack() 
    
    Button(main_screen, text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop() 

main_account_screen()
