# wyniki=[["Adam", 1000], ["Kasia", 3], ["Piotr", 2345], ["Agata", 687]]
# print(wyniki[0][1])
# print(wyniki[0])

# wyniki=[('Adam', 1000), ('Kasia', 3), ('Piotr', 2345), ('Agata', 687)]
# for wiersz in wyniki:
#     for kolumna in wiersz:
#         print(kolumna,end=" ")
#     print()

# wyniki=[("Adam", 1000), ("Kasia", 3), ("Piotr", 2345), ("Agata", 687)]
# for i in range(len(wyniki)):
#     for j in range(len(wyniki[i])):
#         print(wyniki[i][j], end=" ")
#     print()

# slownik={1:"jeden", 2:"dwa", 3:"trzy", 4:"cztery"}
# print(slownik[1])

# slownik={"jeden":"one", "dwa":"two", "trzy":"three", "cztery":"four"}
# # print(slownik["dwa"])
# print("Podaj nowe hasło:")
# haslo=input()
# print("Podaj definicję nowego hasła:")
# definicja=input()
# slownik[haslo]=definicja
# print(slownik)

# slownik={"jeden":"one", "dwa":"two", "trzy":"three", "cztery":"four"}
# print("Które hasło należy przedefiniować?")
# haslo=input()
# print("Podaj nową definicję hasła:")
# definicja=input()
# slownik[haslo]=definicja
# print(slownik)

# slownik={"jeden":"one", "dwa":"two", "trzy":"three", "cztery":"four"}
# print("Które hasło należy usunąć?")
# haslo=input()
# del(slownik[haslo])
# print(slownik)

# slownik={"jeden":"one", "dwa":"two", "trzy":"three", "cztery":"four"}
# if "dwa" in slownik:
#     print("Znam to hasło")
# else:
#     print("Nie znam tego hasła")

# lista=[1,2,3]
# print("Podaj element:")
# element=int(input())
# if element in lista:
#     print("Ten element jest w liście")
# else:
#     print("Tego elementu nie ma w liście")

# slownik={"jeden":"one", "dwa":"two", "trzy":"three", "cztery":"four"}
# print(slownik.keys())
# print(slownik.values())

# ZADANIE 1
# lista=[[1,2,3],[23,45,67],[456,234,900],[29,45,768]]
# najwieksza=lista[0][0]
# for i in range(len(lista)):
#     for j in range(len(lista[i])):
#         if lista[i][j]>najwieksza:
#             najwieksza=lista[i][j]
# print(najwieksza)

# ZADANIE 2
# lista = [1,2,4,56,11,456,234,987,10,90]
# print("Podaj element:")
# element=int(input())
# lista.append(element)
# print(lista)

# ZADANIE 3
# lista = [1,2,4,56,11,456,234,987,10,90]
# suma = 0
# for i in range(len(lista)):
#     suma+=lista[i]
# print(suma)
