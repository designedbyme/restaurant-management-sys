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
                              highlightthickness=0, takefocus=0, bd=0, 
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
                         highlightthickness=0, takefocus=0, bd=0, 
                         command = lambda: [signInn(), waiter.withdraw()])
    orderButt.place(relx = 0.6, rely = 0.64)

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


    back_button = tk.Button(signUpPage, image=backButt, bg="#FFE2EA", highlightthickness = 0, bd = 0, command=signUpPage.destroy)
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
                     command = lambda: [host_hompage(), ss.destroy()])
    host.place(relx = 0.329, rely = 0.3 )
    
    waiter = tk.Button(ss, 
                       image = start_waiter, 
                       bg="#FFE2EA", 
                       highlightthickness=0, bd=0, 
                       command = lambda: [waiter_hompage(), ss.destroy()])
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


# app BACKGROUND
start_host = tk.PhotoImage(file = "start_host.png")
start_waiter = tk.PhotoImage(file = "start_waiter.png")

start = tk.PhotoImage(file = "choose job.png")
s_l_page = tk.PhotoImage(file = "signup_login.png")

host_homepage = tk.PhotoImage(file = "host_homepage.png")
waiter_homepage = tk.PhotoImage(file = "waiter_homepage.png")

# some buttons
backButt = tk.PhotoImage(file = "backButton.png")

signInButt = tk.PhotoImage(file = "sign in button.png")
signUpButt = tk.PhotoImage(file = "sign up button.png")

home_menuButt = tk.PhotoImage(file = "home-menuButt.png")
home_ordersButt = tk.PhotoImage(file = "home-ordersButt.png")
home_signOutButt = tk.PhotoImage(file = "home-signOutButt.png")
home_tableButt = tk.PhotoImage(file = "home-tableButt.png")



root.mainloop()
