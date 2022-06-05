# from tkinter import *
# from tkinter import messagebox
#
# def akcja_przycisk():
#     messagebox.showinfo("Okno powitalne", pole_tekstowe.get())
#
# glowne_okno=Tk()
# glowne_okno.title("Moje okno")
# glowne_okno.geometry("300x250")
#
# opis_pola_tekstowego = Label(glowne_okno, text="Wprowadź tekst")
# opis_pola_tekstowego.pack(side=LEFT)
# pole_tekstowe=Entry(glowne_okno)
# pole_tekstowe.pack(side=RIGHT)
#
# przycisk1=Button(glowne_okno, text = "Powitanie", command = akcja_przycisk)
# przycisk1.pack(side=BOTTOM)
# glowne_okno.mainloop()


#####
###ZARZĄDZANIE UKŁADEM PACK()
#####
# from tkinter import *
# glowne_okno = Tk()
#
# czerwony=Button(glowne_okno, text="Czerwony", fg="red")
# czerwony.pack(side=LEFT)
# zielony=Button(glowne_okno, text="Zielony", fg="green")
# zielony.pack(side=LEFT)
# niebieski=Button(glowne_okno, text="Niebieski", fg="blue")
# niebieski.pack(side=TOP)
# bialy=Button(glowne_okno, text="Biały", fg="white")
# bialy.pack(side=BOTTOM)
# glowne_okno.mainloop()


#####
##ZARZĄDZANIE UKŁADEM GRID()
#####
# from tkinter import *
# glowne_okno=Tk()
#
# przycisk_czerwony=Button(glowne_okno,text="Czerwony",fg="red")
# przycisk_czerwony.grid(row=0 ,column=0)
# przycisk_zielony=Button(glowne_okno,text="Zielony",fg="green")
# przycisk_zielony.grid(row=0 ,column=1)
# przycisk_niebieski=Button(glowne_okno,text="Niebieski",fg="blue")
# przycisk_niebieski.grid(row=0 ,column=2)
# przycisk_bialy=Button(glowne_okno,text="Biały",fg="white")
# przycisk_bialy.grid(row=1 ,column=0)
# przycisk_zolty=Button(glowne_okno,text="Żółty",fg="yellow")
# przycisk_zolty.grid(row=1 ,column=1)
# przycisk_czarny=Button(glowne_okno,text="Czarny",fg="black")
# przycisk_czarny.grid(row=1 ,column=3)
#
# glowne_okno.mainloop()

####RADIOBUTTON
# from tkinter import *
# from tkinter import messagebox
# glowne_okno = Tk()
# zadanie1 = IntVar()
# zadanie2 = IntVar()
#
# def akcja_przycisk():
#     if zadanie1.get()==1:
#         messagebox.showinfo("Say Hello","Witaj")
#     if zadanie2.get()==2:
#         messagebox.showinfo("Say Hello", "Cześć")
#
# rprzycisk1 = Radiobutton(glowne_okno, text ="Wybór 1",
#                         variable=zadanie1, value=1)
# rprzycisk1.pack()
#
# rprzycisk2 = Radiobutton(glowne_okno, text ="Wybór 2",
#                         variable=zadanie1, value=2)
# rprzycisk2.pack()
#
# rprzycisk1 = Radiobutton(glowne_okno, text ="Wybór inny 1",
#                         variable=zadanie2, value=1)
# rprzycisk1.pack()
#
# rprzycisk2 = Radiobutton(glowne_okno, text ="Wybór inny2",
#                         variable=zadanie2, value=2)
# rprzycisk2.pack()
#
# przycisk=Button(glowne_okno, text="Powitanie", command=akcja_przycisk)
# przycisk.pack()
# glowne_okno.mainloop()


#ZADANIE 1
# from tkinter import *
# from tkinter import messagebox
#
# def akcja_przycisk():
#     messagebox.showinfo("Okno powitalne", "1")
#
# def akcja_przycisk1():
#     messagebox.showinfo("Okno powitalne", "2")
#
# def akcja_przycisk2():
#     messagebox.showinfo("Okno powitalne", "3")
#
# glowne_okno=Tk()
# glowne_okno.title("Moje okno")
# glowne_okno.geometry("300x250")
#
# przycisk1=Button(glowne_okno, text = "Powitanie", command = akcja_przycisk)
# przycisk1.pack()
#
# przycisk2=Button(glowne_okno, text = "Pożegnanie", command = akcja_przycisk1)
# przycisk2.pack()
#
# przycisk3=Button(glowne_okno, text = "PPP", command = akcja_przycisk2)
# przycisk3.pack()
#
# glowne_okno.mainloop()


#ZADANIE 5
from tkinter import *
from tkinter import messagebox

glowne_okno=Tk()

def akcja_1():
    messagebox.showinfo("Kalkulator", "1")


jeden=Button(glowne_okno,text="1", command = akcja_1)
jeden.grid(row=0 ,column=0)
dwa=Button(glowne_okno,text="2")
dwa.grid(row=0 ,column=1)
trzy=Button(glowne_okno,text="3")
trzy.grid(row=0 ,column=2)
cztery=Button(glowne_okno,text="4")
cztery.grid(row=1 ,column=0)
piec=Button(glowne_okno,text="5")
piec.grid(row=1 ,column=1)
szesc=Button(glowne_okno,text="6")
szesc.grid(row=1 ,column=2)
siedem=Button(glowne_okno,text="7")
siedem.grid(row=2 ,column=0)
osiem=Button(glowne_okno,text="8")
osiem.grid(row=2 ,column=1)
dziewiec=Button(glowne_okno,text="9")
dziewiec.grid(row=2 ,column=2)
zero=Button(glowne_okno,text="0")
zero.grid(row=3 ,column=1)

plus=Button(glowne_okno, text="+")
plus.grid(row=4, column= 0)
minus=Button(glowne_okno, text="-")
minus.grid(row=4, column= 1)
mnoz=Button(glowne_okno, text="*")
mnoz.grid(row=4, column= 2)
dziel=Button(glowne_okno, text="/")
dziel.grid(row=4, column= 3)
rowna_sie=Button(glowne_okno, text="=")
rowna_sie.grid(row=5, column= 1)

glowne_okno.mainloop()
