######################### Zarządzanie układem: place ##########################
# from tkinter import *
#
# glowneOkno=Tk()
# glowneOkno.title("Moje okno")
# glowneOkno.geometry("300x250")
#
# przyciskCzerwony=Button(glowneOkno,text="Czerwony",fg="red")
# przyciskCzerwony.place(x=70, y=10)
# przyciskZielony=Button(glowneOkno,text="Zielony",fg="green")
# przyciskZielony.place(x=75, y=40)
# przyciskNiebieski=Button(glowneOkno,text="Niebieski",fg="blue")
# przyciskNiebieski.place(x=71, y=70)
# przyciskBialy=Button(glowneOkno,text="Bialy",fg="white")
# przyciskBialy.place(x=80, y=100)
#
# glowneOkno.mainloop()


####
## Usuwanie widżetów ##
####
# from tkinter import *
# glowneOkno = Tk()
# glowneOkno.geometry("400x400")
#
# def usunPrzycisk():
#     przyciskPoprzednie.destroy()
#
# przyciskPoprzednie = Button(glowneOkno, text="wciśnij mnie", command= usunPrzycisk)
# przyciskPoprzednie.place(x=150, y=100)
# glowneOkno.mainloop()


####
## Usuwanie widżetów, inny przykład ##
####
# from tkinter import *
# from random import randint
#
# glowneOkno = Tk()
# glowneOkno.geometry("400x400")
#
# def usunPrzycisk():
#     przyciskPoprzednie.destroy()
#     stworzprzycisk()
#
# def stworzprzycisk():
#     global przyciskPoprzednie
#     przyciskPoprzednie = Button(glowneOkno, text="wciśnij mnie", command= usunPrzycisk)
#     losujX=randint(0,300)
#     losujY=randint(0,300)
#     przyciskPoprzednie.place(x=losujX, y=losujY)
#
# stworzprzycisk()
# glowneOkno.mainloop()


####
## Prosty pasek menu ##
####
# from tkinter import *
# from tkinter import messagebox
#
# glowneOkno=Tk()
# pasekMenu=Menu(glowneOkno)
#
# pierwszeMenu=Menu(pasekMenu,tearoff=0)
# pierwszeMenu.add_command(label="Wyjdz",command=glowneOkno.quit)
# pasekMenu.add_cascade(label="Pierwsze",menu=pierwszeMenu)
#
# glowneOkno.config(menu=pasekMenu)
# glowneOkno.mainloop()


####
## Pasek menu ##
####
# from tkinter import *
# from tkinter import messagebox
#
# def akcjaZrob():
#     messagebox.showinfo("Coś","Wyświetlam okno")
#
# def akcjaAutor():
#     messagebox.showinfo("Autor","Autorem jestem ja")
#
# glowneOkno=Tk()
# pasekMenu=Menu(glowneOkno)
#
# pierwszeMenu=Menu(pasekMenu,tearoff=0)
# pierwszeMenu.add_command(label="Zrób coś",command=akcjaZrob)
# pierwszeMenu.add_command(label="Wyjdz",command=glowneOkno.quit)
# pasekMenu.add_cascade(label="Pierwsze",menu=pierwszeMenu)
#
# pomocMenu=Menu(pasekMenu,tearoff=0)
# pomocMenu.add_command(label="O Autorze",command=akcjaAutor)
# pasekMenu.add_cascade(label="Autor",menu=pomocMenu)
#
# glowneOkno.config(menu=pasekMenu)
# glowneOkno.mainloop()


####
## Wczytanie pliku graficznego ##
####
# from tkinter import *
# from PIL import Image, ImageTk
#
# glowneOkno=Tk()
# plotno=Canvas(glowneOkno, width=400, height=400)
# plotno.pack()
# obraz=Image.open("1.png")
# obrazTk=ImageTk.PhotoImage(obraz)
# plotno.create_image(200,200,image=obrazTk)
#
# glowneOkno.mainloop()


####
## Zmiana wielkości obraza ##
####
# from tkinter import *
# from PIL import Image, ImageTk
#
# glowneOkno=Tk()
# plotno=Canvas(glowneOkno, width=400, height=400)
# plotno.pack()
# obraz=Image.open("1.png")

# obraz= obraz.resize((500,128))

# obrazTk=ImageTk.PhotoImage(obraz)
# plotno.create_image(200,200,image=obrazTk)
#
# glowneOkno.mainloop()


####
## Obrót obrazka ##
####
# from tkinter import *
# from PIL import Image, ImageTk
#
# glowneOkno=Tk()
# plotno=Canvas(glowneOkno, width=400, height=400)
# plotno.pack()
# obraz=Image.open("1.png")
#
# obraz= obraz.rotate(70)
#
# obrazTk=ImageTk.PhotoImage(obraz)
# plotno.create_image(200,200,image=obrazTk)
#
# glowneOkno.mainloop()


####
## Zmiana palety kolorów z RGB na odcienie szarości ##
####
# from tkinter import *
# from PIL import Image, ImageTk
#
# glowneOkno=Tk()
# plotno=Canvas(glowneOkno, width=400, height=400)
# plotno.pack()
#
# obraz=Image.open("1.png").convert("L")
#
# obraz= obraz.convert("L")
#
# obrazTk=ImageTk.PhotoImage(obraz)
# plotno.create_image(200,200,image=obrazTk)
#
# glowneOkno.mainloop()


####
## Wykorzystaniefiltrów ##
####
# from tkinter import *
# from PIL import Image, ImageTk, ImageFilter
#
# glowneOkno=Tk()
# plotno=Canvas(glowneOkno, width=400, height=400)
# plotno.pack()
# obraz=Image.open("1.png")
#
# obraz= obraz.filter(ImageFilter.CONTOUR)
#
# obrazTk=ImageTk.PhotoImage(obraz)
# plotno.create_image(200,200,image=obrazTk)
#
# glowneOkno.mainloop()


##### zadanie 1,2 #####
# from tkinter import *
# from tkinter import messagebox
# from random import randint
#
# def akcjaZrob():
#     messagebox.showinfo("Coś","Wyświetlam okno")
#
# def akcjaAutor():
#     messagebox.showinfo("Autor","Autorem jestem ja")
#
# def akcja1():
#     messagebox.showinfo("Akcja1","To jest akcja 1")
#
# def akcja2():
#     messagebox.showinfo("Akcja2","To jest akcja 2")
#
# def akcja3():
#     messagebox.showinfo("Akcja3","To jest akcja 3")
#
# def akcja4():
#     messagebox.showinfo("Akcja4","To jest akcja 4")
#
# glowneOkno=Tk()
# pasekMenu=Menu(glowneOkno)
# glowneOkno.geometry("400x400")
#
# pierwszeMenu=Menu(pasekMenu,tearoff=0)
# pierwszeMenu.add_command(label="Zrób coś",command=akcjaZrob)
# pierwszeMenu.add_command(label="Wyjdz",command=glowneOkno.quit)
# pasekMenu.add_cascade(label="Pierwsze",menu=pierwszeMenu)
#
# pomocMenu=Menu(pasekMenu,tearoff=0)
# pomocMenu.add_command(label="O Autorze",command=akcjaAutor)
# pomocMenu.add_command(label="Si", command=akcja4)
# pasekMenu.add_cascade(label="Autor",menu=pomocMenu)
#
# trzecieMenu=Menu(pasekMenu, tearoff=0)
# trzecieMenu.add_command(label="Czy to działa?", command=akcja1)
# trzecieMenu.add_command(label="Działa?", command=akcja2)
# trzecieMenu.add_command(label="Ta?", command=akcja3)
# pasekMenu.add_cascade(label="Okej?",menu=trzecieMenu)
#
# glowneOkno.config(menu=pasekMenu)
# glowneOkno.mainloop()


################## zadanie 3 ############### DO POPRAWY
from tkinter import *
from tkinter import messagebox
from random import randint

def stworzprzycisk():
    przycisk=Buttton(glowneOkno, text="a")
    przycisk.place(x=150, y=100)

def usunPrzycisk():
    przycisk.destroy()
    przycisk = Button(glowneOkno, text="wciśnij mnie", command= usunPrzycisk)
    przycisk.place(x=50, y=15)


glowneOkno=Tk()
pasekMenu=Menu(glowneOkno)
glowneOkno.geometry("400x400")

pierwszeMenu=Menu(pasekMenu,tearoff=0)
pierwszeMenu.add_command(label="Usuń przycisk",command=usunPrzycisk)
pasekMenu.add_cascade(label="usun",menu=pierwszeMenu)

pomocMenu=Menu(pasekMenu,tearoff=0)
pomocMenu.add_command(label="Stwórz przycisk",command=stworzprzycisk)
pasekMenu.add_cascade(label="stworz",menu=pomocMenu)

glowneOkno.config(menu=pasekMenu)
glowneOkno.mainloop()
