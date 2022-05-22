# class Telewizor():
#     def powitanie(self):
#         print("Cześć. To ja, Twój telewizor!")
#
#     liczba_kanalow=5 ##wisi-zły przykład
#     def wyswietl_kanaly(self):
#         print(self.liczba_kanalow)
#
#     lista_kanalow=["TVP1", "TVP2", "Polsat", "TVN", "MTV"] ##wisi-zły przykład
#     def wyswietl_liste_kanalow(self):
#         for kanal in self.lista_kanalow:
#             print(kanal)
#
# moj_TV=Telewizor()
# moj_TV.powitanie()
# moj_TV.wyswietl_kanaly()
# moj_TV.wyswietl_liste_kanalow()

#KONSTRUKTOR
# class Telewizor:
#     def __init__(self):
#         self.lista_kanalow=["TVP1", "TVP2", "Polsat", "TVN", "MTV"]
#         self.nr_kanalu=0
#         print("Telewizor włączony")
#         print("Ustawiony kanał: ", self.lista_kanalow[self.nr_kanalu])
#
#     def wyswietl_liste_kanalow(self):
#         for kanal in self.lista_kanalow:
#             print(kanal)
#
#     def ustaw_kanal(self, wpisany_kanal):
#         self.nr_kanalu=wpisany_kanal
#
#     def wyswietl_aktualny_kanal(self):
#         print("Ustawiony kanał: ", self.lista_kanalow[self.nr_kanalu])
#
#
#
# moj_TV=Telewizor()
# moj_TV.wyswietl_liste_kanalow()
# print("Jaki kanał włączyć?")
# nowy_kanal=int(input())
# moj_TV.ustaw_kanal(nowy_kanal)
# moj_TV.wyswietl_aktualny_kanal()

####
# class Student:
#     def __init__(self):
#         self.wiek=19
#         print("Pojawił się nowy studnet! Jak go nazwać?")
#         self.imie=input()
#
#     def wyswietl_podsumowanie(self):
#         print("Student to: ", self.imie, "i ma", self.wiek, "lat")
#
# osoba1=Student()
# osoba2=Student()
# osoba1.wyswietl_podsumowanie()
# osoba2.wyswietl_podsumowanie()

#ZADANIE 1 i 2 i 3
# class Telewizor:
#     def __init__(self):
#         self.lista_kanalow=["TVP1", "TVP2", "Polsat", "TVN", "MTV"]
#         self.nr_kanalu=0
#         self.poziom_glosnosci=5
#         print("Telewizor włączony")
#         print("Ustawiony kanał: ", self.lista_kanalow[self.nr_kanalu])
#
#     def wyswietl_liste_kanalow(self):
#         for kanal in self.lista_kanalow:
#             print(kanal)
#
#     def ustaw_kanal(self, wpisany_kanal):
#         self.nr_kanalu=wpisany_kanal
#
#     def wyswietl_aktualny_kanal(self):
#         print("Ustawiony kanał: ", self.lista_kanalow[self.nr_kanalu])
#
#     def wyswietl_poziom_glosnosci(self):
#         print("Aktualna głośność to: ", self.poziom_glosnosci)
#
#     def zmien_poziom_glosnosci(self, nowy_poziom):
#         self.poziom_glosnosci=nowy_poziom
#         if self.poziom_glosnosci>20:
#             self.poziom_glosnosci=20
#         elif self.poziom_glosnosci<0:
#             self.poziom_glosnosci=0
#
#     def wyswietl_kanaly(self):
#         print("Dostęne kanały: ", self.lista_kanalow)
#
#     def zmien_kanal(self, gora_dol):
#         if gora_dol == "+":
#             self.nr_kanalu += 1
#         elif gora_dol == "-":
#             self.nr_kanalu -= 1
#
#         if self.nr_kanalu == -1:
#             self.nr_kanalu = 4
#         elif self.nr_kanalu == 5:
#             self.nr_kanalu = 0
#
#
# moj_TV= Telewizor()
# while True:
#     print("Co chcesz zrobić?")
#     wybor = input()
#     if wybor == "wyświetl głośność":
#         moj_TV.wyswietl_poziom_glosnosci()
#     elif wybor == "zmień głośność":
#         print("Podaj nowy poziom głośności: ")
#         poziom= int(input())
#         moj_TV.zmien_poziom_glosnosci(poziom)
#         moj_TV.wyswietl_poziom_glosnosci()
#     elif wybor == "wyświetl listę kanały":
#         moj_TV.wyswietl_liste_kanalow()
#     elif wybor == "ustaw kanał":
#         print("Jaki kanał włączyć?")
#         nowy_kanal=int(input())
#         moj_TV.ustaw_kanal(nowy_kanal)
#         moj_TV.wyswietl_aktualny_kanal()
#     elif wybor == "wyświetl kanały":
#         moj_TV.wyswietl_kanaly()
#     elif wybor == "zmien kanal":
#         print("Zwiekszyc czy zmienijszyc")
#         wybor=input()
#         moj_TV.zmien_kanal(wybor)
#         moj_TV.wyswietl_aktualny_kanal()
#     elif wybor == "wyłącz":
#         break

#ZADANIE 4
# class kalkulator:
#     def __init__(self):
#         print("witaj w kalkulatorze!")
#     def dodawanie(self,x,y):
#         print("wynik dodawania:",int(x) + int(y))
#     def odejmowanie(self,x,y):
#         print("wynik odejmowania:",int(x) - int(y))
#     def mnozenie(self,x,y):
#         print("wynik mnożenia:",int(x) * int(y))
#     def dzielenie(self,x,y):
#         print("wynik dzielenia:",int(x) / int(y))
#
# mojkalkulator=kalkulator()
#
# print("podaj pierwszą liczbę")
# x = input()
# print("podaj drugą liczbę")
# y = input()
#
# print("jakie działanie mam na nich zrobić?")
# odp = input()
# if odp == "dodawanie":
#     mojkalkulator.dodawanie(x,y)
# elif odp == "odejmowanie":
#     mojkalkulator.odejmowanie(x,y)
# elif odp == "mnozenie":
#     mojkalkulator.mnozenie(x,y)
# elif odp == "dzielenie":
#     mojkalkulator.dzielenie(x,y)
# else:
#     print("nie da się :(")

#ZADANIE 5
# import random
#
# class kostka:
#     def __init__(self):
#         print("ile ścian ma mieć kostka?")
#         self.sciany = int(input())
#         print("okej!")
#     def rzut(self):
#         print("wyrzucon",random.randint(1,self.sciany))
#
# mojakostka=kostka()
# mojakostka.rzut()

#ZADANIE 6
# import random
#
# class los:
#     def __init__(self):
#         print("witaj w losowanku!")
#         self.wynik = []
#         self.liczniczek = 0
#     def losowanie(self,ile):
#         while self.liczniczek<ile:
#             cyfra = random.randint(0,9)
#             if cyfra not in self.wynik:
#                 self.wynik.append(cyfra)
#                 self.liczniczek += 1
#     def pokaz_wynik(self):
#         print("wylosowano:","".join(str(znak) for znak in self.wynik))
#
# mojlosik = los()
# print("ile cyfr chcesz losować? [maksymalnie 6]")
# ile = int(input())
# while ile>6:
#     print("zła wartość!:(")
#     print("ile cyfr chcesz losować? [maksymalnie 6]")
#     ile = int(input())
# mojlosik.losowanie(ile)
# mojlosik.pokaz_wynik()

#ZADANIE 7
#7
# class dziennik:
#     def __init__(self):
#         print("witaj w żmijowym usosie")
#         self.przedmioty = ["programowanie","epistemologia","procesiki","meto"]
#         self.oceny = []
#         self.srednia = 0
#     def wczytaj_oceny(self,imie):
#         for i in range (len(self.przedmioty)):
#             print("jaką ocenę ma",imie,"z przedmiotu",self.przedmioty[i],"?")
#             ocena = int(input())
#             self.oceny.append(ocena)
#     def wyswietl_oceny(self,imie):
#         print("PODSUMOWANIE:")
#         for i in range (len(self.przedmioty)):
#             print("ocena osoby",imie,"z przedmiotu", self.przedmioty[i],"to",self.oceny[i])
#     def wyswietl_srednia(self,imie):
#         for i in range (len(self.przedmioty)):
#             self.srednia += self.oceny[i]
#         self.srednia = self.srednia / 4
#         print("średnia osoby",imie,"to",self.srednia)
#
#
# emma=dziennik()
# kaja=dziennik()
# julia=dziennik()
# emma.wczytaj_oceny("emma")
# kaja.wczytaj_oceny("kaja")
# julia.wczytaj_oceny("julia")
# emma.wyswietl_oceny("emma")
# emma.wyswietl_srednia("emma")
# kaja.wyswietl_oceny("kaja")
# kaja.wyswietl_srednia("kaja")
# julia.wyswietl_oceny("julia")
# julia.wyswietl_srednia("julia")


#8
# class prostokat:
#     def __init__(self,dlugosc,szerokosc):
#         self.pole = szerokosc * dlugosc
#     def pokaz_pole(self):
#         print("pole tego prostokąta to",self.pole)
#
# mojprostokat=prostokat(3,4)
# mojprostokat.pokaz_pole()


# #9
# class prostokat:
#     def __init__(self):
#         print("podaj długość prostokąta")
#         self.dlugosc = int(input())
#         print("podaj szerokość")
#         self.szerokosc = int(input())
#     def wylicz_pole(self):
#         pole = self.szerokosc * self.dlugosc
#         print("pole tego prostokąta to",pole)
#
# mojprostokat=prostokat()
# mojprostokat.wylicz_pole()

# # #10
# class prostokat:
#     def __init__(self,dlugosc,szerokosc):
#         self.pole = szerokosc * dlugosc
#     def pokaz_pole(self):
#         return self.pole
#
# prostokat1=prostokat(3,4)
# print("pole pierwszego prostokątu to",prostokat1.pokaz_pole())
#
# prostokat2=prostokat(2,3)
# print("pole drugiego to",prostokat2.pokaz_pole())
#
# prostokat3=prostokat(1,2)
# print("pole trzeciego to",prostokat3.pokaz_pole())

#11
# import time
#
# class mikrofalowka:
#     def __init__(self, nazwa):
#         print(nazwa,"zadzwoni za...")
#     def odliczanie(self):
#         for i in range (5,0,-1):
#             print(i,"...")
#             time.sleep(1)
#         print("JUUUUUUŻ!!!!!!!!!!")
#
# mojbudzik=mikrofalowka("mój budzik")
# mojbudzik.odliczanie()
