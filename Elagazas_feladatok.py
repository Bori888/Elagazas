# #4 feladat
#
# a = float(input("Mondj egy számot! "))
# b = float(input("Mondj egy számot! "))
# c = float(input("Mondj egy számot! "))
#
# if (a +b > c) and (a +c > b) and (c +b > a):
#     print("Ez egy 3szög")
#     if (a**2 + b**2 == c**2 ) or (a**2 + c**2 == b**2) or(b**2 + b**2 == a**2) :
#         print("Derékszögű 3szög")
#     else:
#         print("Nem derékszögű 3szög")
# else:
#     print("Ez nem egy 3szög")

#2 feladat
d = int(input("Mondj egy számot! "))
if  d % 3 == 0 or d % 5 == 0:
    print ("Oszthato 3-mal vagy 5-el ez a szám ")