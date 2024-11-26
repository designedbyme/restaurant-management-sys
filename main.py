import time
import csv
import os
import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd 


def homepage():
    home = tk.Toplevel(root)
    home.geometry("1488x945")
    
    s = tk.Label(home, image=homeless_page).pack()
    
    atwork = tk.Label(home, text=f"Welcome, EASYUSER", font=("Inter", 20, "bold"), bg="#FFFFFF")
    atwork.place(relx = 0.38, rely = 0.7)
    
    atwork = tk.Label(home, text="At Work:", font=("Inter", 20, "bold"), bg="#FFFFFF")
    atwork.place(relx = 0.38, rely = 0.7)
    
    changers = tk.Button(home, image=settingBUTON, bg="#FFFFFF", highlightthickness = 0, bd = 0, command=home.destroy)
    changers.place(relx=0.05, rely=0.1, anchor= 'center')
    
    start_ur_job = tk.Button(home, image=watch_jjk, bg="#FFFFFF", highlightthickness = 0, bd = 0, command=home.destroy)
    start_ur_job.place(relx=0.05, rely=0.05, anchor= 'center')
    
    atwork = tk.Label()
    atwork.place(relx = 0.38, rely = 0.7)
    
    atwork = tk.Label()
    atwork.place(relx = 0.38, rely = 0.7)
    
    atwork = tk.Label()
    atwork.place(relx = 0.38, rely = 0.7)
    
    
    
def signUp():
    signUpPage = tk.Toplevel(root)
    signUpPage.geometry("1488x945")
    
    s = tk.Label(signUpPage, image=logIn).pack()
    
    back_button = tk.Button(signUpPage, image=backButt, bg="#FFE2EA", highlightthickness = 0, bd = 0, command=signUpPage.destroy)
    back_button.place(relx=0.05, rely=0.05, anchor= 'center')
    
    name = tk.Entry(signUpPage, width = 17, font=("Inria Sans", 25))
    name.place(relx = 0.37, rely = 0.4)
    
    email = tk.Entry(signUpPage, width = 17, font=("Inria Sans", 25))
    email.place(relx = 0.37, rely = 0.5)
    
    pw = tk.Entry(signUpPage, width = 17, font=("Inria Sans", 25))
    pw.place(relx = 0.37, rely = 0.6)
         
    sUp = tk.Button(signUpPage, image = signUpButt, bg="#FFFFFF", highlightthickness=0, bd=0)
    sUp.place(relx = 0.38, rely = 0.7)

def signInn():
    Start = tk.Toplevel(root)
    Start.geometry("1488x945")
    
    s = tk.Label(Start, image=signIn).pack()
    
    name = tk.Entry(Start, width = 17, font=("Inria Sans", 25))
    name.place(relx = 0.37, rely = 0.45)
    pw = tk.Entry(Start, width = 17, font=("Inria Sans", 25))
    pw.place(relx = 0.37, rely = 0.64)
    
    signUpButton = tk.Button(Start, text = "Sign Up", font=("Inter", 10, "underline"), bg="#FFFFFF", fg="#000000", highlightthickness=0, bd=0, command = signUp)
    signUpButton.place(relx = 0.37, rely = 0.7 )
    
    logIn = tk.Button(Start, image = signInButt, bg="#FFFFFF", highlightthickness=0, bd=0, command = homepage)
    logIn.place(relx = 0.38, rely = 0.75)

def before_login():
    ss = tk.Toplevel(root)
    ss.geometry("1488x945")
    
    s = tk.Label(ss, image=start).pack()
    
    boss = tk.Button(ss, image = start_boss, bg="#FFE2EA", highlightthickness=0, bd=0, command = signInn)
    boss.place(relx = 0.3, rely = 0.3 )
    
    host = tk.Button(ss, image = start_host, bg="#FFE2EA", highlightthickness=0, bd=0, command = signInn)
    host.place(relx = 0.3, rely = 0.5 )
    
    waiter = tk.Button(ss, image = start_waiter, bg="#FFE2EA", highlightthickness=0, bd=0, command = signInn)
    waiter.place(relx = 0.3, rely = 0.7 )
    
    
root = tk.Tk()
root.geometry("1488x945")
root.configure(bg ="magenta")

splashBG = tk.PhotoImage(file = "splash_screen.png")


splashLabel=tk.Label(root, image=splashBG).pack()

root.after(1000, before_login)



# app images
start_boss = tk.PhotoImage(file = "start_boss.png")
start_host = tk.PhotoImage(file = "start_host.png")
start_waiter = tk.PhotoImage(file = "start_waiter.png")

watch_jjk = tk.PhotoImage(file = "start job button.png")
settingBUTON = tk.PhotoImage(file = "settings.png")

backButt = tk.PhotoImage(file = "backButton.png")
signInButt = tk.PhotoImage(file = "sign in button.png")
signUpButt = tk.PhotoImage(file = "sign up button.png")

start = tk.PhotoImage(file = "choose job.png")
signIn = tk.PhotoImage(file = "log In.png")
logIn = tk.PhotoImage(file = "sign up.png")
homeless_page = tk.PhotoImage(file = "homer_page.png")


# some buttons


root.mainloop()
