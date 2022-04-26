##ZADANIE 1
# #Napisz funkcję, która wczytuje listę z liczbami całkowitymi z zakresu od 0 do 99
# #oraz zwraca tę samą listę, ale pozbawioną liczb większych niż 60.
# #Zaprezentuj działanie funkcji na trzech różnych listach tzn.
# #o różnych zawartościach i długościach. Działa
#
# def usuwanie(lista):
#   for element in lista:
#     if element>60:
#       lista.remove(element)
#   return lista
# lista=[13, 23, 37, 99, 0]
# print(f"{lista}, po modyfikacji: {usuwanie(lista)}")
# lista_2=[15,1,5,7,87,57]
# print(f"{lista_2}, po modyfikacji: {usuwanie(lista_2)}")
# lista_3=[60, 93, 38]
# print(f"{lista_3}, po modyfikacji: {usuwanie(lista_3)}")

##ZADANIE 2
#Napisz funkcję, która zlicza i zwraca liczbę cyfr w przekazanym jako argument
#stringu. Nie korzystaj z polecenia len(). Zaprezentuj działanie funkcji na
#trzech różnych stringach o różnych zawartościach i długościach.
#Działa, lecz podany jest jeden string.
#
# def zlicz(tekst):
#     x = 0
#     cyfry=['0','1','2','3','4','5','6','7','8','9']
#     for l in tekst:
#         if l in cyfry:
#             x+=1
#     return(x)
# print('Oryginalny tekst: dywizjon 303')
# print('ilość cyfr w tekście wynosi',zlicz('dywizjon 303'))
#
# print('Oryginalny tekst: 500 dni i 2345 godzin')
# print('ilość cyfr w tekście wynosi',zlicz('500 dni i 2345 godzin'))
#
# str=input("Podaj zdanie z cyframi: ")
# print("Ilość cyfr w tym zdaniu to: ", zlicz(str))

##ZADANIE 3
#Napisz funkcję porównującą podobny tekst np. "Konstantynopol" oraz "Konntaftynolol"
#i zwraca jako string elementy, które są takie same w obu stringach. Teksty powinny
#być równej długości. Jeśli nie są, powinien pojawić się stosowny monit.
#Zaprezentuj działanie funkcji na trzech różnych stringach
#(o różnych zawartościach i długościach).
#
# def porownaj(lista1,lista2):
#     te_same=[]
#     if len(lista1)!=len(lista2):
#         return "Teksty nie są równej długości!!!"
#     else:
#         for i in range(len(lista1)):
#             if lista1[i]==lista2[i]:
#                 te_same.append(lista1[i])
#         return "".join(te_same)
#
# slowo1 = input("Podaj pierwsze slowo: ")
# slowo2 = input("Podaj drugie slowo: ")
# print("Elementy takie same w obu stringach: ", porownaj(slowo1,slowo2))
#
# #Druga wersja
# def porownaj(lista1,lista2):
#     te_same=[]
#     if len(lista1)!=len(lista2):
#         return "Teksty nie są równej długości!!!"
#     else:
#         for i in range(len(lista1)):
#             if lista1[i]==lista2[i]:
#                 te_same.append(lista1[i])
#         return "".join(te_same)
#
# slowo1 = "kot"
# slowo2 = "Konstantynopol"
# print("Elementy takie same w obu stringach(kot, konstantynopol): ", porownaj(slowo1,slowo2))
# slowo11= "konstantynopol"
# slowo12= "kpostantjnhfpo"
# print("Elementy takie same w obu stringach(konstantynopol, konstantynolol): ", porownaj(slowo11,slowo12))
# slowo111= "konstantynopol"
# slowo112= "konstantynopol"
# print("Elementy takie same w obu stringach(konstantynopol, konstantynopol): ", porownaj(slowo111,slowo112))
#
# #ZADANIE 4
# Napisz funkcję, która symuluje rzut monetą. Niech liczba rzutów do wykonania
# będzie podana przez użytkownika (przekazana jako argument). Funkcja powinna
# zwracać listę stringów (orzeł lub reszka). Działa
#
# import random
# def rzut_moneta(argument):
#     list=[]
#     for i in range(argument):
#         list.append(random.randint(1,2))
#     for i in range(len(list)):
#         if list[i] == 1:
#             list[i] = 'orzeł'
#         elif list[i] == 2:
#             list[i] ='reszka'
#     return list
# argument=int(input("Podaj liczbę rzutów: "))
# print(rzut_moneta(argument))
#
# #Symulacja rzutu kostką
# import random
# def rzut_kostka(argument):
#     lista_int=[]
#     for i in range(argument):
#         lista_int.append(random.randint(1,6))
#     return lista_int
# argument=int(input("Podaj liczbę: "))
# print(rzut_kostka(argument))

##ZADANIE 5
#Wymiana spacji na znak
#Napisz funkcję, która w argumencie przyjmie dowolne zdanie (przekazane jako string),
#a następnie zamieni wszystkie występujące w nim spacje na znak podkreślenia "_".
#Funkcja powinna zwracać zmodyfikowanego stringa. Zaprezentuj działanie funkcji
#dla trzech różnych argumentów wejściowych. Działa
#
# def podloga(x):
#     string = list(x)
#     for i in range(len(string)):
#         if string[i]==" ":
#             string[i]="_"
#     nowy_string=" "
#     for i in string:
#         nowy_string+=i
#     return nowy_string
# print(podloga('śmietana, kefir, i dwa banany'))
# print(podloga('jeden, dwa, trzy'))
# print(podloga('daj mnie trzy ananasy'))

##ZADANIE 6
#Napisz funkcję, która pobiera słowo w języku polskim a zwraca to samo słowo w
#dowolnym innym języku. Jeśli podane słowo nie jest znane programowi, funkcja
#powinna zwracać pustego stringa. Program powinien wykorzystywać słowniki.
#Zaprezentuj działanie funkcji na trzech różnych stringach. Działa
#
# slownik={'kot':'Mačka','samochód':'કાર','książka':'पुस्तक','telefon':'電話'}
# def tlumacz(słowo):
#     if słowo in slownik:
#         return slownik[słowo]
#     else:
#         return " "
# print('kot')
# print(tlumacz('kot'))
# print('płot')
# print(tlumacz('płot'))
# print('książka')
# print(tlumacz('książka'))

##ZADANIE 7
#Liczba samogłosek w stringu
#Napisz funkcję, która pobiera stringa oraz zwraca liczbę samogłosek w tym stringu.
#Zaprezentuj działanie funkcji na trzech różnych stringach o różnych zawartościach
#i długościach. Działa
#
# def ile_samoglosek(lancuch):
#     tyle=0
#     for i in lancuch:
#         if i in 'aeuiyoąęó':
#             tyle+=1
#     return tyle
# print('takich jak ja i ty')
# print(ile_samoglosek('takich jak ja i ty'))
# print('nie znają nawet karaiby')
# print(ile_samoglosek('nie znają nawet karaiby'))
# print('i to jest piękne a także')
# print(ile_samoglosek('i to jest piękne a także'))

##ZADANIE 8
#Odwracanie łańcuchu znaków
#Napisz funkcję, która odwraca łańcuch znaków np. “znaków” zamienia na “wókanz”.
#Funkcja ma pobierać stringa i zwracać jego odwróconą wersję. Zaprezentuj działanie
#funkcji na trzech różnych stringach o różnych zawartościach i długościach.
#Nie korzystaj z lista[:-1] oraz reverse.
#
# def odwrocenie(lancuch):
#   nowy_lancuch=""
#   for i in range(1,len(lancuch)+1):
#     nowy_lancuch+=lancuch[-i]
#   return nowy_lancuch
# for i in range(0,3):
#   lancuch=input("Podaj łańcuch znaków do odwrócenia: ")
#   print(f"Do odwrócenia: {lancuch}, {odwrocenie(lancuch)}")

##ZADANIE 9
#Wymiana miejscami pierwszej i ostatniej listy
#Napisz funkcję, która pobiera łańcuch znaków. Wymień miejscami pierwszą i ostatnią
#literę. Funkcja ma pobierać stringa i zwracać jego zmodyfikowaną wersję.
#Zaprezentuj działanie funkcji na trzech różnych stringach
#(o różnych zawartościach i długościach). Działa
#
# def pierwsi_ostatnimi(x):
#     return x[-1]+x[1:-1]+x[0]
# print('Ignacy Daszyński')
# print(pierwsi_ostatnimi('Ignacy Daszyński'))
#
# print('codziennie budze się')
# print(pierwsi_ostatnimi('codziennie budze się'))
#
# print('z uśmiechem')
# print(pierwsi_ostatnimi('z uśmiechem'))

##ZADANIE 10
#Zwracanie listy bez parzystych indeksów
# #Napisz funkcję, która wczytuje listę z liczbami całkowitymi oraz zwraca tę samą
# #listę, ale pozbawioną liczb o parzystych indeksach w liście. Zaprezentuj działanie
# #funkcji na trzech różnych listach (o różnych zawartościach i długościach). Działa
#
# def usuń_parzaki(lista):
#     kopia=lista
#     for i in kopia:
#         if i%2 == 0:
#             kopia.remove(i)
#     return kopia
#
# l1=[1,2,3,4,5,6]
# l2=[4,78,35,3,2,5,7,923,3]
# l3=[0,0,0,3,2,1]
# print(l1)
# print(usuń_parzaki(l1))
# print(l2)
# print(usuń_parzaki(l2))
# print(l3)
# print(usuń_parzaki(l3))
#
# #Poniższy kod wypisuje listę z parzystymi indeksami bez nieparzystych indeksów
# l=[1,2,3,4,5,6,7,8]
# def usuń_parzaki_indeksiaki(l):
#     m=l
#     usuwaki=[]
#     for i in range(len(l)):
#         if i%2 != 1:
#             usuwaki.append(l[i])
#     for i in usuwaki:
#         m.remove(i)
#     return m
# print(l)
# print(usuń_parzaki_indeksiaki(l))

##ZADANIE 11
#Napisz funkcję, która pobiera liczbę elementów listy oraz zwraca listę o zadanej
#długości wypełnioną losowymi liczbami rzeczywistymi z zakresu od 3 do 5.
#Zaprezentuj działanie funkcji na trzech różnych liczbach elementów. Działa
#
# import random
# def niewielkie_rzeczywiste(liczba):
#     lista=[]
#     for i in range(liczba):
#         lista.append(random.randint(3,4)+random.random())
#     return lista
# print(niewielkie_rzeczywiste(5))
# print(niewielkie_rzeczywiste(3))
# print(niewielkie_rzeczywiste(21))

##ZADANIE 12
#Stworzenie słowa
#Napisz funkcję, który losuje zadaną przez użytkownika (i przekazaną do niej
#jako argument) liczbę liter. Niech zwraca stringa z powstałym słowem.
#Zaprezentuj działanie funkcji uruchamiając ją 3 razy. Działa
#
# import random
# alfabet='qwertyuiopsdfghjklzxcvbnmaęóąśłżćń'
# def uloz_slowo(liczba):
#     ulozone=''
#     for i in range(liczba):
#         ulozone+=random.choice(alfabet)
#     return ulozone
# liczba=int(input("Podaj liczbę: "))
# print(uloz_slowo(liczba))
#
# liczba1=12
# liczba2=25
# liczba3=30
#
# print(uloz_slowo(liczba1))
# print(uloz_slowo(liczba2))
# print(uloz_slowo(liczba3))
