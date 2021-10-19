# 20 Element Search

# Write a function
# Take an ordered list of numbers (from small to large) & a number
# Check if the number is on the list
# Extra: Use Binary search

# Option B: Binary Search

def binary_search(slist,num):
    first = 0
    last = len(slist)-1
    found = False
    while ((first <= last) and (not found)):
        middle = (first+last)//2
        if slist[middle] == num:
            found = True
        else:
            if slist[middle] < num:
                first = middle + 1
            else:
                last = middle-1
    return found


a = [1, 3, 5, 30, 42, 43, 500]
binary_search(a,46)