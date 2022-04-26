import random
####Napisz funkcję odejmowanie(x,y), która odejmuje od siebie podane argumenty,
##def odejmowanie(x,y):
##    roznica=x-y
##    return roznica
##
##print("Podaj pierwszą liczbę:")
##x=int(input())
##print("Podaj drugą liczbę:")
##y=int(input())
##roznica=odejmowanie(x,y)
##print("Różnica wynosi:", roznica)

####Napisz funkcję ostatni(lista), która zwraca ostatni element listy,
##def ostatni(lista):
##    return lista[-1]
##lista=[]
##for i in range(0,10):
##    n=random.randint(0,9)
##    lista.append(n)
##print("Lista:", lista)
##print("Ostatni element:",ostatni(lista))
##
####Napisz funkcję ogon(lista), która zwraca wszystko poza pierwszym elementem
####listy,
##def ogon(lista):
##    return lista[1:]
##print("Ogon:",ogon(lista))
##
####Napisz funkcję dlugosc(x), która zwraca wielkość listy (bez wykorzystania
####funkcji len),
##def dlugosc(x):
##    licz=0
##    for i in x:
##        licz+=1
##    return licz
##print("Długość:",dlugosc(lista))
##
####Napisz funkcję maksimum(lista), i minimum(lista), które zwracają
####maksymalny i minimalny element listy (bez wykorzystania funkcji min i
####max). Jeśli chcesz skorzystać z len() skorzystaj z funkcji dlugosc() z
####poprzedniego zadania,
##def maksimum(lista):
##    najwieksza=lista[0]
##    for i in range(dlugosc(lista)):
##        if lista[i]>najwieksza:
##            najwieksza=lista[i]
##    return najwieksza
##
##def minimum(lista):
##    najmniejsza=lista[0]
##    for i in range(dlugosc(lista)):
##        if lista[i]<najmniejsza:
##            najmniejsza=lista[i]
##    return najmniejsza
##print("Max:",maksimum(lista))
##print("Min:",minimum(lista))
##
####Napisz funkcję nta(lista,n), która zwraca n-ty element listy,
##def nta(lista,n):
##    length=dlugosc(lista)
##    if n>length:
##        return blad
##    else:
##        return lista[n]
##
##n=int(input())
##blad="Lista nie ma tylu elementów"
##print("Element", n, "listy:", nta(lista,n))

####Napisz funkcję alternatywa(x,y), która przyjmuje tylko 1 lub 0,
##def alternatywa(x,y):
##    if x>1 or y>1:
##        return "Musisz podać wartość 0 lub 1!"
##    if x==0 and y==0:
##        return "Alternatywa dla podanych wartości to 0"
##    else:
##        return "Alternatywa dla podanych wartości to 1"
##print("Podaj x:")
##x=int(input())
##print("Podaj y:")
##y=int(input())
##print(alternatywa(x,y))
##
####Napisz funkcję koniunkcja(x,y), która przyjmuje tylko 1 lub 0,
##def koniunkcja(x,y):
##    if x>1 or y>1:
##        return "Musisz podać wartość 0 lub 1!"
##    if x==1 and y==1:
##        return "Koniunkcja podanych wartości to 1"
##    else:
##        return "Koniunkcja podanych wartości to 0"
##
##print(koniunkcja(x,y))
##
####Napisz funkcję implikacja(x,y), która przyjmuje tylko 1 lub 0,
##def implikacja(x,y):
##    if x>1 or y>1:
##        return "Musisz podać wartość 0 lub 1!"
##    if x==1 and y==0:
##        return "Implikacja podanych wartości to 0"
##    else:
##        return "Implikacja podanych wartości to 1"
##
##print(implikacja(x,y))

####Napisz funkcję, która oblicza kwadrat lub sześcian podanej liczby
####(powinniśmy wybrać móc wybrać opcję)
##def kwadrat(x):
##    return x**2
##def szescian(x):
##    return x**3
##def decyzja(wybor):
##    if wybor==2:
##        return kwadrat(liczba)
##    elif wybor==3:
##        return szescian(liczba)
##    else:
##        return "Nie ma takiej możliwości"
##    
##print("Wpisz liczbę:")
##liczba=int(input())
##print("Wpisz 2, jeśli chcesz podnieść liczbę do kwadratu, lub 3, jeśli chcesz ją podnieść do sześcianu")
##wybor=int(input())
##print(decyzja(wybor))
##
####Napisz funkcję, pobiera numer dnia tygodnia (cyfra od 1 do 7) i zwraca nazwę
####danego dnia tygodnia
##def tydzien(x):
##    if x==1:
##        return "Poniedziałek"
##    elif x==2:
##        return "Wtorek"
##    elif x==3:
##        return "Środa"
##    elif x==4:
##        return "Czwartek"
##    elif x==5:
##        return "Piątek"
##    elif x==6:
##        return "Sobota"
##    elif x==7:
##        return "Niedziela"
##    else:
##        return "Tydzień nie ma tylu dni"
##
##print("Wpisz numer dnia tygodnia:")
##dzien=int(input())
##print(tydzien(dzien))

####Napisz funkcję gwiazdki(liczba), która wyświetla ciąg symboli ”*”, a liczba to
####liczba gwiazdek, które powinny pojawić się na ekranie
##def gwiazdki(liczba):
##    gw=""
##    for i in range(liczba):
##        gw+="*"
##    return gw
##print("Liczba gwiazdek:")
##liczba=int(input())
##print(gwiazdki(liczba))

####Napisz funkcję, która sprawdza parzystość podanej z klawiatury liczby
##def parzysta(liczba):
##    if liczba%2==0:
##        return "Liczba jest parzysta"
##    else:
##        return "Liczba jest nieparzysta"
##print("Podaj liczbę:")
##liczba=int(input())
##print(parzysta(liczba))
##
####Przygotuj funkcję, która sumuje liczby od 1 do X, gdzie X to liczba podana
####przez użytkownika.
##def sumowanie(x):
##    suma=0
##    for i in range(1,x+1):
##        suma+=i
##    return suma
##
##print("Podaj ostatnią liczbę do sumowania:")
##koniec=int(input())
##print(sumowanie(koniec))

##Napisz program losujący liczbę od 0 do 4. W zależności od wylosowanej liczby
##powinna zostać uruchomiona odpowiednia funkcja
##def los(n)
##    if n==0:
##        
##n=random.randint(0,4)

#zad16
def sprawdz_dol(x):
    if x>10:
        return "Podana liczba jest większa niż 10"
    else:
        return "Podana liczba jest mniejsza niż 10"

def sprawdz_gore(x):
    if x>100:
        return "Podana liczba jest większa niż 100"
    else:
        return "Podana liczba jest mniejsza niż 100"

def pierwiastkuj(x):
    return x**(0.5)





