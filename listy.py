# lista_cyfr_trzy = ["111", 3, "trzy", "three", "..."]
# print(f"Liczba elementów listy to: {len(lista_cyfr_trzy)}")

# lista_cyfr_trzy = ["111", 3, "trzy", "three", "..."]
# print("Różne oblicza cyfry trzy:")
# for i in range(len(lista_cyfr_trzy)):
#     print(lista_cyfr_trzy[i])


# lista_cyfr_trzy = ["111", 3, "trzy", "three", "..."]
# print("Różne oblicza cyfry trzy:")
# for cyfra in lista_cyfr_trzy:
#     print(cyfra)

# lista_cyfr_trzy = ["111", 3, "trzy", "three", "..."]
# print("Różne oblicza cyfry trzy:")
# for i in range(len(lista_cyfr_trzy)):
#     print(i, "element to:", lista_cyfr_trzy[i])

# lista_cyfr_trzy = ["111", 3, "trzy", "three", "..."]
# print(lista_cyfr_trzy[1:2])
# print(lista_cyfr_trzy[1:4])
# print(lista_cyfr_trzy[2:])
# print(lista_cyfr_trzy[:3])

# lista_liczb=[1,2,3]
# print("Podaj nową zawartość 0 elementu:")
# lista_liczb[0]=int(input())
# print(f"Nowa lista: {lista_liczb}")

# lista_liczb=[1,2,3]
# for i in range(len(lista_liczb)):
#     print(f"Podaj nową zawartość {i} elementu:")
#     lista_liczb[i]=input()
# print(f"Nowa lista: {lista_liczb}")

# lista_liczb=[1,2,3]
# for i in range(len(lista_liczb)):
#     print(f"Podaj nową zawartość {i+1} elementu:")
#     lista_liczb[i]=input()
# print(f"Nowa lista: {lista_liczb}")

# "nazwa_listy".append("element który ma zostać dodany")

# lista_liczb=[1,2,3]
# dodaj=input("Jaki element dodać?")
# # dodaj=int(input("Jaki element dodać?"))
# lista_liczb.append(dodaj)
# print(f"Nowa lista: {lista_liczb}")

# lista_liczb=[1,2,3]
# usun=int(input("Jaki element usunąć?"))
# lista_liczb.remove(usun)
# print(f"Nowa lista {lista_liczb}")

# lista_liczb=[1,2,3,2,3,4,2]
# for liczba in lista_liczb[:]:
#     if liczba==2:
#         lista_liczb.remove(liczba)
#         # print(lista_liczb)

# lista_liczb_pierwsza=[1,2,3,2,3,4,2]
# lista_liczb_druga=lista_liczb_pierwsza
# lista_liczb_pierwsza[0]=8
#
# print(lista_liczb_pierwsza)
# print(lista_liczb_druga)

# lista_liczb_pierwsza =[1,2,3,2,3,4,2]
# lista_liczb_druga=lista_liczb_pierwsza[:]
# lista_liczb_pierwsza[0]=8
#
# print(lista_liczb_pierwsza)
# print(lista_liczb_druga)

# wyniki_konkursu=[1000,3,2345,687]
# for wynik in wyniki_konkursu:
#     print(wynik)
#
# print("Sortowanie pierwsze: ")
# wyniki_konkursu.sort()
# for wynik in wyniki_konkursu:
#     print(wynik)
#
# print("Sortowanie drugie: ")
# wyniki_konkursu.sort(reverse=True)
# for wynik in wyniki_konkursu:
#     print(wynik)

# ZADANIE 1
# import random
# lista=[]
# for i in range(10):
#     lista.append(random.randint(1,100))
# print(lista)
#
# najmniejsza=lista[0]
# for j in range(len(lista)):
#     if lista[i]<najmniejsza:
#         najmniejsza=lista[i]
# print(najmniejsza)

# import random
# lista=[]
# for i in range(10):
#     wylosowana = random.randint(1,100)
#     lista.append(wylosowana)
#     print(wylosowana)

# import random
# lista=[]
# suma=0
# for i in range(len(lista)):
#     suma+=lista[:]
# print(suma)
# srednia=suma(len(lista))
# TO NAPRAWIĆ

# ZADANIE 4
# import random
# lista=[]
# pojawienie=0
# for i in range(100):
#     dodaj=random.randint(0,9)
#     lista.append(dodaj)
#     if dodaj ==7:
#         pojawienie+=1
# print(lista)
# print(pojawienie)
