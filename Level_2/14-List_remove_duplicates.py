# 14) List Remove Duplicates

# Write a function
# Create a random list
# Return a new list with same elements (minus duplicates)

import random

def new_list():
    l = [random.randrange(1,10) for i in range(7)]
    return l

def list_nodup(l):
    s ={i for i in l}
    return s

def remove_duplicates():
    l = new_list()
    print(l)
    return list_nodup(l)

remove_duplicates()
