import csv
import os
import tkinter as tk
import tkinter.ttk as ttk
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
    header.place(relx = 0.1, rely = 0.22)

    subHeader = tk.Label(host, 
                      text="End Job",
                      font=("Inter", 30, "bold"), 
                      bg="white", fg="black")
    subHeader.place(relx = 0.225, rely = 0.39)

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

def tables():
    tables = tk.Toplevel(root)
    tables.geometry("1488x945")
    s = tk.Label(tables, image=host_homepage).pack()


def waiter_hompage():
    waiter = tk.Toplevel(root)
    waiter.geometry("1488x945")
    s = tk.Label(waiter, image=waiter_homepage).pack()

    header = tk.Label(waiter, 
                      text=f"Welcome, EASYUSER",
                      font=("Inter", 30, "bold"), 
                      bg="white", fg="black")
    header.place(relx = 0.1, rely = 0.22)

    subHeader = tk.Label(waiter, 
                      text="End Job",
                      font=("Inter", 30, "bold"), 
                      bg="white", fg="black")
    subHeader.place(relx = 0.225, rely = 0.39)

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
                         command = lambda: [menuHub(), waiter.withdraw()])
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

    back_button = tk.Button(menu, 
                            image=backButt, 
                            bg="#CC5576", 
                            highlightthickness = 0, bd = 0, 
                            command= lambda: [waiter_hompage(), menu.withdraw()])
    back_button.place(relx=0.06, rely=0.07, anchor= 'center')
    header = tk.Label(menu, 
                      text="MENU",
                      font=('American Typewriter', 55),
                      bg="#CC5576", fg="black")
    header.place(relx = 0.42, rely = 0.04)

    beverages = tk.Button(menu, 
                          image = m_bev, 
                          bg="#FFE2EA", 
                          highlightthickness=0, takefocus=0, bd=0, 
                          command = lambda: [menus("BEVERAGES"), menu.withdraw()])
    beverages.place(relx = 0.08, rely = 0.25)

    appetizers = tk.Button(menu, 
                           image = m_appetizer, 
                           bg="#FFE2EA", 
                           highlightthickness=0, takefocus=0, bd=0, 
                           command = lambda: [menus("APPETIZERS"), menu.withdraw()])
    appetizers.place(relx = 0.6, rely = 0.25)

    mainCourses = tk.Button(menu, 
                            image = m_courses, 
                            bg="#FFE2EA", 
                            highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [menus("MAIN COURSES"), menu.withdraw()])
    mainCourses.place(relx = 0.33, rely = 0.475)

    sides = tk.Button(menu, 
                      image = m_sides, 
                      bg="#FFE2EA", 
                      highlightthickness=0, takefocus=0, bd=0, 
                      command = lambda: [menus("SIDES"), menu.withdraw()])
    sides.place(relx = 0.08, rely = 0.75)

    desserts = tk.Button(menu, 
                         image = m_dessert, 
                         bg="#FFE2EA", 
                         highlightthickness=0, takefocus=0, bd=0, 
                         command = lambda: [menus("DESSERTS"), menu.withdraw()])
    desserts.place(relx = 0.6, rely = 0.75)

def menus(typo):
    menu = tk.Toplevel(root)
    menu.geometry("1488x945")
    s = tk.Label(menu, image=m_hub).pack()

    back_button = tk.Button(menu, 
                            image=backButt, 
                            bg="#CC5576", 
                            highlightthickness = 0, bd = 0, 
                            command= lambda: [menuHub(), menu.withdraw()])
    back_button.place(relx=0.06, rely=0.07, anchor= 'center')
    header = tk.Label(menu, 
                      text=typo,
                      font=('American Typewriter', 55),
                      bg="#CC5576", fg="black")
    header.place(relx = 0.35, rely = 0.04)

    #test=tk.Label(menu, 
    #                  text="tet",
     #                 font=('American Typewriter', 55),
      #                bg="white", fg="black")
   # test.place(relx = 0, rely = 0.14)

    foodFrame = tk.Frame(menu,  
                         bg ="#FFE2EA",
                         height=802, width=1488)
    foodFrame.place(relx = 0, rely = 0.14)
    
    if typo == "BEVERAGES":
        coke = tk.Button(foodFrame, 
                          image = d_coke, 
                          bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                          command = lambda: [menuHub(), menu.withdraw()])
        coke.place(relx = 0.05, rely = 0.05)

        mangoSmoothie = tk.Button(foodFrame, 
                                  image = d_mango, 
                                  bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                                  command = lambda: [menuHub(), menu.withdraw()])
        mangoSmoothie.place(relx = 0.225, rely = 0.05)

        water = tk.Button(foodFrame, 
                          image = d_water, 
                          bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                          command = lambda: [menuHub(), menu.withdraw()])
        water.place(relx = 0.4, rely = 0.05)

        incaCola = tk.Button(foodFrame, 
                             image = d_inca, 
                             bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                             command = lambda: [menuHub(), menu.withdraw()])
        incaCola.place(relx = 0.55, rely = 0.05)

        morocho = tk.Button(foodFrame, 
                            image = d_morocho, 
                            bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [menuHub(), menu.withdraw()])
        morocho.place(relx = 0.75, rely = 0.05)
        
        sprite = tk.Button(foodFrame, 
                           image = d_sprite, 
                           bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                           command = lambda: [menuHub(), menu.withdraw()])
        sprite.place(relx = 0.075, rely = 0.5)

        strawberrySmoothie = tk.Button(foodFrame, 
                                        image = d_strawberry, 
                                        bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                                        command = lambda: [menuHub(), menu.withdraw()])
        strawberrySmoothie.place(relx = 0.22, rely = 0.5)

        fanta = tk.Button(foodFrame, 
                            image = d_fanta, 
                            bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [menuHub(), menu.withdraw()])
        fanta.place(relx = 0.4, rely = 0.5)

        chicha = tk.Button(foodFrame, 
                            image = d_chicha, 
                            bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [menuHub(), menu.withdraw()])
        chicha.place(relx = 0.575, rely = 0.5)

        icedTea = tk.Button(foodFrame, 
                            image = d_tea, 
                            bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [menuHub(), menu.withdraw()])
        icedTea.place(relx = 0.75, rely = 0.5)
    elif typo == "APPETIZERS":
        coke = tk.Button(foodFrame, 
                          image = d_coke, 
                          bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                          command = lambda: [menuHub(), menu.withdraw()])
        coke.place(relx = 0.05, rely = 0.05)

        mangoSmoothie = tk.Button(foodFrame, 
                                  image = d_mango, 
                                  bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                                  command = lambda: [menuHub(), menu.withdraw()])
        mangoSmoothie.place(relx = 0.225, rely = 0.05)

        water = tk.Button(foodFrame, 
                          image = d_water, 
                          bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                          command = lambda: [menuHub(), menu.withdraw()])
        water.place(relx = 0.4, rely = 0.05)

        incaCola = tk.Button(foodFrame, 
                             image = d_inca, 
                             bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                             command = lambda: [menuHub(), menu.withdraw()])
        incaCola.place(relx = 0.55, rely = 0.05)

        morocho = tk.Button(foodFrame, 
                            image = d_morocho, 
                            bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [menuHub(), menu.withdraw()])
        morocho.place(relx = 0.75, rely = 0.05)
        
        sprite = tk.Button(foodFrame, 
                           image = d_sprite, 
                           bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                           command = lambda: [menuHub(), menu.withdraw()])
        sprite.place(relx = 0.075, rely = 0.5)

        strawberrySmoothie = tk.Button(foodFrame, 
                                        image = d_strawberry, 
                                        bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                                        command = lambda: [menuHub(), menu.withdraw()])
        strawberrySmoothie.place(relx = 0.22, rely = 0.5)

        fanta = tk.Button(foodFrame, 
                            image = d_fanta, 
                            bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [menuHub(), menu.withdraw()])
        fanta.place(relx = 0.4, rely = 0.5)




    '''   
    elif typo == "MAIN COURSES":
    elif typo == "SIDES":
    elif typo == "DESSERTS":
    else:
        pass
'''


def orderHub():
    order = tk.Toplevel(root)
    order.geometry("1488x945")    
    s = tk.Label(order, image=o_hub).pack()

    back_button = tk.Button(order, 
                            image=backButt, 
                            bg="#FF88A9", 
                            highlightthickness = 0, bd = 0, 
                            command= lambda: [waiter_hompage(), order.withdraw()])
    back_button.place(relx=0.04, rely=0.06, anchor= 'center')
    header = tk.Label(order, 
                      text=f"Table X's Order:",
                      font=("Inter", 40, "bold"), 
                      bg="#FF88A9", fg="white")
    header.place(relx = 0.07, rely = 0.03)

    bck = tk.Button(order, 
                    image=o_prev,
                    bg="#FF88A9", 
                    highlightthickness=0, 
                    takefocus=0, bd=0, 
                    command = lambda: [job_select(), order.withdraw()])
    bck.place(relx = 0.36, rely = 0.09)
    nxt = tk.Button(order, 
                    image=o_next ,
                    bg="#FF88A9", 
                    highlightthickness=0, 
                    takefocus=0, bd=0,
                    command = lambda: [job_select(), order.withdraw()])
    nxt.place(relx = 0.41, rely = 0.09)


    canvas = tk.Canvas(order, 
                       bg="#FF88A9",
                       width=663, height=708,
                       highlightthickness=0,
                       scrollregion=(0,0,900,900))
    canvas.place(relx = 0.008, rely = 0.145)
    
    vbar=ttk.Scrollbar(order, orient="vertical", command=canvas.yview)
    vbar.place(relx = 0.463, rely = 0.145, relheight=0.789)

    canvas.configure(yscrollcommand=vbar.set)

    canvas.create_text(50, 50, 
                       text="ITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\n", 
                       font=("Inter", 30), 
                       anchor='nw', 
                       fill="white")


    total = tk.Label(order, 
                      text=f"Total: $0.00",
                      font=("Inter", 40, "bold"), 
                      bg="#FF88A9", fg="white")
    total.place(relx = 0.68, rely = 0.12)

    credit = tk.Button(order, 
                       image=o_credit,
                       bg="#FF88A9", 
                       highlightthickness=0, takefocus=0, bd=0, 
                       command = lambda: [tips(), order.withdraw()])
    credit.place(relx = 0.63, rely = 0.22)

    cash = tk.Button(order, 
                     image=o_cash,
                     bg="#FF88A9", 
                     highlightthickness=0, takefocus=0, bd=0, 
                     command = lambda: [tips(), order.withdraw()])
    cash.place(relx = 0.63, rely = 0.42)

    hold = tk.Button(order, 
                     image=o_hold,
                     bg="#FF88A9", 
                     highlightthickness=0, takefocus=0, bd=0, 
                     command = lambda: [tips(), order.withdraw()])
    hold.place(relx = 0.63, rely = 0.62)

def tips():
    tips = tk.Toplevel(root)
    tips.geometry("1488x945")
    s = tk.Label(tips, image=t_hub).pack()

    back_button = tk.Button(tips, 
                            image=backButt, 
                            bg="#FEB5C9", 
                            highlightthickness = 0, bd = 0, 
                            command= lambda: [orderHub(), tips.withdraw()])
    back_button.place(relx=0.04, rely=0.06, anchor= 'center')

    tt_15 = tk.Button(tips, 
                      image = t_15, 
                      bg="white", 
                      highlightthickness=0, takefocus=0, bd=0, 
                      command = lambda: [purchaseComplete(), tips.withdraw()])
    tt_15.place(relx = 0.2, rely = 0.3)
    tt_20 = tk.Button(tips, 
                      image = t_20, 
                      bg="white", 
                      highlightthickness=0, takefocus=0, bd=0, 
                      command = lambda: [purchaseComplete(), tips.withdraw()])
    tt_20.place(relx = 0.4, rely = 0.3)
    tt_25 = tk.Button(tips, 
                      image = t_25, 
                      bg="white", 
                      highlightthickness=0, takefocus=0, bd=0, 
                      command = lambda: [purchaseComplete(), tips.withdraw()])
    tt_25.place(relx = 0.6, rely = 0.3)

    customTip = tk.Button(tips, 
                          image = t_custom, 
                          bg="white", 
                          highlightthickness=0, takefocus=0, bd=0, 
                          command = lambda: [customTips(), tips.withdraw()])
    customTip.place(relx = 0.1875, rely = 0.6)

    noTip = tk.Button(tips, 
                      image = t_none, 
                      bg="white", 
                      highlightthickness=0, takefocus=0, bd=0, 
                      command = lambda: [purchaseComplete(), tips.withdraw()])
    noTip.place(relx = 0.1875, rely = 0.775)
    
def customTips():
    tips = tk.Toplevel(root)
    tips.geometry("1488x945")
    s = tk.Label(tips, image=t_hub).pack()

    header = tk.Label(tips, 
                      text="Enter Amount:",
                      font=('Bangla MN', 40), 
                      bg="white", fg="#FF88A9")
    header.place(relx = 0.2, rely = 0.3)

    frame = tk.Frame(tips,  
                     bg ="white",
                     highlightbackground="#FF88A9", highlightthickness=2)
    frame.place(relx = 0.201, rely = 0.4)
    amtEntry = tk.Entry(frame, 
                        width=27,
                        font=("Inria Sans", 50),
                        fg="#FF88A9",bg="white",
                        highlightthickness = 0, bd = 0)
    amtEntry.pack()

    back = tk.Button(tips, 
                     image = tc_back, 
                     bg="white", 
                     highlightthickness=0, takefocus=0, bd=0, 
                     command = lambda: [orderHub(), tips.withdraw()])
    back.place(relx = 0.4, rely = 0.7)

    nexx = tk.Button(tips, 
                     image = tc_next, 
                     bg="white", 
                     highlightthickness=0, takefocus=0, bd=0, 
                     command = lambda:[purchaseComplete(), tips.withdraw()])
    nexx.place(relx = 0.4, rely = 0.85)

def purchaseComplete():
    tips = tk.Toplevel(root)
    tips.geometry("1488x945")
    ss = tk.Label(tips, image=o_complete).pack()
    
    tips.after(500, lambda:[orderHub(), tips.withdraw()])


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
m_bev = tk.PhotoImage(file = "menu-beverage-button.png")
m_appetizer = tk.PhotoImage(file = "menu-appetizer-button.png")
m_courses = tk.PhotoImage(file = "menu-course-button.png")
m_sides = tk.PhotoImage(file = "menu-side-button.png")
m_dessert = tk.PhotoImage(file = "menu-desert-button.png")
#MENU: DRINKS
d_coke = tk.PhotoImage(file = "drinks-coke.png")
d_mango = tk.PhotoImage(file = "drinks-mango mango.png")
d_water = tk.PhotoImage(file = "drinks-water.png")
d_inca = tk.PhotoImage(file = "drinks-inca cola.png")
d_morocho = tk.PhotoImage(file = "drinks-morocho.png")
d_sprite = tk.PhotoImage(file = "drinks-sprite.png")
d_strawberry = tk.PhotoImage(file = "drinks-strawberyy.png")
d_fanta = tk.PhotoImage(file = "drinks-fanta.png")
d_chicha = tk.PhotoImage(file = "drinks-chichi.png")
d_tea = tk.PhotoImage(file = "drinks-iced tea.png")

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