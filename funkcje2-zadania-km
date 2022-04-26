#ZADANIE1
lista_jakas = ['adam', 'bodzio', 'cezary', 'darek']
lista_pusta = []


def znajdzOstatni_rek(lista):
    '''
    Funkcja rekurencyjnie wyszukuje ostatni element listy.
    Jeżeli lista jest pusta - oddany zostaje ERROR.
    '''
    if lista == []:
        return 'ERROR: lista nie ma elementów'
    elif len(lista) == 1:
        return lista[0]
    else:
        return znajdzOstatni_rek(lista[1:])


print(znajdzOstatni_rek(lista_jakas))
print(znajdzOstatni_rek(lista_pusta))

#ZADANIE2
lista_jakas = ['adam', 'bodzio', 'cezary', 'darek']
lista_pusta = []
lista_jeden = [1]


def ogon(lista):
    '''
    Funkcja rekurencyjnie zapisuje wszystkie elementy listy poza pierwszym.
    Jeżeli lista nie ma elementów oddany zostaje ERROR.
    '''
    if lista == []:
        return 'ERROR: lista nie ma elementów.'
    elif len(lista) == 1:
        return 'Nie ma tutaj nic'
    elif len(lista) == 2:
        return lista[1]
    else:
        return lista[1] + ', ' + ogon(lista[1:])


print(ogon(lista_jakas))
print(ogon(lista_pusta))
print(ogon(lista_jeden))

#ZADANIE3
import random

losowe = []

for _ in range(10):
    losowe.append(random.randint(1, 100))

print(losowe)


def max_rek(lista):
    '''
    Funkcja rekurencyjnie wyszukuje największy element listy.
    Jeżeli lista jest pusta oddany zostaje error.
    '''
    if lista == []:
        return 'ERROR'
    else:
        if len(lista) == 1:
            return lista[0]
        else:
            if lista[0] > lista[1]:
                lista[1] = lista[0]
                return max_rek(lista[1:])
            else:
                return max_rek(lista[1:])


print(max_rek(losowe))
print(max_rek([]))
print(max_rek([losowe[0]]))

#ZADANIE4
lista_jakas = ['adam', 'bodzio', 'cezary', 'darek']

lista_wprow = []
n = int(input('Ile emelentów ma mieć lista: '))
for _ in range(1, n+1):
    lista_wprow.append(_)


def dlugosc(lista):
    '''
    Funkcja rekurencyjnie liczy długość listy i oddaje wynik.
    '''
    if lista == []:
        return 0
    else:
        return 1 + dlugosc(lista[1:])


print(dlugosc(lista_jakas))
print(dlugosc([]))
print(dlugosc([1, 2]))
print(dlugosc(lista_wprow))

#ZADANIE5
lista_jakas = ['adam', 'bodzio', 'cezary', 'darek']

n = int(input('Który element listy oddać: '))


def nta(lista, szukana=n):
    '''
    Funkcja rekurencyjnie wyszukuje rządany element listy.
    Jeżeli funkcja nie ma wystarczająco elementów - odda ERROR.
    '''
    if len(lista) < szukana or szukana == 0:
        return 'ERROR'
    elif len(lista) == szukana:
        return lista[-1]
    else:
        return nta(lista[:-1])


print(nta(lista_jakas))

#ZADANIE6
lista_jakas = ['adam', 'bodzio', 'cezary', 'darek']

znajdz = input('Wpisz element, który chcesz sprawdzić: ')


def sprawdzCzyJest_rek(lista, element=znajdz):
    '''
    Lista rekurencyjnie sprawdza, czy dany element znajduje się w liście.
    Lista oddaje string 'Tak' albo 'Nie'.
    '''
    if lista == []:
        return 'Nie'
    elif element == lista[0]:
        return 'Tak'
    else:
        return sprawdzCzyJest_rek(lista[1:])


print(sprawdzCzyJest_rek(lista_jakas))

#ZADANIE7
podstawa = float(input('Jaką liczbę chcesz spotęgować: '))
potega = int(input('Do jakiej potęgi chcesz podnieść liczbę: '))


def potegowanie_rek(power=potega, base=podstawa):
    '''
    Funkcja rekurencyjnie podnosi liczbę do danej potęgi i oddaje wynik.
    '''
    if power == 0:
        return 1
    elif power > 0:
        return base*potegowanie_rek(power-1)
    else:
        return (1/base)*potegowanie_rek(power+1)


print(potegowanie_rek())

#ZADANIE8
liczba = int(input('Z jakiej liczby chcesz silnię: '))


def silnia_rek(number=liczba):
    '''
    Funkcja oddaje silnię z podanej liczby.
    Jeżeli podana liczba jest ujemna:
    - funkcja oddaje 'ERROR'.
    '''
    if number < 0:
        return 'ERROR'
    elif number == 0:
        return 1
    else:
        return number*silnia_rek(number-1)


print(silnia_rek())

