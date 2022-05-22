# import random
#
# class Wojownik():
#     def __init__(self):
#         self.pkt_zycia=random.randint(1,100)
#         self.pkt_ataku=random.randint(1,20)
#
#     def obrona(self, obrazenia):
#         self.pkt_zycia-=obrazenia
#         if self.pkt_zycia<0:
#             self.pkt_zycia=0
#
# gracz1=Wojownik()
# gracz2=Wojownik()
#
# while gracz1.pkt_zycia>0 and gracz2.pkt_zycia>0:
#     gracz1.obrona(gracz2.pkt_ataku)
#     gracz2.obrona(gracz1.pkt_ataku)
#     print("Gracz 1 otrzymał", gracz2.pkt_ataku, "obrazeń! Pozostało mu", gracz1.pkt_zycia, "pkt życia.")
#     print("Gracz 2 otrzymał", gracz1.pkt_ataku, "obrazeń! Pozostało mu", gracz2.pkt_zycia, "pkt życia.")

#####poprawna wersja

# import random
# class Wojownik():
#     def __init__(self):
#         self.pkt_zycia=random.randint(1,100)
#         self.pkt_ataku=random.randint(1,20)
#
#     def obrona(self, obrazenia):
#         self.pkt_zycia-=obrazenia
#         if self.pkt_zycia<0:
#             self.pkt_zycia=0
#
#     def pobierz_pkt_ataku(self):
#         return self.pkt_ataku
#
#     def pobierz_pkt_zycia(self):
#         return self.pkt_zycia
#
# gracz1=Wojownik()
# gracz2=Wojownik()
#
# while gracz1.pobierz_pkt_zycia()>0 and gracz2.pobierz_pkt_zycia()>0:
#     gracz1.obrona(gracz2.pobierz_pkt_ataku())
#     gracz2.obrona(gracz1.pobierz_pkt_ataku())
#     print("Gracz 1 otrzymał", gracz2.pobierz_pkt_ataku(), "obrazeń! Pozostało mu", gracz1.pobierz_pkt_zycia(), "pkt życia.")
#     print("Gracz 2 otrzymał", gracz1.pobierz_pkt_ataku(), "obrazeń! Pozostało mu", gracz2.pobierz_pkt_zycia(), "pkt życia.")


####DZIEDZICZENIE
# class Ssak():
#     def policz_lapy(self):
#         print("Mam 4 łapy")
#
# class Pies(Ssak):
#     def przywitaj(self):
#         print("Lubię biegać")
#
# class Kot(Ssak):
#     def przywitaj(self):
#         print("Miau")
#
# Reksio=Pies()
# Filemon=Kot()
# print("Reksio mówi: ")
# Reksio.przywitaj()
# Reksio.policz_lapy()
# print("\nFilemon mówi: ")
# Filemon.przywitaj()
# Filemon.policz_lapy()

# #####
# class Kregowiec():
#     def sprawdz_kregoslup(self):
#         print("mam kręgosłup")
#
# class Ssak():
#     def sprawdz_co_pije(self):
#         print("Piję mleko!")
#
# class Pies(Kregowiec, Ssak):
#     def sprawdz_co_robi(self):
#         print("merdam")
#
# Reksio=Pies()
# Reksio.sprawdz_kregoslup()
# Reksio.sprawdz_co_pije()
# Reksio.sprawdz_co_robi()




#zadanie 1, 2, 3
# import random
# class Wojownik():
#     def __init__(self):
#         self.pkt_zycia=random.randint(1,100)
#         self.pkt_ataku=random.randint(1,20)
#         self.pkt_magii=random.randint(1,30)
#         print("Jak chcesz nazwać wojownika?")
#         self.imie=input()
#
#     def obrona(self, obrazenia):
#         self.pkt_zycia-=obrazenia
#         if self.pkt_zycia<0:
#             self.pkt_zycia=0
#
#     def obrona_magiczna(self, obrazenia):
#         self.pkt_zycia-=obrazenia
#         if self.pkt_zycia<0:
#             self.pkt_zycia=0
#
#     def pobierz_pkt_ataku(self):
#         return self.pkt_ataku
#
#     def pobierz_pkt_zycia(self):
#         return self.pkt_zycia
#
#     def pobierz_pkt_magii(self):
#         return self.pkt_magii
#
#     def is_alive(self):
#         if self.pkt_zycia>0:
#             return True
#         else:
#             return False
#
# gracz1=Wojownik()
# gracz2=Wojownik()
#
# while gracz1.pobierz_pkt_zycia()>0 and gracz2.pobierz_pkt_zycia()>0:
#     gracz1.obrona(gracz2.pobierz_pkt_ataku())
#     gracz2.obrona(gracz1.pobierz_pkt_ataku())
#     print(gracz1.imie, "otrzymał", gracz2.pobierz_pkt_ataku(), "obrazeń! Pozostało mu", gracz1.pobierz_pkt_zycia(), "pkt życia.")
#     print(gracz2.imie, "otrzymał", gracz1.pobierz_pkt_ataku(), "obrazeń! Pozostało mu", gracz2.pobierz_pkt_zycia(), "pkt życia.")
#
#     gracz1.obrona_magiczna(gracz2.pobierz_pkt_magii())
#     gracz2.obrona_magiczna(gracz1.pobierz_pkt_magii())
#     print(gracz1.imie, "otrzymał", gracz2.pobierz_pkt_magii(), "obrazeń! Pozostało mu", gracz1.pobierz_pkt_zycia(), "pkt życia.")
#     print(gracz2.imie, "otrzymał", gracz1.pobierz_pkt_magii(), "obrazeń! Pozostało mu", gracz2.pobierz_pkt_zycia(), "pkt życia.")
#
#
# if gracz1.is_alive():
#     print(gracz1.imie, "wygrał!")
# if gracz2.is_alive():
#     print(gracz2.imie, "wygrał!")
# else:
#     print("Remis!")


###Zadanie 4 - moje źle, do poprawy
# import random
# class Postac():
#     def __init__(self):
#         self.pkt_zycia=random.randint(1,100)
#         print("Jak chcesz nazwać postać?")
#         self.imie=input()
#
#         self.klasa=()
#         print("Jaką klase wybierasz dla swojej postaci? Jeśli chcesz grać wojownikiem wybierz \"w\" a jeśli czarodziejem wybierz \"c\"")
#         self.wybor=input()
#         if self.wybor=="w":
#             self.klasa=Wojownik()
#         if self.wybor=="c":
#             self.klasa=Czarodziej()
#
#     def obrona(self, obrazenia):
#         self.pkt_zycia-=obrazenia
#         if self.pkt_zycia<0:
#             self.pkt_zycia=0
#
#     def pobierz_pkt_zycia(self):
#         return self.pkt_zycia
#
#     def is_alive(self):
#         if self.pkt_zycia>0:
#             return True
#         else:
#             return False
#
# class Wojownik(Postac):
#     def __init__(self):
#         self.pkt_ataku=random.randint(1,30)
#
#     def pobierz_pkt_ataku(self):
#         return self.pkt_ataku
#
# class Czarodziej(Postac):
#     def __init__(self):
#         self.pkt_ataku=random.randint(1,19)
#         self.pkt_magii=random.randint(19,40)
#
#     def pobierz_pkt_ataku(self):
#         return self.pkt_ataku
#
#     def pobierz_pkt_magii(self):
#         return self.pkt_magii
#
# gracz1=Postac()
# gracz2=Postac()
#
# while gracz1.pobierz_pkt_zycia()>0 and gracz2.pobierz_pkt_zycia()>0:
#     gracz1.obrona(gracz2.pobierz_pkt_ataku())
#     gracz2.obrona(gracz1.pobierz_pkt_ataku())
#     print(gracz1.imie, "otrzymał", gracz2.pobierz_pkt_ataku(), "obrazeń! Pozostało mu", gracz1.pobierz_pkt_zycia(), "pkt życia.")
#     print(gracz2.imie, "otrzymał", gracz1.pobierz_pkt_ataku(), "obrazeń! Pozostało mu", gracz2.pobierz_pkt_zycia(), "pkt życia.")
#
#     gracz1.obrona(gracz2.pobierz_pkt_magii())
#     gracz2.obrona(gracz1.pobierz_pkt_magii())
#     print(gracz1.imie, "otrzymał", gracz2.pobierz_pkt_magii(), "obrazeń! Pozostało mu", gracz1.pobierz_pkt_zycia(), "pkt życia.")
#     print(gracz2.imie, "otrzymał", gracz1.pobierz_pkt_magii(), "obrazeń! Pozostało mu", gracz2.pobierz_pkt_zycia(), "pkt życia.")
#
#
# if gracz1.is_alive():
#     print(gracz1.imie, "wygrał!")
# if gracz2.is_alive():
#     print(gracz2.imie, "wygrał!")
# else:
#     print("Remis!")



#  Zadanie 4
# import random
#
# class bitwa():
#
#     def __init__(self):
#         self.pkt_zycia=random.randint(1,100)
#         self.pkt_ataku=random.randint(1,20)
#         self.pkt_magii=random.randint(self.pkt_ataku,20)
#         print("Jak mam na imię?")
#         self.imie = input()
#
#     def jak_mam_na_imie(self):
#         return self.imie
#
#     def obrona(self, obrazenia):
#         self.pkt_zycia -= obrazenia
#         if self.pkt_zycia<0:
#             self.pkt_zycia=0
#
#     def obrona_magiczna(self, od_magii):
#         self.pkt_zycia -= od_magii
#         if self.pkt_zycia<0:
#             self.pkt_zycia=0
#
#     def zyje(self):
#         if self.pkt_zycia > 0:
#             return True
#         else:
#             return False
#
#     def pobierz_pkt_magii(self):
#         return self.pkt_magii
#
#     def pobierz_pkt_ataku(self):
#         return self.pkt_ataku
#
#     def pobierz_pkt_zycia(self):
#         return self.pkt_zycia
#
# gracz1=bitwa()
# gracz2=bitwa()
#
# print(gracz1.jak_mam_na_imie(), "ma być wojownikiem czy czarodziejem")
# odpowiedz1 = input()
# print("A", gracz2.jak_mam_na_imie(), "ma być wojownikiem czy czarodziejem?")
# odpowiedz2 = input()
#
# if odpowiedz1 == "czarodziejem" and odpowiedz2 == "czarodziejem":
#     while gracz1.pobierz_pkt_zycia()>0 and gracz2.pobierz_pkt_zycia()>0:
#         gracz1.obrona(gracz2.pobierz_pkt_ataku())
#         gracz2.obrona(gracz1.pobierz_pkt_ataku())
#
#         print("Gracz 1 otrzymał", gracz2.pobierz_pkt_ataku(), "obrażeń! Pozostało mu", gracz1.pobierz_pkt_zycia(), "pkt życia.")
#         print("Gracz 2 otrzymał", gracz1.pobierz_pkt_ataku(), "obrażeń! Pozostało mu", gracz2.pobierz_pkt_zycia(), "pkt życia.")
#
#         gracz1.obrona_magiczna(gracz2.pobierz_pkt_magii())
#         gracz2.obrona_magiczna(gracz1.pobierz_pkt_magii())
#         print("Gracz 1 otrzymał", gracz2.pobierz_pkt_magii(), "obrażeń magicznych! Pozostało mu", gracz1.pobierz_pkt_zycia(), "pkt życia.")
#         print("Gracz 2 otrzymał", gracz1.pobierz_pkt_magii(), "obrażeń magicznych! Pozostało mu", gracz2.pobierz_pkt_zycia(), "pkt życia.")
#
# elif odpowiedz1 == "czarodziejem" and odpowiedz2 == "wojownikiem":
#     while gracz1.pobierz_pkt_zycia()>0 and gracz2.pobierz_pkt_zycia()>0:
#         gracz1.obrona(gracz2.pobierz_pkt_ataku())
#         gracz2.obrona(gracz1.pobierz_pkt_ataku())
#
#         print("Gracz 1 otrzymał", gracz2.pobierz_pkt_ataku(), "obrażeń! Pozostało mu", gracz1.pobierz_pkt_zycia(), "pkt życia.")
#         print("Gracz 2 otrzymał", gracz1.pobierz_pkt_ataku(), "obrażeń! Pozostało mu", gracz2.pobierz_pkt_zycia(), "pkt życia.")
#
#         gracz1.obrona(gracz2.pobierz_pkt_ataku())
#         print("Gracz 1 otrzymał", gracz2.pobierz_pkt_ataku(), "obrażeń! Pozostało mu", gracz1.pobierz_pkt_zycia(), "pkt życia.")
#         gracz2.obrona_magiczna(gracz1.pobierz_pkt_magii())
#         print("Gracz 2 otrzymał", gracz1.pobierz_pkt_magii(), "obrażeń magicznych! Pozostało mu", gracz2.pobierz_pkt_zycia(), "pkt życia.")
#
# elif odpowiedz1 == "wojownikiem" and odpowiedz2 == "wojownikiem":
#     gracz1.obrona(gracz2.pobierz_pkt_ataku())
#     gracz2.obrona(gracz1.pobierz_pkt_ataku())
#
#     print("Gracz 1 otrzymał", gracz2.pobierz_pkt_ataku(), "obrażeń! Pozostało mu", gracz1.pobierz_pkt_zycia(), "pkt życia.")
#     print("Gracz 2 otrzymał", gracz1.pobierz_pkt_ataku(), "obrażeń! Pozostało mu", gracz2.pobierz_pkt_zycia(), "pkt życia.")
#
# elif odpowiedz1 == "wojownikiem" and odpowiedz2 == "czarodziejem":
#     while gracz1.pobierz_pkt_zycia()>0 and gracz2.pobierz_pkt_zycia()>0:
#         gracz1.obrona(gracz2.pobierz_pkt_ataku())
#         gracz2.obrona(gracz1.pobierz_pkt_ataku())
#
#         print("Gracz 1 otrzymał", gracz2.pobierz_pkt_ataku(), "obrażeń! Pozostało mu", gracz1.pobierz_pkt_zycia(), "pkt życia.")
#         print("Gracz 2 otrzymał", gracz1.pobierz_pkt_ataku(), "obrażeń! Pozostało mu", gracz2.pobierz_pkt_zycia(), "pkt życia.")
#
#         gracz1.obrona_magiczna(gracz2.pobierz_pkt_magii())
#         print("Gracz 1 otrzymał", gracz2.pobierz_pkt_magii(), "obrażeń magicznych! Pozostało mu", gracz1.pobierz_pkt_zycia(), "pkt życia.")
#         gracz1.obrona(gracz2.pobierz_pkt_ataku())
#         print("Gracz 2 otrzymał", gracz1.pobierz_pkt_ataku(), "obrażeń! Pozostało mu", gracz2.pobierz_pkt_zycia(), "pkt życia.")
#
#
# if gracz1.zyje():
#     print(gracz1.jak_mam_na_imie(), "wygrał!")
# elif gracz2.zyje():
#     print(gracz2.jak_mam_na_imie(), "wygrał!")


# Zadanie 5
# class Sim:
#
#     def __init__(self):
#         print("Jak sim ma się nazywać?")
#         self.sim = input()
#         self.pkt_znajomosci = 0
#
#     def rozmowa(self):
#         self.pkt_znajomosci += 10
#         print("Punkty znajomości:", self.pkt_znajomosci)
#
#     def bojka(self):
#         print("walczymy")
#         self.pkt_znajomosci -= 50
#         print("Punkty znajomości:", self.pkt_znajomosci)
#
#     def daj_prezent(self):
#         print("daję prezent")
#         self.pkt_znajomosci += 20
#         print("Punkty znajomości:", self.pkt_znajomosci)
#
#     def klotnia(self):
#         print("kłócimy się")
#         self.pkt_znajomosci -= 10
#         print("Punkty znajomości:", self.pkt_znajomosci)
#
# sim1 = Sim()
# sim2 = Sim()
# while True:
#     print("Co simy chcą robić?")
#     odpowiedz = input()
#     if odpowiedz == "rozmawiać":
#         print("rozmawiamy ze sobą")
#         sim1.rozmowa()
#         sim2.rozmowa()
