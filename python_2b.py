# import math
# feladat 4

# a = float(input("a ="))
# b = float(input("b ="))
# if a < b:
#     print(a, "<", b)
# elif b < a:
#     print(a, ">", b)
# else:
#     print(a, "=", b)
#
# #  feladat 5
#
# s = float(input("Mennyi a kör sugara? "))
# if s > 0:
#     print(s * s * math.pi, 'az ilyen sugaru kör kerülete ')
# else:
#     print("Hiba: a kör sugara nem pozitív!")

#  feladat 6
# c = int(input("Mondj egy számot! "))
#
# if c > 0:
#     if c < 200:
#         print("Alföld")
#     elif c < 500:
#         print("Dombság")
#     elif c < 1500:
#         print("Középhegység")
#     else:
#         print("Hegység")
# else:
#     print("A szám nem pozitiv")

#  feladat 8

# esz = int(input("Mondj egy évszámot! "))
#
# a = esz % 19
# b = esz % 4
# c = esz % 7
# m = 24
# n = 5
# d = (19*a + m) % 30
# e = (2*b + 4*c + 6*d + n) % 7
#
# if 1900 <= esz <= 2099:
#     if d + e < 10:
#         husvetnap = d + e + 22
#         honap = "március"
#
#     else:
#         husvetnap = d + e - 9
#         honap = "aprilis"
#
#     if honap == "aprilis" and husvetnap == 26:
#         print("húsvét április 19-én van")
#     elif honap == "aprilis" and husvetnap == 25:
#         if d == 28 and e == 6 and a > 10:
#             print("húsvét április 18-án van.")
#     else:
#         print("Husvétnapja ", honap, husvetnap)
