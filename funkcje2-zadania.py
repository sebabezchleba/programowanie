# print("Podaj numer telefonu: ")
# telefon=input()
# if telefon.isalpha() is True:
#     print("Ciąg składa się tylko z liter.")
# else:
#     print("Ciąg nie składa się tylko z liter.")
# nowy_numer=telefon.replace("-", "").replace(" ", "")
# print(nowy_numer)
# if nowy_numer.isnumeric() is True:
#     print("tak")


# def porownaj(wyraz1,wyraz2):
#     if len(wyraz1)!=len(wyraz2):
#         return "błąd, ma być równa długość"
#     else:
#         if wyraz1 == wyraz2:
#             return "wyrazy takie same"
#         for i in range(len(wyraz1)):
#             if wyraz1[i]!=wyraz2[i]:
#                 print("różnica na pozycji ", i+1)
#         return "wyrazy róźnią się"
# print(porownaj("konstantynopol", "konntaftynolol"))

# numer=input("Podaj:")
# cyfry=[]
# numer_cyfry=""
#
# for znak in numer:
#     if znak.isdigit():
#         cyfry.append(znak)
# numer_cyfry="".join(cyfry)
#
# poprawny=[]
# for i in range(0,len(numer_cyfry),3):
#     poprawny.append(numer_cyfry[i:i+3])
#
# for trojka in poprawny:
#     print(trojka, end=" ")

# Zadanie 1
# lista=[1,2,3,4,5]
# def ostatni(listaLiczb):
#     if len(listaLiczb)>1:
#         return ostatni(listaLiczb[1:])
#     else:
#         return listaLiczb[0]
#
# wynik=ostatni(lista)
# print(wynik)


# Zadanie 2
# def ogon(lista):
#     if len(lista)!=lista[0]:
#         return lista[1:]
#     else:
#         return ogon(lista[1:])
#
# lista=[1,2,3,4,5,1,2,0,1]
# wynik=ogon(lista)
# print(wynik)

# Zadanie 3
# def maksymalna(listaLiczb, zapamietana):
#     if len(listaLiczb)>0:
#         if listaLiczb[0]>zapamietana:
#             zapamietana=listaLiczb[0]
#         return maksymalna(listaLiczb[1:], zapamietana)
#     else:
#         return zapamietana
#
# lista=[1,2,3,4,5]
# wynik=maksymalna(lista, lista[0])
# print(wynik)
#
# Zadanie 4
# def dlugosc(listaLiczb):
#     if listaLiczb:
#         return 1+dlugosc(listaLiczb[1:])
#     else:
#         return 0
#
# lista=[1,2,3,4,5]
# wynik=dlugosc(lista)
# print(wynik)


# Zadanie 5
# def nta(lista, n):
#     if len(lista)>n:
#         if n==0:
#             return lista[0]
#         return nta(lista[1:], n-1)
#     else:
#         return "Lista nie ma tylu elementów"
# listadana=[1,2,3,4,5,1,3,8,9,10]
# print("Który element listy chcesz zobaczyć?")
# dana = int(input())
# wynik=nta(listadana, dana)
# print(wynik)


# Zadanie 6
# def czynaliscie(listaLiczb, do_sprawdzenia):
#     if len(listaLiczb)>0:
#         if listaLiczb[0] == do_sprawdzenia:
#             return "TAK"
#         else:
#             return czynaliscie(listaLiczb[1:], do_sprawdzenia)
#     else:
#         return "NIE"
#
# lista=[1,2,3,4,5]
# wynik=czynaliscie(lista, 5)
# print(wynik)


# Zadanie 7
# def potegowanie(liczba, potega):
#     if potega==1:
#         return liczba
#     else:
#         return liczba*potegowanie(liczba,potega-1)
#
# print("Podaj liczbę, którą chcesz potęgować")
# podanaliczba=int(input())
# print("Podaj liczbę, ile chcesz potęgować")
# podanapotega=int(input())
# wynik=potegowanie(podanaliczba,podanapotega)
# print("Wynikiem jest:", wynik)



# Zadanie 8
# def silnia(liczba):
#     if liczba==1:
#         return liczba
#     elif liczba<0:
#         return "Silnia nie istnieje dla liczb ujemnych"
#     elif liczba==0:
#         return "Silnia z 0 wynosi 1"
#     else:
#         return liczba*silnia(liczba-1)
#
# print("Jakiej liczby chcesz silnię?")
# podanaliczba=int(input())
# wynik=silnia(podanaliczba)
# print("Wynikiem jest:", wynik)



# Zadanie 9
# def sumowanie(liczba1, liczba2):
#     print(liczba1+liczba2)
# sumowanie(7,9)



# Zadanie 10
# def sumowanie(liczba1, liczba2):
#     return liczba1+liczba2
#
# print("Jakie liczby chcesz sumować?")
# podana1 = int(input())
# podana2 = int(input())
# wynik = sumowanie(podana1, podana2)
# print(wynik)



# Zadanie 11
# def dodawanie(liczba1, liczba2):
#     print(liczba1+liczba2)
#
# def odejmowanie(liczba1, liczba2):
#     print(liczba1-liczba2)
#
# def mnozenie(liczba1, liczba2):
#     print(liczba1*liczba2)
#
# def dzielenie(liczba1, liczba2):
#     print(liczba1/liczba2)
#
# print("Kalkulator\n")
# print("Jakie działanie chcesz wykonać? Dodawanie, odejmowanie, mnożenie czy dzielenie?")
# dzialanie = input()
# print("Jakie liczby chcesz wykorzystać?")
# podana1 = int(input())
# podana2 = int(input())
# if dzialanie == "dodawanie":
#     dodawanie(podana1, podana2)
# elif dzialanie == "odejmowanie":
#     odejmowanie(podana1, podana2)
# elif dzialanie == "mnożenie":
#     mnozenie(podana1, podana2)
# elif dzialanie == "dzielenie":
#     dzielenie(podana1, podana2)
# else:
#     print("Nie wykonam takiego działania!")



# Zadanie 12
# def sprawdzian(wynik):
#     print("Jakie liczby chcesz sprawdzić?")
#     liczba1 = int(input())
#     liczba2 = int(input())
#     if liczba1 == liczba2:
#         return "Liczby są sobie równe!"
#     else:
#         if liczba1>liczba2:
#             wynik = liczba1-liczba2
#             print("Różnica między nimi wynosi:", end=' ')
#             return wynik
#         elif liczba1<liczba2:
#             wynik = liczba2-liczba1
#             print("Różnica między nimi wynosi:", end=' ')
#             return wynik
#
# aktualnywynik=0
# print(sprawdzian(aktualnywynik))



# Zadanie 13
# def laczenie(lista1, lista2):
#     for i in range(len(lista1)-1):
#         if lista1[i] != lista1[i+1]:
#             lista2.append(lista1[i])
#     lista2.append(lista1[-1])
#     return lista2
#
# przykladowalista1 = [1,2,4,3,"a","b","c","f"]
# przykladowalista2 = [4,1,"f",5,9,10,"g"]
# print(laczenie(przykladowalista1, przykladowalista2))


# Zadanie 14
# def laczenie(lista1, lista2):
#     for i in range(len(lista1)-1):
#         if lista1[i] != lista1[i+1]:
#             lista2.append(lista1[i])
#     lista2.append(lista1[-1])
#     lista3=[]
#     for j in lista2:
#         if j not in lista3:
#             lista3.append(j)
#     return lista3
#
# przykladowalista1 = [1,2,4,3,"a","b","c","f"]
# przykladowalista2 = [4,1,"f",5,9,10,"g"]
# print(laczenie(przykladowalista1, przykladowalista2))



# Zadanie 15
# import math
# def pierwiastek(liczba):
#     wynik = math.sqrt(liczba)
#     print("Wynikiem zaokrąglonym do dwóch przecinków jest:", round(wynik,2))
#     if wynik%2==0:
#         return "Liczba jest parzysta"
#     else:
#         return "Liczba jest nieparzysta"
#
#
# print("Jakiej liczby chesz pierwiastek?")
# podana = int(input())
# print(pierwiastek(podana))



# Zadanie 16
# def dlugoscimax(lista):
#     suma = 0
#     for element in lista:
#         suma = suma+1
#     najwieksza = lista[0]
#     for element in lista:
#         if element > najwieksza:
#             najwieksza = element
#     print("Długość listy wynosi", suma)
#     print("Największym elementem listy jest:", end=' ')
#     return najwieksza
#
# podanalista = [1,5,8,2,0,3,45,16,2]
# print(dlugoscimax(podanalista))


def rownosc():
  print("podaj dwie liczby do porownania")
  pierwsza = int(input())
  druga = int(input())
  if pierwsza == druga:
    return "Takie same"
  else:
    print("różnica wynosi:", abs((pierwsza-druga)))
    
rownosc()
