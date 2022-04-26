# Wersja 1

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

# Wersja 2

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
#Wersja 3
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
