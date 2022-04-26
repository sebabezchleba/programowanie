# liczba=7
#
# def dzialanie():
#     liczba=5
#
# print(liczba)


# def rysujProstakat (dlugosc, szerokosc, element=4):
#     for i in range(dlugosc):
#         for j in range(szerokosc):
#             print(element, end='')
#         print()
#
# rysujProstakat(2,3)
# rysujProstakat(2,3, '*')


# def gwiazdki(liczbaGwiazdek):
#     if liczbaGwiazdek > 0:
#         print("*")
#         gwiazdki(liczbaGwiazdek-1)
# gwiazdki(5)


# lista=[1,2,3,4,5]
# def sumowanie(listaLiczb):
#     if len(listaLiczb)>0:
#         return listaLiczb[0]+sumowanie(listaLiczb[1:])
#     else:
#         return 0
#
# wynik=sumowanie(lista)
# print(wynik)
#
#
# lista=[1,2,3,4,5]
# def mnozenie(listaLiczb):
#     if len(listaLiczb)>0:
#         return listaLiczb[0]*mnozenie(listaLiczb[1:])
#     else:
#         return 1
#
# wynik=mnozenie(lista)
# print(wynik)
#
#
# ZADANIE 1
# lista=[1,2,3,4,5]
# def ostatni(lista):
#     if len(lista)>1:
#         return ostatni(lista[1:])
#     else:
#         return lista[0]
#
# wynik=ostatni(lista)
# print(wynik)


# ZADANIE 4
# def dlugosc(lista):
#     if len(lista)>0: #albo "if lista:"
#         return 1 + dlugosc(lista[1:])
#     else:
#         return 0
#
# lista=[1,2,3,4,5,-3,12]
# wynik=dlugosc(lista)
# print(wynik)



# ZADANIE 3
# def maksimum(lista, zapamietana):
#     if len(lista)>0:
#         if lista[0]>zapamietana:
#             zapamietana=lista[0]
#         return maksimum(lista[1:], zapamietana)
#     else:
#         return zapamietana
#
# lista=[1,2,3,4,5, -3, 12]
# wynik=maksimum(lista,lista[0])
# print(wynik)
#
# ###
# def minimum(lista, zapamietana):
#     if len(lista)>0:
#         if lista[0]<zapamietana:
#             zapamietana=lista[0]
#         return minimum(lista[1:],zapamietana)
#     else:
#         return zapamietana
#
# lista=[1,2,3,4,5, -3, 12]
# wynik1=minimum(lista,lista[0])
# print(wynik1)


#ZADANIE 6
# def jest(lista, sprawdzana):
#     if len(lista)>0:
#         if lista[0] == sprawdzana:
#             return "tak"
#         else:
#             return jest(lista[1:], sprawdzana)
#     else:
#         return "nie"
#
# lista=[1,2,3,4,5,-3,12]
# wynik=jest(lista, 7)
# print(wynik)


#ZADANIE 2
# def ogon(lista):
#   if len(lista) > 1:
#       return [lista[1]]+ogon(lista[1:])
#   else:
#       return []
#
# lista=[1,2,3,4,5,6, "a", "c"]
#
# print("Ogon:",ogon(lista))


#ZADANIE 5
# ##Napisz funkcje nta(x), która zwraca n-ty element listy (rekurencyjnie)
# def nta(lista,n):
#    if len(lista)>n:
#        if n==0:
#            return lista[0]
#        return nta(lista[1:],n-1)
#
#    else:
#        return "Lista nie ma tylu elementów"
#
# lista=[1,2,32]
# print("Który element listy wyświetlić?")
# n=int(input())
# print(nta(lista,n))


#ZADANIE 7
##Napisz funkcję, która wyznacza n-tą (n jest liczba naturalną) potęgę zadanej
##liczby x (rekurencyjnie)
# def ntaPotega(x,n):
#    if n==0:
#        return 1
#    if n>=1:
#        return x * ntaPotega(x,n-1)
#
#
# print("Podaj liczbę x:")
# x=int(input())
# print("Podaj liczbę naturalną (potęgę):")
# n=int(input())
# print(ntaPotega(x,n))


####ZADANIE 8
# def silnia(x):
#     if x<0:
#         return "nie może być silni dla ujemnych"
#     if x==0:
#         return 1
#     if x==1:
#         return 1
#     if x>1:
#         return x * silnia(x-1)
#
# liczba = int(input("Podaj liczbę, której silnie chcesz wyliczyć: "))
# wynik = silnia(liczba)
# print(wynik)


######alternatywnie
# def silnia(n):
#     if n > 1:
#         return n*silnia(n-1)
#     return 1
#
# liczba = int(input("Podaj liczbę, której silnie chcesz wyliczyć: "))
# wynik = silnia(liczba)
# print(wynik)

####zadanie 9
# def dodawanie(x,y):
#     suma=x+y
#     return suma
#
# print(dodawanie(1,2))
