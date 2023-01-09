from random import randint


def selectionSort(values):
    for i in range(len(values)):
        minPos = minimumPosition(values, i)
        temp = values[minPos]
        values[minPos] = values[i]
        values[i] = temp

def minimumPosition(values, start):
    minPos = start
    for i in range(start + 1, len(values)):
        if values[i] < values[minPos]:
            minPos = i
    return minPos


n = 20
values = []

for i in range(n):
    values.append(randint(1,100))

print(values)
selectionSort(values)
print(values)