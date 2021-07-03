#Manjinder Sandhu

import sqlite3
import tkinter
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
import re 
import os
from selenium import webdriver
import webbrowser
import time

def bot():
    browser = webdriver.Chrome('/Users/manjinder/ShoppingBot/chromedriver')

def exitInterface():
    exit()


def aboutInterface():
    tkinter.messagebox.showinfo("Shopping Bot -Manjinder Sandhu", "This shopping bot can place orders for any product on any website!")


def helpInterface():
    tkinter.messagebox.showinfo("Shopping Bot -Manjinder Sandhu", "If you need help, Please Click on the 'Help' Button")


def secondInterface():
    root = tkinter.Tk()
    root.title("Shopping Bot- Manjinder Sandhu")
    text = tkinter.Text()

    FetchInfo = tkinter.StringVar()
    FetchInfo2 = tkinter.StringVar()
    FetchInfo3 = tkinter.StringVar()
    FetchInfo4 = tkinter.StringVar()

    db = sqlite3.connect('AccountInformation.db')
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS account(first_name text, last_name text, email text, password text)")
    db.commit()


    def validateInformation():
        if entry_1.get() == "":
            tkinter.messagebox.showinfo("Shopping Bot -Manjinder Sandhu", "Please enter your Password!")
        elif entry_2.get() == "":
            tkinter.messagebox.showinfo("Shopping Bot -Manjinder Sandhu", "Please enter your Last Name!")
        elif entry_3.get() == "":
            tkinter.messagebox.showinfo("Shopping Bot -Manjinder Sandhu", "Please enter your First Name!")
        elif entry_4.get() == "":
            tkinter.messagebox.showinfo("Shopping Bot -Manjinder Sandhu", "Please enter your Email!")
        else:
            insert()


    def insert():
        e_1 = entry_1.get()
        e_2 = entry_2.get()
        e_3 = entry_3.get()
        e_4 = entry_4.get()
        conn = sqlite3.connect("AccountInformation.db")
        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO account (password, last_name, first_name, email) VALUES(?,?,?,?)",(e_1, e_2, e_3, e_4))
            tkinter.messagebox.showinfo("Shopping Bot -Manjinder Sandhu", "Account Created Sucessfully!")
            db.close()
    

    def show():
        #Website to view SQLite FIle
        #http://inloop.github.io/sqlite-viewer/
        connt = sqlite3.connect('AccountInformation.db')
        cursor = connt.cursor()
        cursor.execute("SELECT * FROM account")
        for row in cursor.fetchall():
            print(row)


    canvas = tkinter.Canvas(root, width=900, height = 500)
    canvas.grid(columnspan = 5, rowspan = 5)
    root.resizable(True, True) #Width, #Height
    
    Instruction = tkinter.Label (root, text = "Create your account!", relief = "solid", font ="Georgia 32 bold").place(x=300, y= 50)
    Instruction1 = tkinter.Label (root, text = "By Signing up you agree to the terms of services and privacy policy", relief = "solid", font ="Times 12").place(x=120, y= 450)

    menu = Menu(root)
    root.config(menu = menu)

    submenu = Menu(menu)
    menu.add_cascade(label = "File",menu = submenu)
    submenu.add_command(label = "Exit", command = exitInterface)

    submenu2 = Menu(menu)
    menu.add_cascade(label = "Option",menu = submenu2)
    submenu2.add_command(label = "About", command = aboutInterface)

    submenu3 = Menu(menu)
    menu.add_cascade(label = "Help",menu = submenu3)
    submenu3.add_command(label = "Help", command = helpInterface)

    browse_text_secondInterface = tkinter.StringVar(root)
    browse_button_secondInterface = tkinter.Button(root, textvariable = browse_text_secondInterface, font = "Georgia", bd=1, bg = "#D4D0C8", fg = "Black", height = 2, width = 15, command = validateInformation )
    browse_text_secondInterface.set("Sign Up")
    browse_button_secondInterface.place(x=435, y= 350)

    browse_text_secondInterface2 = tkinter.StringVar(root)
    browse_button_secondInterface2 = tkinter.Button(root, textvariable = browse_text_secondInterface2, font = "Georgia", bd=1, bg = "#D4D0C8", fg = "Black", height = 2, width = 18, command = thirdInterface)
    browse_text_secondInterface2.set("Terms of Services")
    browse_button_secondInterface2.place(x=233, y= 351)

    label_firstName = Label(root, text= "First Name: ", width = 20, font=("Times 16 bold"))
    label_firstName.place(x=80, y=130)

    entry_1 = Entry(root, textvar = FetchInfo, bd = 1)
    entry_1.place(x=250, y=280)

    label_lastName = Label(root, text= "Last Name: ", width = 20, font=("Times 16 bold"))
    label_lastName.place(x=78, y=180)

    entry_2 = Entry(root, textvar = FetchInfo2, bd = 1)
    entry_2.place(x=250, y=180)

    label_email = Label(root, text= "Email: ", width = 20, font=("Times 16 bold"))
    label_email.place(x=61, y=230)

    entry_3 = Entry(root, textvar = FetchInfo3, bd = 1)
    entry_3.place(x=250, y=130)

    label_password = Label(root, text= "Password: ", width = 20, font=("Times 16 bold"))
    label_password.place(x=73, y=280)

    entry_4 = Entry(root, textvar = FetchInfo4, bd = 1)
    entry_4.place(x=250, y=230)
    

def thirdInterface():
    root = tkinter.Tk()
    text = tkinter.Text()
    root.title("Shopping Bot- Manjinder Sandhu")
    canvas = tkinter.Canvas(root, width=900, height = 500)
    canvas.grid(columnspan = 5, rowspan = 5)

    # Resize the Interface
    root.resizable(True, True) #Width, #Height
    menu = Menu(root)
    root.config(menu = menu)

    submenu = Menu(menu)
    menu.add_cascade(label = "File",menu = submenu)
    submenu.add_command(label = "Exit", command = exitInterface)

    submenu2 = Menu(menu)
    menu.add_cascade(label = "Option",menu = submenu2)
    submenu2.add_command(label = "About", command = aboutInterface)

    submenu3 = Menu(menu)
    menu.add_cascade(label = "Help",menu = submenu3)
    submenu3.add_command(label = "Help", command = helpInterface)

    Instruction = tkinter.Label (root, text = "Terms and Conditions!", relief = "solid", font ="Georgia 32 bold").place(x=300, y= 50)
    Instruction1 = tkinter.Label (root, text = "We are not responsible for anything that program may do. Please use this program at your own caution. Thank You", font ="Times 12").place(x=230, y= 125)


def fourthInterface():
    root = tkinter.Tk()
    text = tkinter.Text()
    root.title("Shopping Bot- Manjinder Sandhu")
    canvas = tkinter.Canvas(root, width=900, height = 500)
    canvas.grid(columnspan = 5, rowspan = 5)

    FetchInfo = StringVar()
    FetchInfo2 = StringVar()

    db = sqlite3.connect('AccountInformation.db')
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS account(first_name text, last_name text, email text, password text)")
    db.commit()

    def checker():
        e_3 = entry_3.get()
        e_4 = entry_4.get()
        db = sqlite3.connect('AccountInformation.db')
        cursor = db.cursor()
        finduser = ("SELECT * FROM account WHERE email = ?")
        findpassword = ("SELECT * FROM account WHERE password = ?")
        cursor.execute(finduser,[(e_3)])
        cursor.execute(findpassword,[(e_4)])
        if cursor.fetchall():
            tkinter.messagebox.showinfo("Shopping Bot -Manjinder Sandhu", "Signing In!")
            sixthInterface()
        else:
            tkinter.messagebox.showinfo("Shopping Bot -Manjinder Sandhu", "Incorrect Email or Password!")
            

    # Resize the Interface
    root.resizable(True, True) #Width, #Height
    menu = Menu(root)
    root.config(menu = menu)

    submenu = Menu(menu)
    menu.add_cascade(label = "File",menu = submenu)
    submenu.add_command(label = "Exit", command = exitInterface)

    submenu2 = Menu(menu)
    menu.add_cascade(label = "Option",menu = submenu2)
    submenu2.add_command(label = "About", command = aboutInterface)

    submenu3 = Menu(menu)
    menu.add_cascade(label = "Help",menu = submenu3)
    submenu3.add_command(label = "Help", command = helpInterface)

    Instruction = tkinter.Label (root, text = "Signing in!", relief = "solid", font ="Georgia 32 bold").place(x=300, y= 50)

    label_email = Label(root, text= "Email: ", width = 20, font=("Times 16 bold"))
    label_email.place(x=135, y=145)

    entry_3 = Entry(root, textvar = FetchInfo, bd = 1)
    entry_3.place(x=250, y=145)

    label_password = Label(root, text= "Password: ", width = 20, font=("Times 16 bold"))
    label_password.place(x=120, y=230)

    entry_4 = Entry(root, textvar = FetchInfo2, bd = 1)
    entry_4.place(x=250, y=230)

    browse_text_secondInterface = tkinter.StringVar(root)
    browse_button_secondInterface = tkinter.Button(root, textvariable = browse_text_secondInterface, font = "Georgia", bd=1, bg = "#D4D0C8", fg = "Black", height = 2, width = 15, command = checker)
    browse_text_secondInterface.set("Sign In")
    browse_button_secondInterface.place(x=435, y= 350)

    browse_text_secondInterface2 = tkinter.StringVar(root)
    browse_button_secondInterface2 = tkinter.Button(root, textvariable = browse_text_secondInterface2, font = "Georgia", bd=1, bg = "#D4D0C8", fg = "Black", height = 2, width = 18, command = thirdInterface)
    browse_text_secondInterface2.set("Terms of Services")
    browse_button_secondInterface2.place(x=233, y= 351)

    Instruction1 = tkinter.Label (root, text = "By Signing In you agree to the terms of services and privacy policy", relief = "solid", font ="Times 12").place(x=120, y= 450)


def fifthInterface():
    root = tkinter.Tk()
    text = tkinter.Text()
    root.title("Shopping Bot- Manjinder Sandhu")
    canvas = tkinter.Canvas(root, width=900, height = 500)
    canvas.grid(columnspan = 5, rowspan = 5)

    FetchInfo = StringVar()
    FetchInfo2 = StringVar()
    FetchInfo3 = StringVar()
    FetchInfo4 = StringVar()

    db = sqlite3.connect('HelpTicket.db')
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS helpInfo(first_name text, last_name text, email text, problem text)")
    db.commit()


    def validateInformation2():
        if entry_1.get() == "":
            tkinter.messagebox.showinfo("Shopping Bot -Manjinder Sandhu", "Please enter your First Name!")
        elif entry_2.get() == "":
            tkinter.messagebox.showinfo("Shopping Bot -Manjinder Sandhu", "Please enter your Last Name!")
        elif entry_3.get() == "":
            tkinter.messagebox.showinfo("Shopping Bot -Manjinder Sandhu", "Please enter your Email!")
        elif entry_4.get() == "":
            tkinter.messagebox.showinfo("Shopping Bot -Manjinder Sandhu", "Please enter your Problem!")
        else:
            insert2()


    def insert2():
        e_1 = entry_1.get()
        e_2 = entry_2.get()
        e_3 = entry_3.get()
        e_4 = entry_4.get()
        conn = sqlite3.connect("HelpTicket.db")
        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO helpInfo (email, last_name, first_name, problem) VALUES(?,?,?,?)",(e_1, e_2, e_3, e_4))
            tkinter.messagebox.showinfo("Shopping Bot -Manjinder Sandhu", "Thank You!, we will reach out to you concerning this problem")
            db.close()
    

    def show2():
        #Website to view SQLite FIle
        #http://inloop.github.io/sqlite-viewer/
        connt = sqlite3.connect('HelpTicket.db')
        cursor = connt.cursor()
        cursor.execute("SELECT * FROM help")
        for row in cursor.fetchall():
            print(row)


    # Resize the Interface
    root.resizable(True, True) #Width, #Height
    menu = Menu(root)
    root.config(menu = menu)

    Instruction1 = tkinter.Label (root, text = "Please enter fill out the information below. This will create a ticket for the help desk. Thank You", font ="Times 17 bold").place(x=130, y= 95)

    submenu = Menu(menu)
    menu.add_cascade(label = "File",menu = submenu)
    submenu.add_command(label = "Exit", command = exitInterface)

    submenu2 = Menu(menu)
    menu.add_cascade(label = "Option",menu = submenu2)
    submenu2.add_command(label = "About", command = aboutInterface)

    submenu3 = Menu(menu)
    menu.add_cascade(label = "Help",menu = submenu3)
    submenu3.add_command(label = "Help", command = helpInterface)
    Instruction = tkinter.Label (root, text = "Help!", relief = "solid", font ="Georgia 32 bold").place(x=435, y= 40)

    label_firstName = Label(root, text= "First Name: ", width = 20, font=("Times 16 bold"))
    label_firstName.place(x=80, y=180)

    entry_1 = Entry(root, textvar = FetchInfo, bd = 1)
    entry_1.place(x=250, y=180)

    label_lastName = Label(root, text= "Last Name: ", width = 20, font=("Times 16 bold"))
    label_lastName.place(x=80, y=230)

    entry_2 = Entry(root, textvar = FetchInfo2, bd = 1)
    entry_2.place(x=250, y=230)

    label_email = Label(root, text= "Email: ", width = 20, font=("Times 16 bold"))
    label_email.place(x=80, y=270)

    entry_3 = Entry(root, textvar = FetchInfo3, bd = 1)
    entry_3.place(x=250, y=270)

    label_problem = Label(root, text= "Problem: ", width = 20, font=("Times 16 bold"))
    label_problem.place(x=80, y=310)

    entry_4 = Entry(root, textvar = FetchInfo4, bd = 1)
    entry_4.place(x=250, y=310)

    browse_text_fifthInterface = tkinter.StringVar(root)
    browse_button_fifthInterface = tkinter.Button(root, textvariable = browse_text_fifthInterface, font = "Georgia", bd=1, bg = "#D4D0C8", fg = "Black", height = 2, width = 15, command = validateInformation2)
    browse_text_fifthInterface.set("Submit")
    browse_button_fifthInterface.place(x=435, y= 400)


def sixthInterface():
    root = tkinter.Tk()
    text = tkinter.Text()
    root.title("Shopping Bot- Manjinder Sandhu")

    FetchInfo = tkinter.StringVar()
    FetchInfo2 = tkinter.StringVar()
    FetchInfo3 = tkinter.StringVar()
    FetchInfo4 = tkinter.StringVar()

    db = sqlite3.connect('PurchaseRecord.db')
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS account(product_Name text, purchase_Date text, card_Name text, card_Number text)")
    db.commit()


    def validateInformation3():
        if entry_1.get() == "":
            tkinter.messagebox.showinfo("Shopping Bot -Manjinder Sandhu", "Please enter your Product Name!")
        elif entry_2.get() == "":
            tkinter.messagebox.showinfo("Shopping Bot -Manjinder Sandhu", "Please enter your Purchase Date!")
        elif entry_3.get() == "":
            tkinter.messagebox.showinfo("Shopping Bot -Manjinder Sandhu", "Please enter the Card Name!")
        elif entry_4.get() == "":
            tkinter.messagebox.showinfo("Shopping Bot -Manjinder Sandhu", "Please enter your Card Number!")
        else:
            insert3()


    def insert3():
        e_1 = entry_1.get()
        e_2 = entry_2.get()
        e_3 = entry_3.get()
        e_4 = entry_4.get()
        conn = sqlite3.connect("PurchaseRecord.db")
        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO account (card_Number, purchase_Date, product_name, card_Name) VALUES(?,?,?,?)",(e_1, e_2, e_3, e_4))
            tkinter.messagebox.showinfo("Shopping Bot -Manjinder Sandhu", "Recorded Sucessfully!")
            db.close()
    

    def show3():
        #Website to view SQLite FIle
        #http://inloop.github.io/sqlite-viewer/
        connt = sqlite3.connect('PurchaseRecord.db')
        cursor = connt.cursor()
        cursor.execute("SELECT *, oid FROM account")
        displayRecords = cursor.fetchall()
        print_records = ""
        for displayRecords in displayRecords:
            print_records += str(displayRecords) + "\n"

        label_record = Label(root, text= print_records  , width = 55, font=("Times 20"))
        label_record.place(x=5, y=450)
        

    def Amazon():
        url = "https://www.amazon.com"
        webbrowser.open_new(url)
    

    def Walmart():
        url = "https://www.walmart.com"
        webbrowser.open_new(url)
    

    def GameStop():
        url = "https://www.gamestop.com"
        webbrowser.open_new(url)
    

    def BestBuy():
        url = "https://www.bestbuy.com"
        webbrowser.open_new(url)
    

    def BestBuyBot():
        browser_Chrome = webdriver.Chrome('/Users/manjinder/ShoppingBot/chromedriver')
        browser_Chrome.get("https://www.bestbuy.com/site/clx-set-gaming-desktop-intel-core-i9-10900k-32gb-memory-nvidia-geforce-rtx-3070-960gb-ssd-4tb-hdd-black/6439575.p?skuId=6439575")
        buyButton = False
        while not buyButton:
            try:
                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-disabled")

                print("Button isnt ready")

                time.sleep(1)
                browser_Chrome.refresh()
            except:
                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-primary")

                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-secondary")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("cart-label")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-lg")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True
    

    def BestBuyBot2():
        browser_Chrome = webdriver.Chrome('/Users/manjinder/ShoppingBot/chromedriver')
        browser_Chrome.get("https://www.bestbuy.com/site/asus-rog-gaming-desktop-intel-core-i7-9700k-16gb-memory-nvidia-geforce-rtx-2080-super-2tb-hdd-512gb-ssd-black/6401068.p?skuId=6401068")
        buyButton = False
        while not buyButton:
            try:
                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-disabled")

                print("Button isnt ready")

                time.sleep(1)
                browser_Chrome.refresh()
            except:
                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-primary")

                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-secondary")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("cart-label")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-lg")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True
    

    def BestBuyBot3():
        browser_Chrome = webdriver.Chrome('/Users/manjinder/ShoppingBot/chromedriver')
        browser_Chrome.get("https://www.bestbuy.com/site/ibuypower-arc-gaming-desktop-intel-i3-9100f-8gb-memory-nvidia-geforce-gt-710-1gb-480gb-ssd/6451066.p?skuId=6451066")
        buyButton = False
        while not buyButton:
            try:
                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-disabled")

                print("Button isnt ready")

                time.sleep(1)
                browser_Chrome.refresh()
            except:
                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-primary")

                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-secondary")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("cart-label")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-lg")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True
    

    def BestBuyBot4():
        browser_Chrome = webdriver.Chrome('/Users/manjinder/ShoppingBot/chromedriver')
        browser_Chrome.get("https://www.bestbuy.com/site/hp-envy-desktop-intel-core-i7-16gb-memory-512gb-ssd-nightfall-black/6428087.p?skuId=6428087")
        buyButton = False
        while not buyButton:
            try:
                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-disabled")

                print("Button isnt ready")

                time.sleep(1)
                browser_Chrome.refresh()
            except:
                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-primary")

                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-secondary")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("cart-label")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-lg")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True
        

    def BestBuyBot5():
        browser_Chrome = webdriver.Chrome('/Users/manjinder/ShoppingBot/chromedriver')
        browser_Chrome.get("https://www.bestbuy.com/site/cyberpowerpc-gamer-master-gaming-desktop-amd-ryzen-5-3600-8gb-memory-amd-radeon-rx-580-500gb-ssd/6452139.p?skuId=6452139")
        buyButton = False
        while not buyButton:
            try:
                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-disabled")

                print("Button isnt ready")

                time.sleep(1)
                browser_Chrome.refresh()
            except:
                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-primary")

                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-secondary")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("cart-label")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-lg")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True
    

    def BestBuyBot6():
        browser_Chrome = webdriver.Chrome('/Users/manjinder/ShoppingBot/chromedriver')
        browser_Chrome.get("https://www.bestbuy.com/site/samsung-50-class-7-series-led-4k-uhd-smart-tizen-tv/6401738.p?skuId=6401738")
        buyButton = False
        while not buyButton:
            try:
                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-disabled")

                print("Button isnt ready")

                time.sleep(1)
                browser_Chrome.refresh()
            except:
                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-primary")

                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-secondary")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("cart-label")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-lg")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True


    def BestBuyBot7():
        browser_Chrome = webdriver.Chrome('/Users/manjinder/ShoppingBot/chromedriver')
        browser_Chrome.get("https://www.bestbuy.com/site/vizio-50-class-v-series-led-4k-uhd-smartcast-tv/6416380.p?skuId=6416380")
        buyButton = False
        while not buyButton:
            try:
                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-disabled")

                print("Button isnt ready")

                time.sleep(1)
                browser_Chrome.refresh()
            except:
                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-primary")

                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-secondary")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("cart-label")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-lg")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True
    

    def BestBuyBot8():
        browser_Chrome = webdriver.Chrome('/Users/manjinder/ShoppingBot/chromedriver')
        browser_Chrome.get("https://www.bestbuy.com/site/insignia-50-class-f30-series-led-4k-uhd-smart-fire-tv/6401029.p?skuId=6401029")
        buyButton = False
        while not buyButton:
            try:
                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-disabled")

                print("Button isnt ready")

                time.sleep(1)
                browser_Chrome.refresh()
            except:
                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-primary")

                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-secondary")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("cart-label")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-lg")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True
    

    def BestBuyBot9():
        browser_Chrome = webdriver.Chrome('/Users/manjinder/ShoppingBot/chromedriver')
        browser_Chrome.get("https://www.bestbuy.com/site/toshiba-50-class-led-4k-uhd-smart-firetv-edition-tv/6394759.p?skuId=6394759")
        buyButton = False
        while not buyButton:
            try:
                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-disabled")

                print("Button isnt ready")

                time.sleep(1)
                browser_Chrome.refresh()
            except:
                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-primary")

                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-secondary")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("cart-label")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-lg")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True
    

    def BestBuyBot10():
        browser_Chrome = webdriver.Chrome('/Users/manjinder/ShoppingBot/chromedriver')
        browser_Chrome.get("https://www.bestbuy.com/site/lg-50-class-un7000-series-led-4k-uhd-smart-webos-tv/6417301.p?skuId=6417301")
        buyButton = False
        while not buyButton:
            try:
                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-disabled")

                print("Button isnt ready")

                time.sleep(1)
                browser_Chrome.refresh()
            except:
                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-primary")

                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-secondary")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("cart-label")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True

                addToCartBtn = addButton = browser_Chrome.find_element_by_class_name("btn-lg")
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True
            
    

    canvas = tkinter.Canvas(root, width=1500, height = 1500)
    canvas.grid(columnspan = 5, rowspan = 5)
    root.resizable(True, True) #Width, #Height

    Instruction = tkinter.Label (root, text = "Pick a product!", relief = "solid", font ="Georgia 32 bold").place(x=700, y= 50)
    Instruction2 = tkinter.Label (root, text = "Record Your Purchases!", relief = "solid", font ="Georgia 12 bold").place(x=335, y= 140)

    menu = Menu(root)
    root.config(menu = menu)
    submenu = Menu(menu)
    menu.add_cascade(label = "File",menu = submenu)
    submenu.add_command(label = "Exit", command = exitInterface)

    submenu2 = Menu(menu)
    menu.add_cascade(label = "Option",menu = submenu2)
    submenu2.add_command(label = "About", command = aboutInterface)

    submenu3 = Menu(menu)
    menu.add_cascade(label = "Help",menu = submenu3)
    submenu3.add_command(label = "Help", command = helpInterface)


    browse_text_sixthInterface4 = tkinter.StringVar(root)
    browse_button_sixthInterface4 = tkinter.Button(root, textvariable = browse_text_sixthInterface4, font = "Georgia", bd=1, bg = "#D4D0C8", fg = "Black", height = 2, width = 15, command = BestBuy)
    browse_text_sixthInterface4.set("BestBuy")
    browse_button_sixthInterface4.place(x=1100, y= 160)

    browse_text_sixthInterface4 = tkinter.StringVar(root)
    browse_button_sixthInterface4 = tkinter.Button(root, textvariable = browse_text_sixthInterface4, font = "Georgia", bd=1, bg = "#D4D0C8", fg = "Black", height = 2, width = 25, command = BestBuyBot)
    browse_text_sixthInterface4.set("CLX SET Gaming Desktop")
    browse_button_sixthInterface4.place(x=900, y= 250)

    browse_text_sixthInterface4 = tkinter.StringVar(root)
    browse_button_sixthInterface4 = tkinter.Button(root, textvariable = browse_text_sixthInterface4, font = "Georgia", bd=1, bg = "#D4D0C8", fg = "Black", height = 2, width = 25, command = BestBuyBot10)
    browse_text_sixthInterface4.set("LG - 50 Class UN7000 Series")
    browse_button_sixthInterface4.place(x=1200, y= 250)

    browse_text_sixthInterface24 = tkinter.StringVar(root)
    browse_button_sixthInterface24 = tkinter.Button(root, textvariable = browse_text_sixthInterface24, font = "Georgia", bd=1, bg = "#D4D0C8", fg = "Black", height = 2, width = 25, command = BestBuyBot2)
    browse_text_sixthInterface24.set("ASUS-ROG Gaming Desktop")
    browse_button_sixthInterface24.place(x=900, y= 320)

    browse_text_sixthInterface34 = tkinter.StringVar(root)
    browse_button_sixthInterface34 = tkinter.Button(root, textvariable = browse_text_sixthInterface34, font = "Georgia", bd=1, bg = "#D4D0C8", fg = "Black", height = 2, width = 28, command = BestBuyBot3)
    browse_text_sixthInterface34.set("iBUYPOWER - ARC Gaming Desktop")
    browse_button_sixthInterface34.place(x=900, y= 390)

    browse_text_sixthInterface94 = tkinter.StringVar(root)
    browse_button_sixthInterface94 = tkinter.Button(root, textvariable = browse_text_sixthInterface94, font = "Georgia", bd=1, bg = "#D4D0C8", fg = "Black", height = 2, width = 28, command = BestBuyBot9)
    browse_text_sixthInterface94.set("Toshiba - 50 Class LED")
    browse_button_sixthInterface94.place(x=1200, y= 320)

    browse_text_sixthInterface84 = tkinter.StringVar(root)
    browse_button_sixthInterface84 = tkinter.Button(root, textvariable = browse_text_sixthInterface84, font = "Georgia", bd=1, bg = "#D4D0C8", fg = "Black", height = 2, width = 29, command = BestBuyBot8)
    browse_text_sixthInterface84.set(" Insignia™ - 50 Class F30 Series")
    browse_button_sixthInterface84.place(x=1200, y= 390)

    browse_text_sixthInterface44 = tkinter.StringVar(root)
    browse_button_sixthInterface44 = tkinter.Button(root, textvariable = browse_text_sixthInterface44, font = "Georgia", bd=1, bg = "#D4D0C8", fg = "Black", height = 2, width = 25, command = BestBuyBot4)
    browse_text_sixthInterface44.set("HP - ENVY Desktop")
    browse_button_sixthInterface44.place(x=900, y= 460)

    browse_text_sixthInterface74 = tkinter.StringVar(root)
    browse_button_sixthInterface74 = tkinter.Button(root, textvariable = browse_text_sixthInterface74, font = "Georgia", bd=1, bg = "#D4D0C8", fg = "Black", height = 2, width = 29, command = BestBuyBot7)
    browse_text_sixthInterface74.set("VIZIO - 50 Class V-Series")
    browse_button_sixthInterface74.place(x=1200, y= 460)

    browse_text_sixthInterface54 = tkinter.StringVar(root)
    browse_button_sixthInterface54 = tkinter.Button(root, textvariable = browse_text_sixthInterface54, font = "Georgia", bd=1, bg = "#D4D0C8", fg = "Black", height = 2, width = 29, command = BestBuyBot5)
    browse_text_sixthInterface54.set("CyberPowerPC - Gamer Master Desktop")
    browse_button_sixthInterface54.place(x=900, y= 530)

    browse_text_sixthInterface64 = tkinter.StringVar(root)
    browse_button_sixthInterface64 = tkinter.Button(root, textvariable = browse_text_sixthInterface64, font = "Georgia", bd=1, bg = "#D4D0C8", fg = "Black", height = 2, width = 29, command = BestBuyBot6)
    browse_text_sixthInterface64.set("Samsung - 50 Class 7 Series")
    browse_button_sixthInterface64.place(x=1200, y= 530)

    label_productName = Label(root, text= "Product Name: ", width = 20, font=("Times 16 bold"))
    label_productName.place(x=5, y=170)
    entry_1 = Entry(root, textvar = FetchInfo, bd = 1)
    entry_1.place(x=150, y=170)

    label_purchaseDate = Label(root, text= "Purchase Date: ", width = 20, font=("Times 16 bold"))
    label_purchaseDate.place(x=5, y=200)
    entry_2 = Entry(root, textvar = FetchInfo2, bd = 1)
    entry_2.place(x=150, y=200)

    label_cardName = Label(root, text= "Card Name: ", width = 20, font=("Times 16 bold"))
    label_cardName.place(x=5, y=230)
    entry_3 = Entry(root, textvar = FetchInfo3, bd = 1)
    entry_3.place(x=150, y=230)

    label_cardNumber = Label(root, text= "Card Number: ", width = 20, font=("Times 16 bold"))
    label_cardNumber.place(x=5, y=260)
    entry_4 = Entry(root, textvar = FetchInfo4, bd = 1)
    entry_4.place(x=150, y=260)

    browse_text_sixthInterface6 = tkinter.StringVar(root)
    browse_button_sixthInterface6 = tkinter.Button(root, textvariable = browse_text_sixthInterface6, font = "Georgia", bd=1, bg = "#D4D0C8", fg = "Black", height = 2, width = 35, command = validateInformation3)
    browse_text_sixthInterface6.set("Record Purchase")
    browse_button_sixthInterface6.place(x=170, y= 300)

    browse_text_sixthInterface7 = tkinter.StringVar(root)
    browse_button_sixthInterface7 = tkinter.Button(root, textvariable = browse_text_sixthInterface7, font = "Georgia", bd=1, bg = "#D4D0C8", fg = "Black", height = 2, width = 19, command = show3)
    browse_text_sixthInterface7.set("Show Purchase History")
    browse_button_sixthInterface7.place(x=230, y= 400)



root = tkinter.Tk()
text = tkinter.Text()
root.title("Shopping Bot- Manjinder Sandhu")

canvas = tkinter.Canvas(root, width=900, height = 500)
canvas.grid(columnspan = 5, rowspan = 5)

# Resize the Interface
root.resizable(True, True) #Width, #Height


#Shopping logo
logo = Image.open('ShoppingBot.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(image = logo)
logo_label.image = logo
logo_label.grid(column = 2, row = 0)

#Instructions
Instruction = tkinter.Label (root, text = "Welcome to the Shopping Bot!", font ="Georgia 32 bold")
Instruction.grid(columnspan = 10, rowspan = 10, column = 0, row = 0)
Instruction1 = tkinter.Label (root, text = "Manjinder Sandhu", fg="white", bg="#1D69AB", font ="Times 14 bold", width = 19).place(x=374, y= 73)

#Button
browse_text = tkinter.StringVar()
browse_button = tkinter.Button(root, textvariable = browse_text, font = "Georgia", bg = "#D4D0C8", fg = "Black", height = 2, width = 15, command = secondInterface)
browse_text.set("Create an Account")
browse_button.grid(column = 2, row = 2)

browse_text2 = tkinter.StringVar()
browse_button2 = tkinter.Button(root, textvariable = browse_text2, font = "Georgia", bg = "#D4D0C8", fg = "Black", height = 2, width = 15, command = fifthInterface)
browse_text2.set("Help")
browse_button2.grid(column = 2, row = 4)

browse_text3 = tkinter.StringVar()
browse_button3 = tkinter.Button(root, textvariable = browse_text3, font = "Georgia", bg = "#D4D0C8", fg = "Black", height = 2, width = 15, command = fourthInterface)
browse_text3.set("Sign In")
browse_button3.grid(column = 2, row = 3)

root.columnconfigure(2, weight = 1)
root.rowconfigure(7, weight = 1)
sizeGrip = ttk.Sizegrip(root)

#Adding a menu
menu = Menu(root)
root.config(menu = menu)

submenu = Menu(menu)
menu.add_cascade(label = "File",menu = submenu)
submenu.add_command(label = "Exit", command = exitInterface)

submenu2 = Menu(menu)
menu.add_cascade(label = "Option",menu = submenu2)
submenu2.add_command(label = "About", command = aboutInterface)

submenu3 = Menu(menu)
menu.add_cascade(label = "Help",menu = submenu3)
submenu3.add_command(label = "Help", command = helpInterface)

root.mainloop()