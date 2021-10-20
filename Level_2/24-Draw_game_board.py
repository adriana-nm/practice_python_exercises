# 24) Draw a game board (TIC TAC TOE PART 1)

# Draw and print the following game board:
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---

cont=2
flag = True
while flag is True:
    if cont == 8:
        flag = False
    if cont%2 == 0:
        print(' --- --- --- ')
        cont += 1
    else:
        print('|   |   |   |')
        cont += 1