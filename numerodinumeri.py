# chiedere all'utente il numero di numeri da inserire e farne la somma

# creating an empty list
lst = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
    lst.append(ele) # adding the element

somma = sum(i for i in lst)

print(lst)

print(somma)

# chiedere una serie di numeri finche l'utente scrive fine e calcolarne la somma