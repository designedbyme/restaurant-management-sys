import csv
import os
import tkinter as tk
#import tkmacosx as tmacc
from tkmacosx import Button
from PIL import Image, ImageTk


def host_hompage():
    host = tk.Toplevel(root)
    host.geometry("1488x945")
    s = tk.Label(host, image=host_homepage).pack()

    header = tk.Label(host, 
                      text=f"Welcome, EASYUSER",
                      font=("Inter", 30, "bold"), 
                      bg="white", fg="black")
    header.place(relx = 0.1, rely = 0.19)

    subHeader = tk.Label(host, 
                      text="End Job",
                      font=("Inter", 30, "bold"), 
                      bg="white", fg="black")
    subHeader.place(relx = 0.225, rely = 0.375)

    signoutButton = tk.Button(host, 
                              image = home_signOutButt, 
                              bg="white", 
                              highlightthickness=0, takefocus=0, bd=0, 
                              command = lambda: [signInn(), host.withdraw()])
    signoutButton.place(relx = 0.14, rely = 0.48)


    tableButt = tk.Button(host, 
                         image = home_tableButt, 
                         bg="white", 
                         highlightthickness=0, takefocus=0, bd=0, 
                         command = lambda: [signInn(), host.withdraw()])
    tableButt.place(relx = 0.6, rely = 0.43)


def waiter_hompage():
    waiter = tk.Toplevel(root)
    waiter.geometry("1488x945")
    s = tk.Label(waiter, image=waiter_homepage).pack()

    header = tk.Label(waiter, 
                      text=f"Welcome, EASYUSER",
                      font=("Inter", 30, "bold"), 
                      bg="white", fg="black")
    header.place(relx = 0.1, rely = 0.19)

    subHeader = tk.Label(waiter, 
                      text="End Job",
                      font=("Inter", 30, "bold"), 
                      bg="white", fg="black")
    subHeader.place(relx = 0.225, rely = 0.375)

    signoutButton = tk.Button(waiter, 
                              image = home_signOutButt, 
                              bg="white", 
                              highlightthickness=0, bd=0, 
                              command = lambda: [signInn(), waiter.withdraw()])
    signoutButton.place(relx = 0.14, rely = 0.48)


    menuButt = tk.Button(waiter, 
                         image = home_menuButt, 
                         bg="white", 
                         highlightthickness=0, takefocus=0, bd=0, 
                         command = lambda: [signInn(), waiter.withdraw()])
    menuButt.place(relx = 0.6, rely = 0.4)

    orderButt= tk.Button(waiter, 
                         image = home_ordersButt, 
                         bg="white", 
                         highlightthickness=0, bd=0, 
                         command = lambda: [orderHub(), waiter.withdraw()])
    orderButt.place(relx = 0.6, rely = 0.64)

def menuHub():
    menu = tk.Toplevel(root)
    menu.geometry("1488x945")
    s = tk.Label(menu, image=m_hub).pack()

def orderHub():
    order = tk.Toplevel(root)
    order.geometry("1488x945")    
    s = tk.Label(order, image=o_hub).pack()

    header = tk.Label(order, 
                      text=f"Table X's Order:",
                      font=("Inter", 40, "bold"), 
                      bg="#FF88A9", fg="white")
    header.place(relx = 0.05, rely = 0.1)

    bck = tk.Button(order, 
                    image=o_prev,
                    bg="#FF88A9", 
                    highlightthickness=0, 
                    takefocus=0, bd=0, 
                    command = lambda: [job_select(), order.withdraw()])
    bck.place(relx = 0.35, rely = 0.1)
    nxt = tk.Button(order, 
                    image=o_next ,
                    bg="#FF88A9", 
                    highlightthickness=0, 
                    takefocus=0, bd=0,
                    command = lambda: [job_select(), order.withdraw()])
    nxt.place(relx = 0.4, rely = 0.1)


    credit = tk.Button(order, 
                       image=o_credit,
                       bg="#FF88A9", 
                       highlightthickness=0, takefocus=0, bd=0, 
                       command = lambda: [job_select(), order.withdraw()])
    credit.place(relx = 0.6, rely = 0.3)

    cash = tk.Button(order, 
                     image=o_cash,
                     bg="#FF88A9", 
                     highlightthickness=0, takefocus=0, bd=0, 
                     command = lambda: [job_select(), order.withdraw()])
    cash.place(relx = 0.6, rely = 0.5)

    hold = tk.Button(order, 
                     image=o_hold,
                     bg="#FF88A9", 
                     highlightthickness=0, takefocus=0, bd=0, 
                     command = lambda: [job_select(), order.withdraw()])
    hold.place(relx = 0.6, rely = 0.7)
    

def signUp():
    signUpPage = tk.Toplevel(root)
    signUpPage.geometry("1488x945")
    
    s = tk.Label(signUpPage, image=s_l_page).pack()
    
    sign_up = tk.Label(signUpPage, text="Sign Up", font=('Didot', 48),fg="black",bg="white")
    sign_up.place(relx = 0.43, rely = 0.249)

    fname = tk.Label(signUpPage, text="Full Name:", font=('Didot', 32),fg="black",bg="white")
    fname.place(relx = 0.3, rely = 0.4)

    email = tk.Label(signUpPage, text="Email:", font=('Didot', 32),fg="black",bg="white")
    email.place(relx = 0.345, rely = 0.5)
    
    password = tk.Label(signUpPage, text="Password:", font=('Didot', 32),fg="black",bg="white")
    password.place(relx = 0.31, rely = 0.6)


    back_button = tk.Button(signUpPage, image=backButt, bg="#FFE2EA", highlightthickness = 0, bd = 0, command=signUpPage.withdraw)
    back_button.place(relx=0.05, rely=0.05, anchor= 'center')
    
    name = tk.Entry(signUpPage, 
                    width = 22, 
                    font=("Inria Sans", 25),
                    fg="#FF88A9",bg="#FFE2EA",
                    highlightthickness = 0, bd = 0)
    name.place(relx = 0.435, rely = 0.41)
    
    email = tk.Entry(signUpPage,
                     width = 22, 
                     font=("Inria Sans", 25),
                     fg="#FF88A9",bg="#FFE2EA",
                     highlightthickness = 0, bd = 0)
    email.place(relx = 0.435, rely = 0.51)
    
    pw = tk.Entry(signUpPage,
                  width = 22,
                  font=("Inria Sans", 25),
                  fg="#FF88A9",bg="#FFE2EA",
                  highlightthickness = 0, bd = 0)
    pw.place(relx = 0.435, rely = 0.61)
         
    sUp = tk.Button(signUpPage, image = signUpButt, bg="#FFFFFF", highlightthickness=0, bd=0)
    sUp.place(relx = 0.38, rely = 0.7)

def job_select():
    ss = tk.Toplevel(root)
    ss.geometry("1488x945")
    
    s = tk.Label(ss, image=start).pack()
    
    host = tk.Button(ss, 
                     image = start_host, 
                     bg="#FFE2EA", highlightthickness=0, bd=0, 
                     command = lambda: [host_hompage(), ss.withdraw()])
    host.place(relx = 0.329, rely = 0.3 )
    
    waiter = tk.Button(ss, 
                       image = start_waiter, 
                       bg="#FFE2EA", 
                       highlightthickness=0, bd=0, 
                       command = lambda: [waiter_hompage(), ss.withdraw()])
    waiter.place(relx = 0.329, rely = 0.6 )

def signInn():
    Start = tk.Toplevel(root)
    Start.geometry("1488x945")
    
    s = tk.Label(Start, image=s_l_page).pack()

    sign_in = tk.Label(Start, text="Sign In", font=('Didot', 48),fg="black",bg="white")
    sign_in.place(relx = 0.43, rely = 0.249)

    username = tk.Label(Start, text="Username:", font=('Didot', 32),fg="black",bg="white")
    username.place(relx = 0.365, rely = 0.375)

    password = tk.Label(Start, text="Password:", font=('Didot', 32),fg="black",bg="white")
    password.place(relx = 0.365, rely = 0.6)

    name = tk.Entry(Start, 
                    width = 23, 
                    font=("Inria Sans", 25), 
                    fg="black",bg="white")
    name.place(relx = 0.368, rely = 0.43)

    pw = tk.Entry(Start, 
                  width = 23, 
                  font=("Inria Sans", 25), 
                  fg="black",bg="white")
    pw.place(relx = 0.368, rely = 0.65)
    
    signUpButton = Button(Start, 
                          text = "Sign Up", 
                          font=("Inter", 10, "underline"), 
                          bg="white", fg="black", 
                          borderwidth=0, highlightthickness=0, bd=0, 
                          command = lambda: [signUp(), Start.withdraw()])
    signUpButton.place(relx = 0.368, rely = 0.75)
    
    logIn = tk.Button(Start, 
                   image = signInButt, 
                   bg="white", 
                   highlightthickness=0, 
                   takefocus=0, bd=0, 
                   command = lambda: [job_select(), Start.withdraw()])
    logIn.place(relx = 0.38, rely = 0.8)

root = tk.Tk()
root.geometry("1488x945")
root.configure(bg ="magenta")

splashBG = tk.PhotoImage(file = "splash_screen.png")
splashLabel=tk.Label(root, image=splashBG).pack()

root.after(200, lambda:[signInn(), root.withdraw()])

# font=('Didot', 12)


'''APP BACKGROUNDS'''
#LOGIN/JOB SELECTOR
s_l_page = tk.PhotoImage(file = "signup_login.png")
start = tk.PhotoImage(file = "choose job.png")

#HOST/WAITER HOMEPAGE
host_homepage = tk.PhotoImage(file = "host_homepage.png")
waiter_homepage = tk.PhotoImage(file = "waiter_homepage.png")

#WAITER ORDER/MENU SCREENS
host_homepage = tk.PhotoImage(file = "host_homepage.png")
waiter_homepage = tk.PhotoImage(file = "waiter_homepage.png")

#WAITER: MENU
m_hub = tk.PhotoImage(file = "menu-hubScreen.png")
#WAITER: ORDERS
o_hub = tk.PhotoImage(file = "orders screen.png")
o_complete = tk.PhotoImage(file = "order confirmation screen.png")
#WAITER: ORDERS: TIPS
t_hub = tk.PhotoImage(file = "tips screen.png")


'''APP BUTTONS'''
backButt = tk.PhotoImage(file = "backButton.png")

start_host = tk.PhotoImage(file = "start_host.png")
start_waiter = tk.PhotoImage(file = "start_waiter.png")

signInButt = tk.PhotoImage(file = "sign in button.png")
signUpButt = tk.PhotoImage(file = "sign up button.png")

#HOMEPAGE BUTTONS
home_signOutButt = tk.PhotoImage(file = "home-signOutButt.png")
home_tableButt = tk.PhotoImage(file = "home-tableButt.png")
home_menuButt = tk.PhotoImage(file = "home-menuButt.png")
home_ordersButt = tk.PhotoImage(file = "home-ordersButt.png")

#TABLE BUTTONS

#MENU BUTTONS
m_appetizer = tk.PhotoImage(file = "menu-appetizer-button.png")
m_bev = tk.PhotoImage(file = "menu-beverage-button.png")
m_courses = tk.PhotoImage(file = "menu-course-button.png")
m_sides = tk.PhotoImage(file = "menu-side-button.png")
#ORDER BUTTONS
o_credit = tk.PhotoImage(file = "orders-creditDebit.png")
o_cash = tk.PhotoImage(file = "orders-cash.png")
o_hold = tk.PhotoImage(file = "orders-hold.png")
o_next = tk.PhotoImage(file = "orders-orderNext.png")
o_prev = tk.PhotoImage(file = "orders-orderPrev.png")
#TIPS BUTTONS
t_15 = tk.PhotoImage(file = "tips-15Tip.png")
t_20 = tk.PhotoImage(file = "tips-20Tip.png")
t_25 = tk.PhotoImage(file = "tips-25Tip.png")
t_custom = tk.PhotoImage(file = "tips-customTip.png")
t_none = tk.PhotoImage(file = "tips-noTip.png")
tc_back = tk.PhotoImage(file = "tipscustom-backButt.png")
tc_next = tk.PhotoImage(file = "tipscustom-nextButt.png")


root.mainloop()