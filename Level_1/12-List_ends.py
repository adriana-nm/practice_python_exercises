# 12) List Ends

# Create a random list and extract the first and last numbers
# Write the code inside functions

import random

def create_rd_list():
    lt = list(random.sample(range(1,100),8))
    return lt

def first_last(lt):
    a = [lt[0],lt[-1]]
    return print(a)

lt = create_rd_list()
#print(lt)
first_last(lt)
