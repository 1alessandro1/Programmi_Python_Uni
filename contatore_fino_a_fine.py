lst = []


while True:
    ele = (input("Input: "))
    lst.append(ele) # adding the element
    if ele == "fine":
        break

somma = sum(int(i) for i in lst[:-1])

print(somma)

