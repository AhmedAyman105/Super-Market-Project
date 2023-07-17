from tkinter import *
import math , os , random 
from tkinter import messagebox
import numpy as np

def second_win() :
    class Super(Tk) :
        def __init__(self,root):
            self.root = root
            self.root.geometry('1400x770+70+25')
            self.root.title('Eska-Market')
            self.root.resizable(False,False)
            self.root.iconbitmap(r"SM images\SM LOGO 1.ico")
            title = Label(self.root,text='ادارة المشاريع : سوبر ماركت',fg='white',bg='#0B2F3A',font=('tajawal',16,'bold'))
            title.pack(fill=X)
            #===== Customer Data =====#
            f1 = Frame(self.root,bg='#0B2F3A',width=350,height=200)
            f1.place(x=1049,y=38)
            c_data = Label(f1,text=': بيانات المشتري',font=('tajawal',13,'bold'),bg='#0B2F3A',fg='tomato')
            c_data.place(x=210,y=6)
            c_name = Label(f1,text='اسم المشتري',font=('tajawal',10,'bold'),bg='#0B2F3A',fg='white')
            c_name.place(x=250,y=50)
            c_phone = Label(f1,text='هاتف المشتري',font=('tajawal',10,'bold'),bg='#0B2F3A',fg='white')
            c_phone.place(x=248,y=90)
            bill_num = Label(f1,text='رقم الفاتورة',font=('tajawal',10,'bold'),bg='#0B2F3A',fg='white')
            bill_num.place(x=265,y=130)

            #===== Enteries =====#

            self.ent0_1 = StringVar()
            self.ent0_2 = StringVar()
            self.ent0_3 = StringVar()

            # Random Number For Bill
            x = random.randint(1000,9999)
            self.ent0_3.set(str(x))

            ent_name = Entry(f1,font=('tajawal',10),fg='black',highlightcolor='#DBA901'
                            ,highlightthickness=2,justify='center',textvariable=self.ent0_1)
            ent_name.place(x=80,y=52)
            ent_phone = Entry(f1,font=('tajawal',10),fg='black',highlightcolor='#DBA901'
                            ,highlightthickness=2,justify='center',textvariable=self.ent0_2)
            ent_phone.place(x=80,y=92)
            ent_bill = Entry(f1,font=('tajawal',10),fg='black',highlightcolor='#DBA901'
                            ,highlightthickness=2,justify='center',textvariable=self.ent0_3)
            ent_bill.place(x=80,y=132)

            btn_c = Button(f1,width=7,text='بحث',fg='black',bg='white',activebackground='#DBA901',font=('tajawal',10,'bold'),height=5)
            btn_c.place(x=9,y=52)

            #===== Bill =====#
            b = Label(f1,text='[ الفواتير ]',font=('tajawal',13,'bold'),fg='gold' , bg='#0B2F3A')
            b.place(x=150,y=165)
            f2 = Frame(self.root,width=350,height=350,bg='white')
            f2.place(x=1049,y=238)

            scroll_y = Scrollbar(f2,orient='vertical')
            self.textarea = Text(f2,yscrollcommand=scroll_y.set)
            scroll_y.pack(side='left',fill=Y)
            scroll_y.config(command=self.textarea.yview)
            self.textarea.pack(fill=BOTH,expand=1)
            #===== Price =====#
            f3 = Frame(self.root,bg='#0B2F3A',width=760,height=139)
            f3.place(x=639,y=630)

            btn_1 = Button(f3,bg='#DBA901',fg='#0B2F3A',width=12,font=('tajawal',12,'bold'),text='الحساب',command=self.total)
            btn_1.place(x=570,y=20)
            btn_2 = Button(f3,bg='#DBA901',fg='#0B2F3A',width=12,font=('tajawal',12,'bold'),text='افراغ الحقول',command=(self.reset))
            btn_2.place(x=430,y=20)
            btn_3 = Button(f3,bg='#DBA901',fg='#0B2F3A',width=12,font=('tajawal',12,'bold'),text='تصدير فاتورة',command=self.billing)
            btn_3.place(x=570,y=80)
            btn_4 = Button(f3,bg='#DBA901',fg='#0B2F3A',width=12,font=('tajawal',12,'bold'),text='اغلاق البرنامج',command=self.close)
            btn_4.place(x=430,y=80)

            #  Total Variables

            self.bokoliat = StringVar()
            self.adoat = StringVar()
            self.elec = StringVar()


            lb1 = Label(f3,text='الحساب الكلي للبقوليات',fg='gold',bg='#0B2F3A',font=('tajawal',12,'bold'))
            lb1.place(x=230 ,y=22)

            self.ent1 = Entry(f3,bg='white',font=('tajawal',10),highlightcolor='#DBA901',highlightthickness=2,justify='center',textvariable=self.bokoliat)
            self.ent1.place(x=60 ,y=28)

            lb2 = Label(f3,text='حساب اللوازم المنزلية',fg='gold',bg='#0B2F3A',font=('tajawal',12,'bold'))
            lb2.place(x=245 ,y=55)

            ent2 = Entry(f3,bg='white',font=('tajawal',10),highlightcolor='#DBA901',highlightthickness=2,justify='center',textvariable=self.adoat)
            ent2.place(x=60 ,y=61)

            lb3 = Label(f3,text='حساب ادوات الكهرباء',fg='gold',bg='#0B2F3A',font=('tajawal',12,'bold'))
            lb3.place(x=247 ,y=88)

            ent3 = Entry(f3,bg='white',font=('tajawal',10),highlightcolor='#DBA901',highlightthickness=2,justify='center',textvariable=self.elec)
            ent3.place(x=60 ,y=93)

            #===== Items =====#

            f4 = Frame(self.root,bd=2,width=318,height=731,bg='#0B2F3A')
            f4.place(x=1,y=38)

            bo = Label(f4,text='البقوليات',font=('tajawal',13,'bold'),fg='gold',bg='#0B2F3A',width=10)
            bo.place(x=100,y=10)
            
            bo1 = Label(f4,text='رز',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bo1.place(x=250,y=50)

            bo2 = Label(f4,text='برغل',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bo2.place(x=230,y=90)

            bo3 = Label(f4,text='فاصولياء',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bo3.place(x=205,y=130)

            bo4 = Label(f4,text='عدس',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bo4.place(x=226,y=170)

            bo5 = Label(f4,text='معكرونة',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bo5.place(x=205,y=210)

            bo6 = Label(f4,text='فريكة',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bo6.place(x=226,y=250)

            bo7 = Label(f4,text='حمص',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bo7.place(x=223,y=290)

            bo8 = Label(f4,text='فول',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bo8.place(x=233,y=330)

            bo9 = Label(f4,text='ملح',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bo9.place(x=233,y=370)

            bo10 = Label(f4,text='سكر',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bo10.place(x=230,y=410)
            
            bo11 = Label(f4,text='فلفل اسود',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bo11.place(x=190,y=450)

            bo12 = Label(f4,text='فلفل احمر',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bo12.place(x=190,y=490)

            bo13 = Label(f4,text='لوبيا',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bo13.place(x=230,y=530)

            bo14 = Label(f4,text='قمح',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bo14.place(x=226,y=570)

            bo15 = Label(f4,text='شعير',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bo15.place(x=220,y=610)

            bo16 = Label(f4,text='ذرة',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bo16.place(x=232,y=650)

            # [Variables : Seeds ]

            self.ent_1 = IntVar()
            self.ent_2 = IntVar()
            self.ent_3 = IntVar()
            self.ent_4 = IntVar()
            self.ent_5 = IntVar()
            self.ent_6 = IntVar()
            self.ent_7 = IntVar()
            self.ent_8 = IntVar()
            self.ent_9 = IntVar()
            self.ent_10 = IntVar()
            self.ent_11 = IntVar()
            self.ent_12 = IntVar()
            self.ent_13 = IntVar()
            self.ent_14 = IntVar()
            self.ent_15 = IntVar()
            self.ent_16 = IntVar()

            entbo1 = Entry(f4,font=('tajawal',10),justify='center',width=18,textvariable=self.ent_1)
            entbo1.place(x=35 ,y=53)

            entbo2 = Entry(f4,font=('tajawal',10),justify='center',width=18,textvariable=self.ent_2)
            entbo2.place(x=35 ,y=93)

            entbo3 = Entry(f4,font=('tajawal',10),justify='center',width=18,textvariable=self.ent_3)
            entbo3.place(x=35 ,y=133)

            entbo4 = Entry(f4,font=('tajawal',10),justify='center',width=18,textvariable=self.ent_4)
            entbo4.place(x=35 ,y=173)

            entbo5 = Entry(f4,font=('tajawal',10),justify='center',width=18,textvariable=self.ent_5)
            entbo5.place(x=35 ,y=213)

            entbo6 = Entry(f4,font=('tajawal',10),justify='center',width=18,textvariable=self.ent_6)
            entbo6.place(x=35 ,y=253)

            entbo7 = Entry(f4,font=('tajawal',10),justify='center',width=18,textvariable=self.ent_7)
            entbo7.place(x=35 ,y=293)

            entbo8 = Entry(f4,font=('tajawal',10),justify='center',width=18,textvariable=self.ent_8)
            entbo8.place(x=35 ,y=333)

            entbo9 = Entry(f4,font=('tajawal',10),justify='center',width=18,textvariable=self.ent_9)
            entbo9.place(x=35 ,y=373)

            entbo10 = Entry(f4,font=('tajawal',10),justify='center',width=18,textvariable=self.ent_10)
            entbo10.place(x=35 ,y=413)

            entbo11 = Entry(f4,font=('tajawal',10),justify='center',width=18,textvariable=self.ent_11)
            entbo11.place(x=35 ,y=453)

            entbo12 = Entry(f4,font=('tajawal',10),justify='center',width=18,textvariable=self.ent_12)
            entbo12.place(x=35 ,y=493)

            entbo13 = Entry(f4,font=('tajawal',10),justify='center',width=18,textvariable=self.ent_13)
            entbo13.place(x=35 ,y=533)

            entbo14 = Entry(f4,font=('tajawal',10),justify='center',width=18,textvariable=self.ent_14)
            entbo14.place(x=35 ,y=573)

            entbo15 = Entry(f4,font=('tajawal',10),justify='center',width=18,textvariable=self.ent_15)
            entbo15.place(x=35 ,y=613)

            entbo16 = Entry(f4,font=('tajawal',10),justify='center',width=18,textvariable=self.ent_16)
            entbo16.place(x=35 ,y=653)

            # Second Part # 

            f5 = Frame(self.root,bd=2,width=318,height=731,bg='#0B2F3A')
            f5.place(x=320,y=38)

            bh = Label(f5,text='اللوازم المنزلية',font=('tajawal',13,'bold'),fg='gold',bg='#0B2F3A',width=15)
            bh.place(x=90,y=10)
            
            bh1 = Label(f5,text='مصفاة',font=('tajawal',12),fg='white',bg='#0B2F3A')
            bh1.place(x=230,y=50)

            bh2 = Label(f5,text='صحن',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bh2.place(x=240,y=90)

            bh3 = Label(f5,text='كاس',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bh3.place(x=240,y=130)

            bh4 = Label(f5,text='ابريق',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bh4.place(x=240,y=170)

            bh5 = Label(f5,text='سكين',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bh5.place(x=235,y=210)

            bh6 = Label(f5,text='شوك',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bh6.place(x=235,y=250)

            bh7 = Label(f5,text='ملاعق',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bh7.place(x=230,y=290)

            bh8 = Label(f5,text='صينية',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bh8.place(x=233,y=330)

            bh9 = Label(f5,text='مقشرة',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bh9.place(x=220,y=370)

            bh10 = Label(f5,text='حفارة',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bh10.place(x=235,y=410)
            
            bh11 = Label(f5,text='سلة قمامة',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bh11.place(x=200,y=450)

            bh12 = Label(f5,text='فتاحة علب',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bh12.place(x=205,y=490)

            bh13 = Label(f5,text='منفضة',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bh13.place(x=225,y=530)

            bh14 = Label(f5,text='اكياس',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bh14.place(x=230,y=570)

            bh15 = Label(f5,text='لوح تقطيع',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bh15.place(x=200,y=610)

            bh16 = Label(f5,text='وعاء',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            bh16.place(x=236,y=650)

            # [Variables : HomeNeeds]

            self.ent1_1 = IntVar()
            self.ent1_2 = IntVar()
            self.ent1_3 = IntVar()
            self.ent1_4 = IntVar()
            self.ent1_5 = IntVar()
            self.ent1_6 = IntVar()
            self.ent1_7 = IntVar()
            self.ent1_8 = IntVar()
            self.ent1_9 = IntVar()
            self.ent1_10 = IntVar()
            self.ent1_11 = IntVar()
            self.ent1_12 = IntVar()
            self.ent1_13 = IntVar()
            self.ent1_14 = IntVar()
            self.ent1_15 = IntVar()
            self.ent1_16 = IntVar()

            entbh1 = Entry(f5,font=('tajawal',10),justify='center',width=18,textvariable=self.ent1_1)
            entbh1.place(x=35 ,y=53)

            entbh2 = Entry(f5,font=('tajawal',10),justify='center',width=18,textvariable=self.ent1_2)
            entbh2.place(x=35 ,y=93)

            entbh3 = Entry(f5,font=('tajawal',10),justify='center',width=18,textvariable=self.ent1_3)
            entbh3.place(x=35 ,y=133)

            entbh4 = Entry(f5,font=('tajawal',10),justify='center',width=18,textvariable=self.ent1_4)
            entbh4.place(x=35 ,y=173)

            entbh5 = Entry(f5,font=('tajawal',10),justify='center',width=18,textvariable=self.ent1_5)
            entbh5.place(x=35 ,y=213)

            entbh6 = Entry(f5,font=('tajawal',10),justify='center',width=18,textvariable=self.ent1_6)
            entbh6.place(x=35 ,y=253)

            entbh7 = Entry(f5,font=('tajawal',10),justify='center',width=18,textvariable=self.ent1_7)
            entbh7.place(x=35 ,y=293)

            entbh8 = Entry(f5,font=('tajawal',10),justify='center',width=18,textvariable=self.ent1_8)
            entbh8.place(x=35 ,y=333)

            entbh9 = Entry(f5,font=('tajawal',10),justify='center',width=18,textvariable=self.ent1_9)
            entbh9.place(x=35 ,y=373)

            entbh10 = Entry(f5,font=('tajawal',10),justify='center',width=18,textvariable=self.ent1_10)
            entbh10.place(x=35 ,y=413)

            entbh11 = Entry(f5,font=('tajawal',10),justify='center',width=18,textvariable=self.ent1_11)
            entbh11.place(x=35 ,y=453)

            entbh12 = Entry(f5,font=('tajawal',10),justify='center',width=18,textvariable=self.ent1_12)
            entbh12.place(x=35 ,y=493)

            entbh13 = Entry(f5,font=('tajawal',10),justify='center',width=18,textvariable=self.ent1_13)
            entbh13.place(x=35 ,y=533)

            entbh14 = Entry(f5,font=('tajawal',10),justify='center',width=18,textvariable=self.ent1_14)
            entbh14.place(x=35 ,y=573)

            entbh15 = Entry(f5,font=('tajawal',10),justify='center',width=18,textvariable=self.ent1_15)
            entbh15.place(x=35 ,y=613)

            entbh16 = Entry(f5,font=('tajawal',10),justify='center',width=18,textvariable=self.ent1_16)
            entbh16.place(x=35 ,y=653)

            # Third Part 
            f6 = Frame(self.root,bd=2,width=409,height=591,bg='#0B2F3A')
            f6.place(x=639,y=38)

            be = Label(f6,text='ادوات كهربائية',font=('tajawal',13,'bold'),fg='gold',bg='#0B2F3A',width=15)
            be.place(x=120,y=10)
            
            be1 = Label(f6,text='مكنسة',font=('tajawal',12),fg='white',bg='#0B2F3A')
            be1.place(x=290,y=50)

            be2 = Label(f6,text='تلفزيون',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            be2.place(x=285,y=90)

            be3 = Label(f6,text='غسالة',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            be3.place(x=288,y=130)

            be4 = Label(f6,text='ميكروويف',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            be4.place(x=270,y=170)

            be5 = Label(f6,text='خلاط',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            be5.place(x=295,y=210)

            be6 = Label(f6,text='فرن',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            be6.place(x=300,y=250)

            be7 = Label(f6,text='فرن غاز',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            be7.place(x=280,y=290)

            be8 = Label(f6,text='مروحة',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            be8.place(x=290,y=330)

            be9 = Label(f6,text='مروحة سقف',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            be9.place(x=250,y=370)

            be10 = Label(f6,text='لابتوب',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            be10.place(x=285,y=410)
            
            be11 = Label(f6,text='سخان',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            be11.place(x=290,y=450)

            be12 = Label(f6,text='مكواة',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            be12.place(x=290,y=490)

            be13 = Label(f6,text='شاحن',font=('tajawal',12),fg='white',bg='#0B2F3A',justify='right')
            be13.place(x=290,y=530)

            # [Variables : Electricity]
            self.ent2_1 = IntVar()
            self.ent2_2 = IntVar()
            self.ent2_3 = IntVar()
            self.ent2_4 = IntVar()
            self.ent2_5 = IntVar()
            self.ent2_6 = IntVar()
            self.ent2_7 = IntVar()
            self.ent2_8 = IntVar()
            self.ent2_9 = IntVar()
            self.ent2_10 = IntVar()
            self.ent2_11 = IntVar()
            self.ent2_12 = IntVar()
            self.ent2_13 = IntVar()

            entbe1 = Entry(f6,font=('tajawal',10),justify='center',width=18,textvariable=self.ent2_1)
            entbe1.place(x=55 ,y=53)

            entbe2 = Entry(f6,font=('tajawal',10),justify='center',width=18,textvariable=self.ent2_2)
            entbe2.place(x=55 ,y=93)

            entbe3 = Entry(f6,font=('tajawal',10),justify='center',width=18,textvariable=self.ent2_3)
            entbe3.place(x=55 ,y=133)

            entbe4 = Entry(f6,font=('tajawal',10),justify='center',width=18,textvariable=self.ent2_4)
            entbe4.place(x=55 ,y=173)

            entbe5 = Entry(f6,font=('tajawal',10),justify='center',width=18,textvariable=self.ent2_5)
            entbe5.place(x=55 ,y=213)

            entbe6 = Entry(f6,font=('tajawal',10),justify='center',width=18,textvariable=self.ent2_6)
            entbe6.place(x=55 ,y=253)

            entbe7 = Entry(f6,font=('tajawal',10),justify='center',width=18,textvariable=self.ent2_7)
            entbe7.place(x=55 ,y=293)

            entbe8 = Entry(f6,font=('tajawal',10),justify='center',width=18,textvariable=self.ent2_8)
            entbe8.place(x=55 ,y=333)

            entbe9 = Entry(f6,font=('tajawal',10),justify='center',width=18,textvariable=self.ent2_9)
            entbe9.place(x=55 ,y=373)

            entbe10 = Entry(f6,font=('tajawal',10),justify='center',width=18,textvariable=self.ent2_10)
            entbe10.place(x=55 ,y=413)

            entbe11 = Entry(f6,font=('tajawal',10),justify='center',width=18,textvariable=self.ent2_11)
            entbe11.place(x=55 ,y=453)

            entbe12 = Entry(f6,font=('tajawal',10),justify='center',width=18,textvariable=self.ent2_12)
            entbe12.place(x=55 ,y=493)

            entbe13 = Entry(f6,font=('tajawal',10),justify='center',width=18,textvariable=self.ent2_13)
            entbe13.place(x=55 ,y=533)

            self.welcome()

        def welcome(self) :
                self.textarea.delete('1.0',END)
                self.textarea.insert(END,"\t سوبر ماركت اسكا يرحب بكم \t")
                self.textarea.insert(END,"\n =======================================")
                self.textarea.insert(END,f"\n\t B.NUM   : {self.ent0_3.get()} ")
                self.textarea.insert(END,f"\n\t Name    : {self.ent0_1.get()} ")
                self.textarea.insert(END,f"\n\t Phone   : {self.ent0_2.get()} ")
                self.textarea.insert(END,"\n =======================================")
                self.textarea.insert(END,"\n المشتريات         العدد         السعر")
                self.textarea.insert(END,"\n =======================================")
        
        
        def total(self) :
            
            # Bokoliat Total

            # Prices
            array1 = np.array([1.5,1.5,2,3,1.5,1.4,1.3,1.7,2.5,2.6,2.7,2.9,1.4,1.6,1.4,1.6])
            
            # Quantities
            array2 = np.array([])
            for i in range(1,17) :
                ent_attr_name = "ent_" + str(i)
                value = float(getattr(self, ent_attr_name).get())
                array2 = np.append(array2,value,) 
            self.array3 = array1*array2
            self.total1 = np.sum(self.array3)  
            self.bokoliat.set(str(self.total1)+ "$")     

            
            # Home Need Total

            # Prices
            array4 = np.array([1.5,1.5,2,3,1.5,1.4,1.3,1.7,2.5,2.6,2.7,2.9,1.4,1.6,1.4,1.6])
            
            # Quantities
            array5 = np.array([])
            for i in range(1,17) :
                ent_attr_name = "ent1_" + str(i)
                value = float(getattr(self, ent_attr_name).get())
                array5 = np.append(array5,value,) 
            self.array6 = array4*array5
            self.total2 = np.sum(self.array6)  
            self.adoat.set(str(self.total2)+ "$") 
            

            # Elec Total
            # Prices
            array7 = np.array([1.5,1.5,2,3,1.5,1.4,1.3,1.7,2.5,2.6,2.7,2.9,1.4])
            
            # Quantities
            array8 = np.array([])
            for i in range(1,14) :
                ent_attr_name = "ent2_" + str(i)
                value = float(getattr(self, ent_attr_name).get())
                array8 = np.append(array8,value,) 
            self.array9 = array7*array8
            self.total3 = np.sum(self.array9)   
            self.elec.set(str(self.total3)+ "$")

            
        def reset(self):
            self.welcome()
            for i in range(1, 17):
                ent_attr_name = "ent_" + str(i)
                ent_obj = getattr(self,ent_attr_name )
                ent_obj.set(0)

                ent_attr_name = "ent1_" + str(i)
                ent_obj = getattr(self,ent_attr_name )
                ent_obj.set(0)

                if i <=13 :
                    ent_attr_name = "ent2_" + str(i)
                    ent_obj = getattr(self,ent_attr_name )
                    ent_obj.set(0)
                else :
                    pass
            self.bokoliat .set(0)
            self.adoat.set(0) 
            self.elec.set(0) 
            self.ent0_1.set('')
            self.ent0_2.set('')
            self.ent0_3.set('')
        
        def save(self) :
            a =  messagebox.askyesno('هل تريد حفظ الفاتورة؟','حفظ')
            if a > 0: 
                self.fator = self.textarea.get('1.0',END)
                # specify the path to the directory
                directory = r"D:\Fatora"

                # create the directory if it does not exist
                if not os.path.exists(directory):
                    os.makedirs(directory)
                path = str(self.ent0_3.get()) + ".txt"
                file_path = os.path.join(directory,path )
                f = open(file_path,'w',encoding='UTF-8')
                f.write(self.fator)
                f.close()
            else :
                pass
            
        def billing(self) :
            self.total()
            if self.ent0_1.get() == '' or self.ent0_2.get() == '' :
                messagebox.showerror('خطاء','لايجوز ترك حقل الاسم ورقم الهاتف فارغا')
            elif self.bokoliat.get() == '0' and self.adoat.get() == '0' and self.get() == '0':
                messagebox.showerror('خطاء','لم تختار اي من المنتجات')
            
            else :
                self.welcome()
                for i in range(1,17) :
                    ent_attr_name = "ent_" + str(i)
                    ent_obj = getattr(self,ent_attr_name).get()
                    bo = ['الرز','برغل','فاصولياء','عدس','معكرونة','فريكة','حمص','فول','ملح','سكر','فلفل اسود','فلفل احمر','لوبيا','قمح','شعير','ذرة']
                    product_name = bo[i-1]
                    qt = ent_obj
                    price = self.array3[(i-1)]
                    txt = f"\n{price:.2f}\t\t{qt}\t\t{(product_name)}"
                    if qt !=0:
                        self.textarea.insert(END,txt)
                    else :
                        pass
                # Home Needs
                for i in range(1,17) :
                    ent_attr_name2 = "ent1_" + str(i)
                    ent_obj2 = getattr(self,ent_attr_name2).get()
                    bo2 = ['مصفاه','صحن','كاس','ابريق','سكين','شوك','ملاعق','صينية','مقشرة','حفارة','سلة قمامة','فتاحة علب','منفضة','اكياس','لوح تقطيع','وعاء']
                    product_name2 = bo2[i-1]
                    qt2 = ent_obj2
                    price2 = self.array6[i-1]
                    txt2 = f"\n{price2:.2f}\t\t{qt2}\t\t{(product_name2)}"
                    if qt2 !=0:
                        self.textarea.insert(END,txt2)
                    else :
                        pass
                # Elec 
                for i in range(1,14) :
                    ent_attr_name3 = "ent2_" + str(i)
                    ent_obj3 = getattr(self,ent_attr_name3).get()
                    bo3 = ['مكنسة','تلفزيون','غسالة','ميكرويف','خلاط','فرن','فرن غاز','مروحة','مروحة سقف','لابتوب','سخان','مكواه','شاحن']
                    product_name3 = bo3[i-1]
                    qt3 = ent_obj3
                    price3 = self.array9[i-1]
                    txt3 = f"\n{price3:.2f}\t\t{qt3}\t\t{(product_name3)}"
                    if qt3 !=0:
                        self.textarea.insert(END,txt3)
                    else :
                        pass
                self.textarea.insert(END,'\n.........................................')
                self.textarea.insert(END,f'\n {self.total1+self.total2+self.total3}$ \t\t\tالمجموع الكلي   ')
                self.textarea.insert(END,'\n.........................................')
            if self.ent0_1.get() == '' or self.ent0_2.get() == '' :
                messagebox.showerror('خطاء','لايجوز ترك حقل الاسم ورقم الهاتف فارغا')
            else:
                self.save()

        def close(self) :
            self.root.destroy()



    root2 = Tk()
    Super(root2)

    root2.mainloop()
