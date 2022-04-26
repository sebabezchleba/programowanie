# for i in range(2137):
#     print(i)
#
# for i in range(69,420):
#     print(i)

# for i in range (0,30,3):
#     print(i)

# for i in range (50, 30, -3):
#     print(i)

# cyfra = 0
# while cyfra !=10:
#     print(cyfra)
#     cyfra+=1
#
# znak=""
# print("Aby zakończyć program wciśnij \"q\"")
# while znak != "q":
#     print("Nie wcisnąłeś \"q\"")
#     znak=input()

# print("Aby zakończyć program wciśnij \"q\"")
# while True:
#     znak = input()
#     if znak != "q":
#         print("Nie wcisnąłeś \"q\"")
#     else:
#         break

# print("Aby zakończyć program wciśnij \"q\"")
# while True:
#     znak = input()
#     if znak == "q":
#         break
#     print("Nie wcisnąłeś \"q\"")

# while True:
#     print("Aby zakońzyć program wciśnij \"q\"")
#     print("Aby wyświetlić imię autora wciśnij \"i\"")
#     print("Aby wyświetlić nazwę przedmiotu i kierunku wciśnij \"n\"")
#     znak = input()
#     if znak == "i":
#         print("Sa")
#     elif znak == "n":
#         print("Programowanie na kognitywistyce")
#     elif znak == "q":
#         break
#     else:
#         print("Nieprawidłowy znak.")

# for i in range (1,4):
#     for j in range (1,5):
#         print(f"To jest {i} wykonanie zewnętrznej pętli i {j} wewnętrznej pętli")

# for i in range (0,2):
#     for j in range (0,2):
#         for k in range (0,2):
#             print(f"{i} {j} {k}")

# import os
# os.system("cls")

# import os
# print("To nie będzie widoczne")
# os.system ("cls")
# print("To będzie widoczne")

# from colorama import init
# from termcolor import colored
# init()
# print(colored("Cześć!", "green"))

# ZADANIE 1
# import os
# while True:
#     print("Aby wykonać operację na liczbach wybierz \"o\"")
#     print("Aby zakończyć wybierz \"q\"")
#     znak = input()
#     os.system("cls")
#     if znak == "o":
#         print("Podaj pierwszą liczbę:")
#         pierwsza = int(input())
#         print("Podaj drugą liczbę:")
#         druga = int(input())
#         print("Jaką operację chcesz wykonać?")
#         operacja = input()
#         os.system("cls")
#         if operacja == "dodawanie":
#             dodawanie = pierwsza + druga
#             print(f"Wynikiem dodawania {pierwsza} i {druga} jest {dodawanie}.")
#         elif operacja == "odejmowanie":
#             odejmowanie = pierwsza - druga
#             print(f"Wynikiem odejmowania {druga} od {pierwsza} jest {odejmowanie}.")
#         elif operacja == "mnożenie":
#             mnozenie = pierwsza*druga
#             print(f"Wynikiem mnożenia {pierwsza} razy {druga} jest {mnozenie}.")
#         elif operacja == "dzielnie":
#             dzielenie = pierwsza / druga
#             print(f"Wynikiem dzielenia {pierwsza} przez {druga} jest {dzielenie}.")
#         else:
#             print("Nierozpoznano.")
#     elif znak == "q":
#         break
#     else:
#         print("Nierozpoznano.")

# ZADANIE 2
# suma = 0
# for i in range (0,51):
#     print(i)
#     suma+=i
# print(f"Suma tych wszystkich liczb to {suma}")

# ZADANIE 3
# i=0
# while (i<101):
#     if (i==4 or i==34 or i==92):
#         i+=1
#     elif (i==57):
#         i+=18
#     elif(i==78):
#         i+=13
#     print(i)
#     i+=1

# ZADANIE 4
# import termcolor
# import colorama
# from termcolor import colored
# from colorama import init
# init()
# print(colored("       x       ", "green"))
# print(colored("      xxx      ", "green"))
# print(colored("     xx","green")+colored("x","red")+colored("xx     ","green"))
# print(colored("    x","green")+colored("x", "red")+colored("x", "green")+colored("x", "blue")+colored("x", "green")+colored("x","red")+colored("x    ", "green"))
# print(colored("   xxxxxxxxx   ", "cyan"))
# print(colored("  xxxxxxxxxxx  ", "magenta"))
# print(colored(" xxxxxxxxxxxxx ", "blue"))
# print(colored("xxxxxxxxxxxxxxx", "red"))
# print(colored("      |||      ", "yellow"))
# print(colored("      |||      ", "yellow"))

# ZADANIE 6
# for i in range (0,10):
#     for j in range (0,10):
#         for k in range (0,10):
#             print(f"{i} {j} {k}")

# ZADANIE 7
# liczba_wystapien=0
# for i in range (10):
#     for j in range (10):
#         for k in range (10):
#             print(f"{i} {j} {k}")
#             if i==4:
#                 liczba_wystapien+=1
#             if j==4:
#                 liczba_wystapien+=1
#             if k==4:
#                 liczba_wystapien+=1
# print(f"Liczba 4 wystąpiła {liczba_wystapien} razy")

# ZADANIE 8, sposób 1
# suma = 0
# for i in range (25,51):
#     # print(i)
#     suma+=i
# print(f"Suma tych wszystkich liczb to {suma}")

# ZADANIE 8, sposób 2
# suma=0
# liczba=25
# while liczba<51:
#     # print(liczba)
#     suma+=liczba
#     liczba+=1
# print(suma)

# ZADANIE 9, sposób 1
# suma=0
# for i in range (25,51):
#     # print(i)
#     if i%2==0:
#         suma+=i
#     i+=1
# print(suma)

# ZADANIE 9, sposób 2
# suma=0
# liczba=25
# while liczba<51:
#     # print(liczba)
#     if liczba%2==0:
#         suma+=liczba
#     liczba+=1
# print(suma)

# ZADANIE 10
# for i in range (10):
#     print(i)
# ZOSTAWIAMY TO BO SKOMPLIKOWANE

# ZADANIE 11
# print("Przepis na jajecznicę. Ilu jaj chcesz użyć?")
# jaja=int(input())
# NIE CHCE MI SIĘ

# ZADANIE 12
# import os
# import termcolor
# import colorama
# from termcolor import colored
# from colorama import init
# while True:
#     print("Aby zakońzyć program wciśnij \"q\"")
#     print("Aby wyświetlić imię autora wciśnij \"i\"")
#     print("Aby wyświetlić nazwę przedmiotu i kierunku wciśnij \"n\"")
#     print("Aby policzyć sume liczb od 0 do 50 wciśnij \"s\"")
#     print("Aby wyswietlić liczby od 0 do 100, poza: 4, 34, 57-74, 78-90, 92 wciśnij \"p\"")
#     print("Aby wyświetlić kolorową choinkę wciśnij \"c\"")
#     znak = input()
#     os.system("cls")
#     if znak == "i":
#         print("Sa")
#     elif znak == "n":
#         print("Programowanie na kognitywistyce")
#     elif znak == "s":
#         suma = 0
#         for i in range (0,51):
#             print(i)
#             suma+=i
#         print(f"Suma tych wszystkich liczb to {suma}")
#     elif znak == "p":
#         i=0
#         while (i<101):
#             if (i==4 or i==34 or i==92):
#                 i+=1
#             elif (i==57):
#                 i+=18
#             elif(i==78):
#                 i+=13
#             print(i)
#             i+=1
#     elif znak == "c":
#         init()
#         print(colored("       x       ", "green"))
#         print(colored("      xxx      ", "green"))
#         print(colored("     xx","green")+colored("x","red")+colored("xx     ","green"))
#         print(colored("    x","green")+colored("x", "red")+colored("x", "green")+colored("x", "blue")+colored("x", "green")+colored("x","red")+colored("x    ", "green"))
#         print(colored("   xxxxxxxxx   ", "cyan"))
#         print(colored("  xxxxxxxxxxx  ", "magenta"))
#         print(colored(" xxxxxxxxxxxxx ", "blue"))
#         print(colored("xxxxxxxxxxxxxxx", "red"))
#         print(colored("      |||      ", "yellow"))
#         print(colored("      |||      ", "yellow"))
#     elif znak == "q":
#         break
#     else:
#         print("Nieprawidłowy znak.")
#     print(" ")
