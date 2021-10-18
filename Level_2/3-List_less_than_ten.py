# 3) List less than ten

# Print all the elements of the list that are less than 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for num in a:
    if num < 5:
        print(num)

# Extra 1: Make a new list that has all the elements less than 5 from this list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = []
for num in a:
    if num < 5:
        c.append(num)
print(c)

# Extra 2: Write this in one line of Python.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([num for num in a if num<5] )


# Extra 3: Ask the user for a number and return a list that contains only elements from the original list a that are smaller.
number = input('Please introduce a number')
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
d = []
for num in a:
    if num < int(number):
        d.append(num)
print(d)