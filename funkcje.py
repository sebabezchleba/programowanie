# def wyznacz_kwadrat(liczba):
#     ####
#     # Funkcja pobiera liczbę i oblicza jej kwadrat
#     ####
#     return liczba**2
#
# print("Wpisz cyfrę")
# liczba = int(input())
# obliczony_kwadrat=wyznacz_kwadrat(liczba)
#
# print(obliczony_kwadrat)

# def dodawanie(liczba1, liczba2):
#     suma=liczba1+liczba2
#     return suma
# def mnozenie(liczba1, liczba2):
#     iloczyn=liczba1*liczba2
#     return iloczyn
#
# pierwsza = int(input("Podaj liczbę: "))
# druga = int(input("Podaj liczbę: "))
# wynik=mnozenie(pierwsza,druga)
# wynik1=dodawanie(pierwsza,druga)
# print(f"Wynikiem dodawania jest: {wynik1}")
# print(f"Wynikiem mnożenia jest: {wynik}")
#
# def dziwne_dzielenie(liczba1):
#     suma = liczba1 + liczba1
#     kwadrat = suma **2
#     wynik=kwadrat -1
#     return wynik
#
# pierwsza = float(input("Podaj liczbę "))
# wynik = dziwne_dzielenie(pierwsza)
# print("Wynikiem skomplikowanego dzialania jest: ", wynik)
# print("Kwadratem podanych liczb jest: ", kwadrat)
# #### nie ma prawa działać

# ZADANIE 1
# def odejmowanie(liczba1, liczba2):
#     roznica=liczba1-liczba2
#     return roznica
#
# pierwsza=int(input("Podaj liczbę: "))
# druga=int(input("Podaj liczbę: "))
# print(odejmowanie(pierwsza, druga))

#ZADANIE 2
# def ostatni(lista):
#     ostatni=lista[-1]
#     return ostatni
# lista=[1,2,3,4,5,6,7,8,9]
# print(ostatni(lista))

#ZADANIE 3
# def ogon(lista):
#     ogon=lista[1:]
#     return ogon
# lista=[1,2,3,4,5,6,7,8,9]
# print(ogon(lista))

#ZADANIE 4
# def maksimum(lista):
#     maks=lista[0]
#     for liczba in lista:
#         if liczba>maks:
#             maks=liczba
#     return maks
#
#
# def minimum(lista):
#     min=lista[0]
#     for liczba in lista:
#         if liczba<min:
#             min=liczba
#     return min
#
# lista1=[6719,55555555555,111111111111111111,789,234,2137]
# print(maksimum(lista1))
# print(minimum(lista1))

#ZADANIE 5
# def dlugosc(lista):
#     ilosc=0
#     for liczba in lista:
#         ilosc+=1
#     return ilosc
#
# lista1=[1,2,3,4,5,6,7,8,9]
# print(dlugosc(lista1))

#ZADANIE 6
# def nta(lista):
#     podaj=int(input())
#     nty=lista[podaj]
#     return nty
#
# #######
# ## ogarnij to
# #######
#
# # lista1=[]
# # while True:
# #     wybor=input()
# #     if wybor=="a":
# #         element=int(input())
# #         lista1.append(element)
# #     if wybor=="b":
# #         break
#
# lista1=[1,2,3]
# print(nta(lista1))

#ZADANIE 10
def kwadrat(liczba):
    kwa=liczba**2
    retur kwa

def szescian(liczba):
    szes=liczba**3
    return szes

while True:
    podaj=input("Podaj liczbę: ")
    print("Jeśli chesz sprawdzić kwadrat wciśnij \"k\"")
    print("Jeśli chesz sprawdzić sześcian wciśnij \"s\"")
    wybor=input()
    if wybor=="k":
        print(kwadrat(podaj))
    if wybor=="s":
        print(szescian(podaj))
    else:
        print("Nie rozpoznano.")
