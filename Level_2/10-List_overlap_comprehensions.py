# 10) Ex. 5 List overlap using list comprehension

# Return a list that contains only elements that are in both list.
# Make sure size of the list are different.
# Write it with list comprehension in one line

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print({ data for data in a if data in b})