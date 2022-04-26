# lancuch="slowo"
# dlugosc=len(lancuch)
#
# print(dlugosc)
#
# print(lancuch)
#
# for i in range(dlugosc):
#     print(lancuch[i])
#
# for i in lancuch:
#     print(i)


# lancuch="Więcej liter"
# print(lancuch[3])
# print(lancuch[-1])
# print(lancuch[5:])


# print("Podaj swoje imię")
# imie=input()
#
# lancuch1="Cześć "
# lancuch2="! Miło mi cię widzieć!"
#
# print(lancuch1 + imie + lancuch2)


# lancuch = "Dużo więcej liter"
# for litera in lancuch:
#     if "e" == litera:
#         print("Znalazłem \"e\"")

# lancuch = "Dużo więcej liter"
# if "e" in lancuch:
#         print("Znalazłem \"e\"")


# lancuch = "Dużo więcej liter"
# nowy_lancuch=""
#
# for litera in lancuch:
#     if "e"==litera:
#         nowy_lancuch+="aaa"
#     else:
#         nowy_lancuch+=litera
#
# print(nowy_lancuch)


# lancuch="slowo"
# print(lancuch)
#
# lancuch_lista=list(lancuch)
# lancuch_lista[1]="m"
# lancuch="".join(lancuch_lista)
# print(lancuch)


# lancuch=("Second-year high school student Yatora Yaguchi is a delinquent"
#         "with excellent grades, but is unmotivated to find his true calling in "
#         "life. Yatora spends his days working hard to maintain his academic "
#         "standing while hanging out with his equally unambitious friends.")
#
# print(lancuch.upper())
# print(lancuch.lower())
#
# print(lancuch.count("u"))
#
# print(lancuch.replace("Second-year", "Dumb"))

#ZADANIE 1
# ciag="qwertyuiopasdfghjkklcbxjk"
# ciag.isalpha()
# if ciag.isalpha():
#     print("Tak")
# else:
#     print("Nie")


#ZADANIE 2
# ciag="qwertyuiopasdfghjkklcbxjk"
# print(ciag.capitalize())


#ZADANIE 3
# ciag="qwe rty uio pasd fghjkklc bxjk"
# print(ciag.replace(" ", ""))

#ZADANIE 4
# lancuch=input("Podaj łańcuch: ")
# spolgloski_spis="QWRTPSDFGHJKLZXCVBNMqwrtpsdfghjklzxcvbnmŚśŁłżŻźŹćĆŃń"
# samogloski_spis="eyuioaEYUIOAĘęóÓąĄ"
# samogloski=0
# spolgloski=0
# liczby=0
# for element in lancuch:
#     if element in samogloski_spis:
#         samogloski+=1
#     if element in spolgloski_spis:
#         spolgloski+=1
# print(f"Liczba społgłosek w łancuchu: {spolgloski}")
# print(f"Liczba samogłosek w łancuchu: {samogloski}")

#ZADANIE 5
# print("Podaj łańcuch: ")
# lancuch=input()
# samogloski_spis="eyuioaEYUIOAĘęóÓąĄ"
# for samogloska in lancuch:
#     if samogloska in samogloski_spis:
#         print(samogloska, end="")
#     else:
#         print(" ", end="")

#ZADANIE 6
# print("Podaj zdanie wyjściowe: ", end="")
# zdanie=input()
# print("Podaj który znak chcesz zmienić: ", end="")
# znak=input()
# print("Podaj co wpisać z zamian: ", end="")
# zamiana=input()
# zdanie1=zdanie.replace(znak,zamiana)
# print(zdanie1)
#
# print("Podaj który znak chcesz zmienić: ", end="")
# znak=input()
# print("Podaj co wpisać z zamian: ", end="")
# zamiana=input()
# zdanie2=zdanie1.replace(znak,zamiana)
# print(zdanie2)
#
# print("Podaj który znak chcesz zmienić: ", end="")
# znak=input()
# print("Podaj co wpisać z zamian: ", end="")
# zamiana=input()
# zdanie3=zdanie2.replace(znak,zamiana)
# print(zdanie3)

#ZADANIE 7
# print("Podaj imię:")
# imie=input()
# print(imie.capitalize())

#ZADANIE 8


#ZADANIE 9
# print("Podaj słowo:")
# slowo=input()
#
# nowe_slowo=""
# for i in range(1,len(slowo)+1):
#     nowe_slowo+=slowo[-i]
# print(nowe_slowo)
#
# nowe_slowo=""
# for i in range(len(slowo)):
#     nowe_slowo+=slowo[-i-1]
# print(nowe_slowo)


#ZADANIE 13
# ciag="hjm"
# m = ciag.find("m")
# print(m)

#ZADANIE 14
# ciag = "thyjkkmjokm"
# m = ciag.rfind("m")
# print(m)
