# print("Ile masz lat?")
# wiek = int(input())
# #
# # if wiek >= 18:
# #     print("Brawo!")
# #     print("Jesteś pełnoletni!")
# # else:
# #     print("Nie jesteś pełnoletni!")
# # print("To był program sprawdzający pełnoletniość")


# print("Ile masz lat?")
# wiek = int(input())
#
# if wiek <= 3:
#     print("Jesteś niemowlęciem!")
# elif wiek < 12:
#     print("Jesteś dzieckiem")
# elif wiek < 20:
#     print("Jesteś nastolatkiem")
# else:
#     print("Jesteś dorosły")

# print("Podaj wartość pierwszego wyrazu logicznego")
# p=int(input())
# print("Podaj wartość drugiego wyrazu logicznego")
# q=int(input())
#
# if p and q:
#     print("Prawda")
# else:
#     print("Fałsz")


# print("Podaj wartość pierwszego wyrazu logicznego")
# p=int(input())
# print("Podaj wartość drugiego wyrazu logicznego")
# q=int(input())
#
# if not (p or q) and q:
#     print("Prawda")
# else:
#     print("Fałsz")

# X=0
# if X>4 or X>7:
#     print("coś")

# print("Czy masz ochotę napić się piwa?")
# decyzja=input()
#
# if decyzja == "tak":
#     print("Czy masz 18 lat?")
#     decyzja2=input()
#     if decyzja2 == "tak":
#         print("Możesz!")
#     else:
#         print("Nie możesz!")
# else:
#     print("No trudno")

#
# liczba_wystapien=0
#
# print("Wpisz liczbę")
# pobrana_liczba=int(input())
# if pobrana_liczba == 5:
#     liczba_wystapien=liczba_wystapien+1
#
# print("Wpisz liczbę")
# pobrana_liczba=int(input())
# if pobrana_liczba == 5:
#     liczba_wystapien+=1
#
# print("Wpisz liczbę")
# pobrana_liczba=int(input())
# if pobrana_liczba == 5:
#     liczba_wystapien+=1
# print(f"Cyfra 5 wystąpiła: {liczba_wystapien} razy")

# ZADANIE 1
# print("Podaj pierwszą liczbę:")
# pierwsza = int(input())
# print("Podaj drugą liczbę:")
# druga = int(input())
# print("Jaką operację chcesz wykonać?")
# operacja = input()
# dodawanie = pierwsza + druga
# odejmowanie = pierwsza - druga
# mnozenie = pierwsza * druga
# dzielenie = pierwsza / druga
# if operacja == "dodawanie":
#     print(f"Wynikiem dodawania jest: {dodawanie}")
# elif operacja == "odejmowanie":
#     print(f"Wynikiem odejmowania jest: {odejmowanie}")
# elif operacja == "mnożenie":
#     print(f"Wynikiem mnożenia jest: {mnozenie}")
# elif operacja == "dzielenie":
#     print(f"Wynikiem dzielenia jest: {dzielenie}")
# else:
#     print("Nie rozpoznano operacji.")
#
# ZADANIE 2
# print("Podaj pierwszą liczbę:")
# pierwsza = int(input())
# print("Podaj drugą liczbę:")
# druga = int(input())
# if pierwsza>druga:
#     print(f"{pierwsza} jest większą z nich")
# elif druga>pierwsza:
#     print(f"{druga} jest większą z nich")
# elif pierwsza==druga:
#     print(f"To ta sama liczba")

# ZADANIE 3
# print("Podaj 1. liczbę:")
# a = int(input())
# print("Podaj 2. liczbę:")
# b = int(input())
# print("Podaj 3. liczbę:")
# c = int(input())
# print("Podaj 4. liczbę:")
# d = int(input())
# print("Podaj 5. liczbę:")
# e = int(input())
#
# if a>=b and a>=c and a>=d and a>=e :
#     print(f"{a} jest największą z nich")
# elif b>=a and b>=c and b>=d and b>=e:
#     print(f"{b} jest największą z nich")
# elif c>=a and c>=b and c>=d and c>=e:
#     print(f"{c} jest największą z nich")
# elif d>=a and d>=b and d>=c and d>=e:
#     print(f"{d} jest największą z nich")
# elif e>=a and e>=b and e>=c and e>=d:
#     print(f"{e} jest największą z nich")
# else:
#     print("Błąd")

# ZADANIE 4
# print("Podaj ile uzyskano punktów:")
# punkty = float(input())
# if punkty <= 5:
#     print("Ocena: ndst")
# elif punkty <= 7:
#     print("Ocena: dst")
# elif punkty ==7.5:
#     print("Ocena: dst+")
# elif punkty == 8:
#     print("Ocena: db")
# elif punkty == 9:
#     print("Ocena: db+")
# elif punkty == 10:
#     print("Ocena: bdb")
# else:
#     print("Błąd")
#
# ZADANIE 5
# print("Podaej nazwę użytkownika:")
# nazwa = input()
# print("Podaj hasło:")
# haslo1 = input()
# print("Podaj hasło ponownie")
# haslo2 = input()
# if haslo1 == haslo2:
#     print("Hasło poprawne")
# else:
#     print("Hasła niezgodne")

# ZADANIE 6i7
# print("Podaj nazwę użytkownika.")
# nazwa = input()
# print("Podaj dwukrotnie hasło")
# haslo1 = input()
# haslo2 = input()
# if haslo1 == haslo2:
#     print("Hasła są zgodne. Czy masz 18 lat?")
#     wiek = input()
#     if wiek =="tak":
#         print("Konto założone! Czy chcesz założyć konto superużytkownika?")
#         super = input()
#         if super == "tak":
#             print("Zostałeś superużytkonikiem!")
#         elif super == "nie":
#             print("Dlaczego nie chcesz super-konta?")
#             why = input()
#             if why == "za drogie":
#                 print("Ok biedaku!")
#             elif why == "nie potrzebuję":
#                 print("Tak sobie wmawiaj")
#             else:
#                 print("Twoja strata!")
#         else:
#             print("Komenda nierozpoznana.")
#     elif wiek =="nie":
#         print("Masz zgodę rodziców?")
#         zgoda = input()
#         if zgoda == "tak":
#             print("Konto założone! Czy chcesz założyć konto superużytkownika?")
#             super = input()
#             if super == "tak":
#                 print("Zostałeś superużytkonikiem!")
#             elif super == "nie":
#                 print("Dlaczego nie chcesz super-konta?")
#                 why = input()
#                 if why == "za drogie":
#                     print("Ok biedaku!")
#                 elif why == "nie potrzebuję":
#                     print("Tak sobie wmawiaj")
#                 else:
#                     print("Twoja strata!")
#             else:
#                 print("Komenda nierozpoznana.")
#         elif zgoda == "nie":
#             print("Nie możesz założyć konta!")
#         else:
#             print("Komenda nierozpoznana.")
# else:
#     print("Hasła niezgodne")

# ZADANIE 8
# print("Podaj liczbę:")
# liczba = float(input())
# if liczba >= 0:
#     print(f"Wartość bezwzględna = {liczba}")
# elif liczba <0:
#     dodaj = liczba-(2*liczba)
#     print(f"Wartość bezwzględna = {dodaj}")

# ZADANIE 9i10
# print("Podaj liczbę:")
# liczba=int(input())
# test=liczba%2
# dziel=liczba/2
# if test == 0:
#     print(f"Liczba jest parzysta. Wynikiem dzielenia przez 2 jest: {dziel}")
# elif test != 0 and liczba>10:
#     print("Ta duża liczba nie jest parzysta.")
# elif test !=0 and liczba<10:
#     print("Ta mała liczba nie jest parzysta.")

# ZADANIE 12
print("Podaj wartość p:")
p = bool(input())
print("Podaj wartość q:")
q = bool(input())
linia = "-----------------------------------------------------------"
zdanie1 = p or q
zdanie2 = not (p or q)
zdanie3 = not (p or q) and q
print(linia)
print("|  p   |  q   | p or q | not (p or q) | not (p or q) and q |")
print(linia)
print(f"| {p} | {q} | {zdanie1}   |{zdanie2}         |{zdanie3}               |")
print(linia)

# print("Podaj wartość p:")
# p = int(input())
# print("Podaj wartość q:")
# q = int(input())
# linia = "------------------------------------------------------"
# print(linia)
# print("| p | q | p or q | not (p or q) | not (p or q) and q |")
# print(linia)
# if p==1 and q==1:
#     print(f"| 1 | 1 | 1      | 0            | 0                  |")
# elif p==0 and q==0:
#     print(f"| 0 | 0 | 0      | 1            | 0                  |")
# elif p==1 and q==0:
#     print(f"| 1 | 0 | 1      | 0            | 0                  |")
# elif p==0 and q==1:
#     print(f"| 0 | 1 | 1      | 0            | 0                  |")
# print(linia)
#
#
#
# linia = "------------------------------------------------------"
# print(linia)
# print("| p | q | p or q | not (p or q) | not (p or q) and q |")
# print(linia)
# print("| 1 | 1 | 1      | 0            | 0                  |")
# print(linia)
# print("| 0 | 0 | 0      | 1            | 0                  |")
# print(linia)
# print("| 1 | 0 | 1      | 0            | 0                  |")
# print(linia)
# print("| 0 | 1 | 1      | 0            | 0                  |")
# print(linia)
