from tkinter import * 
# My Module
from sm2 import *
# Warning Messsegs 
from tkinter import messagebox

# To Deal With the Broweser (Open Links)
import webbrowser

# Deal With System Paths 
import os

# Deal With System
import sys

# Main Window root => Object , Tk => Class
root = Tk()

# Title of The Window
root.title("Super Market سوبر ماركت")

# Icon for The Window => Accept ICO extension Only
root.iconbitmap(r"SM images\SM LOGO 1.ico")

# geomerty(widthxheight)
root.geometry("800x450+400+200")

# Size of the Window X Y or C R
root.resizable(False,False)



###############################################################################

# Label (master , Options)

# Font = (Font Family ,Size , Type)
title = Label(root,text="Super Market System",fg='gold',bg='black',font=('tajawal','16','bold '))

# Fill the Background in X Direction
title.pack(fill=X)

# Functions 
f = 'https://www.facebook.com/es.sa.18659/'
y = 'https://youtube.com/playlist?list=PLSiLeKadTQ7lSFEmVIGdU9YdMMOE9lLFa'
t = 'https://t.me/ahmedayman105'

user1 = "Ahmed_Ayman"
pass1 = "1234"


def facebook() :
    webbrowser.open_new(f)

def telegram() :
    webbrowser.open_new(t)

def youtube() :
    webbrowser.open_new(y)
# Also we can use built in function quit
def close() :
    root.destroy()

def about_me() :
    messagebox.showinfo('Developer',''''
    Eng Ahmed Ayman 
    Phone No. : 01099605975
        ''')
    
def about_prog():
    messagebox.showinfo('عن البرنامج','تدريب علي مشروع سوبر ماركت باستخدام بايثون')

def login() :
    user =  ent1.get()
    passs =  ent2.get()
    if user == user1 and passs==pass1 :
        messagebox.showinfo('Welcome','Correct Username & Password')
        root.destroy()
        second_win()

    else :
        messagebox.showerror('Erorr','Wrong Username or Password')



# Divide GUI Into Frames

f1 = Frame(root,width=230,height=420,bg='#0B2F3A')
f1.place(x=570,y=37)


title1 = Label(f1,text='مشروع سوبر ماركت',fg='white',bg='#0B2F3A',font=('tajawal',12,'bold '))
title1.place(x=50 , y=10)

title2 = Label(f1,text='المطور احمد ايمن',fg='white',bg='#0B2F3A',font=('tajawal',12,'bold '))
title2.place(x=55 , y=45)

title3 = Label(f1,text='وسائل الاتصال بنا',fg='white',bg='#0B2F3A',font=('tajawal',12,'bold '))
title3.place(x=55 , y=80)

# Buttons 

b1 = Button(f1,text='حسابنا علي الفيسبوك',width=22,fg='black',bg='#DBA901',font=('tajawal',12,'bold '),command=facebook)
b1.place(x=12,y=130)

b2 = Button(f1,text='حسابنا علي التلجرام',width=22,fg='black',bg='#DBA901',font=('tajawal',12,'bold '),command=telegram)
b2.place(x=12,y=177)

b3 = Button(f1,text='قناتنا علي يوتيوب',width=22,fg='black',bg='#DBA901',font=('tajawal',12,'bold '),command=youtube)
b3.place(x=12,y=225)

b4 = Button(f1,text='لمحة عن المطور',width=22,fg='black',bg='#DBA901',font=('tajawal',12,'bold '),command=about_me)
b4.place(x=12,y=272)


b5 = Button(f1,text='لمحة عن المشروع',width=22,fg='black',bg='#DBA901',font=('tajawal',12,'bold '),command=about_prog)
b5.place(x=12,y=318)

b6 = Button(f1,text='اغلاق البرنامج',width=22,fg='black',bg='#DBA901',font=('tajawal',12,'bold '),relief="flat",command=close)
b6.place(x=12,y=365)

# Landing Photo

# Photo Extension must be PNG
photo = PhotoImage(file=r'SM images\Super Market.png')

img1 = Label(root,image=photo)
img1.place(x=90,y=43,width=380,height=272)

f2 = Frame(root,width=570,height=120,bg='#0B2F3A')
f2.place(x=0,y=330)

photo2 = PhotoImage(file=r'SM images\login.png')
img2 = Label(root,image=photo2)
img2.config(borderwidth=0, highlightthickness=0, padx=0, pady=0)
img2.place(x=450,y=335,width=110,height=110)

l1 = Label(f2,text='اسم المستخدم',bg='#0B2F3A',fg='gold',font=('tajawal',12,'bold '))
l1.place(x=330,y=20)

l2 = Label(f2,text='كلمة المرور',bg='#0B2F3A',fg='gold',font=('tajawal',12,'bold '))
l2.place(x=360,y=75)



# Enteries 

ent1 = Entry(f2,font=('tajawal',12),justify=CENTER)
ent1.place(x=130,y=23)

ent2 = Entry(f2,font=('tajawal',12),justify=CENTER,show='*')
ent2.place(x=130,y=75)

btn7 = Button(f2,text='تسجيل الدخول',bg='gold',fg='#0B2F3A',font=('tajawal',10,'bold'),height=1,command=login)
btn7.place(x=20,y=46)

root.mainloop()

