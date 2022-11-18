# si gioca con le liste

# v = [6,7,2,1,2,5]
# for i in range(len(v)):
#     print(i, v[i])
# 
# # altri giochi con le liste
# 
# c = list("ciao")
# #copia = 
# 
# divisib_per_3 = list(range(0,100,3))
# print(divisib_per_3)

# esercizi

# trovare il massimo elemento con le liste

# list = []
# 
# limite = int(input("inserisci il numero di elementi da confrontare: "))
# 
# for i in range(limite):
#     ele = int((input("Input: ")))
#     list.append(ele)
# 
# for i in list:
#     if list[i] <= list[i+1]:
#         massimo = [i] 
#     print(a)


# oppure

my_list = [4,5,2,6,1,7,8]

max = sorted(my_list)[-1]

# oppure

massimo = list[4,5,2,6,1,7,8]
for x in list:
    if x > max:
        max = x
print(massimo)