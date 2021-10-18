# 7) List Comprehensions

# Take a list and create a new one that has only the even elements on it.
# Write it in one line of code

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([c for c in a if int(c)%2 == 0])