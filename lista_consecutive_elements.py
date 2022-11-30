from itertools import groupby

list1 = [0, 0, 1, 1, 1, 1, 0, 1, 1, 0]

count_dups = [sum(1 for _ in group) for _, group in groupby(list1)]
print((count_dups))

