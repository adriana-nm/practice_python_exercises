# 27) TIC TAC TOE Draw (TIC TAC TOE PART 3)

# Handle the user input in a tic tac toe game
# Ask Player 1 (X) what their move is, and print the board
# Move in format row,col (could be 1, 2 or 3). Ex. 1,3 is row 1 column 3.
# Then ask Player 2 (o) for their move and print again the board.
# Keep asking the moves until the board is full

# CODING STEPS:
# instructions for user (how to introduce the move)
# input of player (row, col)
#     validation: check input is correct (r,c between 1 and 3)
#     validation: check the place is not taken
# extract the (row - 1) & (col - 1)
# put the correct sign of player in the board (list)
# print the board (list)
# repeat until board is full


gamelist = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
print('Welcome to Tic, Tac, Toe\n'
      'Player 1 you will be \'X\'\n'
      'Player 2 you will be \'o\'\n'
      'Please introduce your move as follow:\n' 
      'number of row, number of column (Ex. 1,2)\n'
      'rows and columns goes from 1 to 3\n'
      'Once you made your move you will\n' 
      'see the board with the updated move\n'
      'Good luck!')
player = [1,2,1,2,1,2,1,2,1]
incorrect_move = True
for i in player:
    while incorrect_move:
        move = input('Player {}, please introduce your move'.format(i)).split(',')
        # adapt the move introduced by user, to the correct row & col in python list
        row = int(move[0]) - 1
        col = int(move[1]) - 1
        # validation: check if the numbers are correct & if the position is empty
        if (row >= 0) and (col >= 0) and (row <= 2) and (col <=2):
            if gamelist[row][col] == 0:
                incorrect_move = False
    # check who is the player making the move
    if i == 1:
        fig = 'X'
    else:
        fig = 'o'
    # write the move in the board
    gamelist[row][col] = fig
    # print the board in separate lines
    for sublist in gamelist:
        print(*sublist)
    incorrect_move = True