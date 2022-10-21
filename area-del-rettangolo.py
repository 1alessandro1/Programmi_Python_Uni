import math

altezza = float(input("Dammi l'altezza: "))
base = float(input("Dammi la base: "))

Area = base * altezza

diagonale_del_rettangolo = math.sqrt(altezza*altezza + base*base)

print ("L'area del rettangolor vale:", (Area), "e la sua diagonale vale: ", (diagonale_del_rettangolo))
