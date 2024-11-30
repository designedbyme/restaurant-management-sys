import csv
import os
import tkinter as tk
#import tkmacosx as tmacc
from tkmacosx import Button
from PIL import Image, ImageTk

def waiter():
    waiter = tk.Toplevel(root)
    waiter.geometry("1488x945")

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
    
    host = tk.Button(ss, image = start_host, bg="#FFE2EA", highlightthickness=0, bd=0, command = lambda: [signInn(), ss.withdraw()])
    host.place(relx = 0.329, rely = 0.3 )
    
    waiter = tk.Button(ss, image = start_waiter, bg="#FFE2EA", highlightthickness=0, bd=0, command = lambda: [signInn(), ss.withdraw()])
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

# app images
start_host = tk.PhotoImage(file = "start_host.png")
start_waiter = tk.PhotoImage(file = "start_waiter.png")

start = tk.PhotoImage(file = "choose job.png")
s_l_page = tk.PhotoImage(file = "signup_login.png")


# some buttons
backButt = tk.PhotoImage(file = "backButton.png")
signInButt = tk.PhotoImage(file = "sign in button.png")
signUpButt = tk.PhotoImage(file = "sign up button.png")


root.mainloop()
