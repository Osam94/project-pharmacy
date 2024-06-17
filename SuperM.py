from tkinter import *
from tkinter import messagebox
import webbrowser
import os
import sys

pro = Tk()
pro.geometry("800x450+280+50")
pro.resizable(False,False)
pro.title("АПТЕКА 4753")
pro.iconbitmap(r"C:\Users\Hp\Desktop\project1\sup.ico")
title=Label(pro , text="Pharmacy System",fg="gold",bg="black",font=('tajawal',16,"bold"))
title.pack(fill=X)

F1=Frame(pro,width=230,height=420,bg="#0B2F3A")
F1.place(x=570,y=37)
Title1=Label(F1,text="АПТЕКА 4753",bg="#0B2F3A",fg="white",font=("tajawal",12,"bold"))
Title1.place(x=40,y=10)
Title2=Label(F1,text="КРАСНОПРУДНАЯ 15",bg="#0B2F3A",fg="white",font=("tajawal",12,"bold"))
Title2.place(x=20,y=40)
Title3=Label(F1,text="ОТДЕЛЕНИЯ ВОСТОК",bg="#0B2F3A",fg="white",font=("tajawal",12,"bold"))
Title3.place(x=20,y=70)
B1=Button(F1,text="НАШ САЙТ",width=22,fg="black",bg="#DBA901",font=("tajawal",11,"bold"))
B1.place(x=6,y=130)
B2=Button(F1,text="СТАНЦИЯ МЕТРО",width=22,fg="black",bg="#DBA901",font=("tajawal",11,"bold"))
B2.place(x=6,y=177)
B3=Button(F1,text="ПРО АПТЕКЕ",width=22,fg="black",bg="#DBA901",font=("tajawal",11,"bold"))
B3.place(x=6,y=225)
B4=Button(F1,text="СОТРУДНКИ",width=22,fg="black",bg="#DBA901",font=("tajawal",11,"bold"))
B4.place(x=6,y=272)
B5=Button(F1,text="ОТДЕЛЬ КАДРОВ",width=22,fg="black",bg="#DBA901",font=("tajawal",11,"bold"))
B5.place(x=6,y=318)
B6=Button(F1,text="ВЫХОД",width=22,fg="black",bg="#DBA901",font=("tajawal",11,"bold"))
B6.place(x=6,y=365)


photo=PhotoImage(file="C:\\Users\\Hp\\Desktop\\project1\\pharm.png")
imo=Label(pro,image=photo)
imo.place(x=160,y=43,height=272)

F2=Frame(pro,width=570,height=120,bg="#0B2F3A")
F2.place(x=0,y=330)


photo1=PhotoImage(file="C:\\Users\\Hp\\Desktop\\project1\\login3.png")
imo1=Label(pro,image=photo1)
imo1.place(x=10,y=335,width=110,height=110)


L1=Label(F2,text="LOGIN",fg="gold",bg="#0B2F3A",font=("tajawal",12))
L1.place(x=130,y=25)

L2=Label(F2,text="PASSWORD",fg="gold",bg="#0B2F3A",font=("tajawal",12))
L2.place(x=130,y=70)

En1=Entry(F2,font=("tajawal",12))
En1.place(x=230,y=26)

En2=Entry(F2,font=("tajawal",12))
En2.place(x=230,y=71)

B=Button(F2,text="LOG IN",bg="#DBA901",font=("tajawal",12,),width=12,height=3)
B.place(x=430,y=26)


















pro.mainloop()