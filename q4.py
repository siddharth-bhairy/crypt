
import tkinter as tk
import sqlite3

key="mysecretkey"

con=sqlite3.connect("users.db")
cur=con.cursor()
cur.execute("create table if not exists users(username,password)")
con.commit()

def vernam(text):
    res=""
    for i in range(len(text)):
        res+=chr(ord(text[i])^ord(key[i%len(key)]))
    return res

def store():
    username=user.get()
    password=pass1.get()
    confirm=pass2.get()

    if password!=confirm:
        msg.config(text="Passwords do not match")
        return

    if len(password)!=8:
        msg.config(text="Password must be 8 characters")
        return

    if not any(i.isdigit() for i in password):
        msg.config(text="Password must contain a digit")
        return

    if not any(i.isupper() for i in password):
        msg.config(text="Password must contain a capital letter")
        return

    if not any(not i.isalnum() for i in password):
        msg.config(text="Password must contain a special symbol")
        return

    epass=vernam(password)
    cur.execute("insert into users values(?,?)",(username,epass))
    con.commit()
    msg.config(text="Registration successful")

def refresh():
    user.delete(0,tk.END)
    pass1.delete(0,tk.END)
    pass2.delete(0,tk.END)
    msg.config(text="")

def login_screen():
    reg.destroy()

    global login
    login=tk.Tk()
    login.title("Login")
    login.geometry("400x250")

    box=tk.Frame(login,bd=2,relief="solid")
    box.pack(padx=30,pady=30,fill="both",expand=True)

    tk.Label(box,text="LOGIN",font=("Arial",16)).pack(pady=15)

    global luser,lpass,lmsg

    f1=tk.Frame(box)
    f1.pack(pady=5)
    tk.Label(f1,text="Username").pack(side="left",padx=5)
    luser=tk.Entry(f1)
    luser.pack(side="left")

    f2=tk.Frame(box)
    f2.pack(pady=5)
    tk.Label(f2,text="Password").pack(side="left",padx=5)
    lpass=tk.Entry(f2,show="*")
    lpass.pack(side="left")

    b=tk.Frame(box)
    b.pack(pady=10)

    tk.Button(b,text="OK",command=check_login).pack(side="left",padx=10)
    tk.Button(b,text="BACK",command=back).pack(side="left",padx=10)

    lmsg=tk.Label(box,text="")
    lmsg.pack()

    login.mainloop()

def check_login():
    username=luser.get()
    password=lpass.get()

    if username=="" or password=="":
        lmsg.config(text="Please enter username and password")
        return

    epass=vernam(password)

    cur.execute("select * from users where username=? and password=?",(username,epass))
    data=cur.fetchone()

    if data:
        lmsg.config(text="Login successful")
    else:
        lmsg.config(text="Login failed")

def back():
    login.destroy()
    registration()

def registration():
    global reg,user,pass1,pass2,msg

    reg=tk.Tk()
    reg.title("Registration")
    reg.geometry("450x350")

    box=tk.Frame(reg,bd=2,relief="solid")
    box.pack(padx=30,pady=30,fill="both",expand=True)

    tk.Label(box,text="REGISTER",font=("Arial",16)).pack(pady=15)

    f1=tk.Frame(box)
    f1.pack(pady=5)
    tk.Label(f1,text="Username").pack(side="left",padx=5)
    user=tk.Entry(f1)
    user.pack(side="left")

    f2=tk.Frame(box)
    f2.pack(pady=5)
    tk.Label(f2,text="Password").pack(side="left",padx=5)
    pass1=tk.Entry(f2,show="*")
    pass1.pack(side="left")

    f3=tk.Frame(box)
    f3.pack(pady=5)
    tk.Label(f3,text="Confirm Password").pack(side="left",padx=5)
    pass2=tk.Entry(f3,show="*")
    pass2.pack(side="left")

    b=tk.Frame(box)
    b.pack(pady=15)

    tk.Button(b,text="REFRESH",command=refresh).pack(side="left",padx=5)
    tk.Button(b,text="STORE",command=store).pack(side="left",padx=15)
    tk.Button(b,text="LOGIN",command=login_screen).pack(side="left",padx=5)

    msg=tk.Label(box,text="")
    msg.pack()

    reg.mainloop()

registration()

