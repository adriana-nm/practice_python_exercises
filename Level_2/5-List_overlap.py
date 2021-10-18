# 5) List Overlap

# Return a list with only the elements that are in both list (no duplicates)
# Size of list must be different

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
e = []
for data in a:
    if (data in b) and (data not in e):
        e.append(data)
e.sort()
print(e)

# Put 2 random generated list

import random

a = [random.randint(1, 25) for i in range(11)]
b = [random.randint(1, 25) for i in range(13)]
e = []
for data in a:
    if (data in b) and (data not in e):
        e.append(data)
e.sort()
print(e)