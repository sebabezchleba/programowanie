#Stworzenie słowa
#Napisz funkcję, który losuje zadaną przez użytkownika (i przekazaną do niej
#jako argument) liczbę liter. Niech zwraca stringa z powstałym słowem.
#Zaprezentuj działanie funkcji uruchamiając ją 3 razy. Działa

import random
alfabet='qwertyuiopsdfghjklzxcvbnma'
def uloz_slowo(liczba):
    ulozone=''
    for i in range(liczba):
        ulozone+=random.choice(alfabet)
    return ulozone
liczba=int(input("Podaj liczbę: "))
print(uloz_slowo(liczba))
