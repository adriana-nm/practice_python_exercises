# 20 Element Search

# Take an ordered list of numbers (from small to large) & a number
# Check if the number is on the list

# Option A:

a = [1, 3, 5, 30, 42, 43, 500]
num = int(input('Please enter a number'))
if num in a:
    print('The number is in the list')
else:
    print('The number is not in the list')
