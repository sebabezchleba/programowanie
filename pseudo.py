# import random
# wylosowana = random.randint(1,10)
# print(wylosowana)

# import random
# wylosowana = random.random()
# print(wylosowana)

# import random
# wylosowana = random.randint(0,1)+random.random()
# print(wylosowana)

# import random
# wylosowana = 2*random.random()
# print(wylosowana)

# import random
# wylosowana = random.randint(0,9)+random.random()-5
# print(wylosowana)

# import random
# wylosowana = random.random()
# zaokraglona = round(wylosowana,2)
# print(zaokraglona)

# import random
# wylosowana = random.random()
# print(f"{wylosowana: .2f}")

# import random
# slowo = "Kognitywistyka"
# wylosowana = random.choice(slowo)
# print(wylosowana)

# import time
# cyfra=0
# start=time.time()
# while cyfra!=1:
#     print("Nie wcisnąłeś \"1\"\n")
#     cyfra=int(input())
# koniec=time.time()
# czas_trwania=koniec-start
# print(f"Na wciśnięcie 1 potrzebowałeś: {czas_trwania}")

# import time
# print(f"Początek: {time.ctime()}")
# time.sleep(5)
# print(f"Koniec: {time.ctime()}")

# ZADANIE 1
# import time
# print("Uwaga!")
# for i in range (5,0,-1):
#     time.sleep(1)
#     print(i)
# time.sleep(1)
# print("Boom!")

# ZADANIE 3
# import random
# kostka = random.randint(1,6)
# print(kostka)

# ZADANIE 4
# import random
# for i in range (6):
#     lotto = random.randint(2,48)
#     print(lotto)

# ZADANIE 5
# import random
# lotto1 = random.randint(2,48)
# lotto2 = random.randint(2,48)
# lotto3 = random.randint(2,48)
# lotto4 = random.randint(2,48)
# lotto5 = random.randint(2,48)
# lotto6 = random.randint(2,48)
# print(lotto1)
# if lotto2 != lotto1:
#     print(lotto2)
#     if lotto3!= lotto2 and lotto3!=lotto1:
#         print(lotto3)
#         if lotto4!=lotto3 and lotto4!=lotto2 and lotto4!=lotto1:
#             print(lotto4)
#             if lotto5!=lotto4 and lotto5!=lotto3 and lotto5!=lotto2 and lotto5!=lotto1:
#                 print(lotto5)
#                 if lotto6!=lotto5 and lotto6!=lotto4 and lotto6!=lotto3 and lotto6!=lotto2 and lotto6!=lotto1:
#                     print(lotto6)
# TU COŚ TRZEBA ZMIENIĆ

# import random
# import time
# i=0
# lotto={}
# while True:
#     lotto[i]=random.randint(1,49)
#     for j in range (0,i):
#         while lotto[j]==lotto[i]:
#             lotto[i]=random.randint(1,49)
#     print(lotto[i])
#     if i==5:
#         break
#     time.sleep(0.5)
#     i+=1

# ZADANIE 6
# import random
# import time
# slowo = "qwertyuiopasdfghjklzxcvbnm"
# wylosowana = random.choice(slowo)
# print(f"Wciśnij jak najszybciej klawisz: {wylosowana}")
# start=time.time()
# while True:
#     wcisk = input()
#     if wcisk == wylosowana:
#         koniec=time.time()
#         czas_trwania=koniec-start
#         print(f"Na wciśnięcie {wylosowana} potrzebowałeś: {czas_trwania}")
#     else:
#         print("Zły znak")

# ZADANIE 7
