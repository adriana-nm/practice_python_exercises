# 29) TIC TAC TOE Game (TIC TAC TOE PART 4)

def introduction():
    print('Welcome to Tic, Tac, Toe\n'
          'Player 1 you will be \'X\'\n'
          'Player 2 you will be \'o\'\n'
          'Please introduce your move as follow:\n' 
          'number of row, number of column (Ex. 1,2)\n'
          'rows and columns goes from 1 to 3\n'
          'Once you made your move you will\n' 
          'see the board with the updated move\n'
          'Good luck!')


def print_board():
    for sublist in gamelist:
        a = sublist[0] if sublist[0] != 0 else ' '
        b = sublist[1] if sublist[1] != 0 else ' '
        c = sublist[2] if sublist[2] != 0 else ' '
        print(' --- --- --- ')
        print('| {} | {} | {} |'.format(a, b, c))
    print(' --- --- --- ')


def check_win():
    # board positions of every win option
    # every pair of numbers are coordinates of the position (1st number = row, 2nd number = column)
    wins = [['00', '10', '20'], ['01', '11', '21'], ['02', '12', '22'], ['00', '01', '02'],
            ['10', '11', '12'], ['20', '21', '22'], ['00', '11', '22'], ['02', '11', '20']]
    # loop through every sublist and extract the value under each coordinate row/col
    for i in range(8):
        val1 = get_value(i, wins, 0)
        val2 = get_value(i, wins, 1)
        val3 = get_value(i, wins, 2)
        if (val1 == val2 == val3) and (val1 != 0):  # someone won!
            # 1 = Player 1 "X" won
            # 2 = Player 2 "o" won
            return 1 if val1 == 'X' else 2


def get_value(i, wins, pos):
    # get the value of the position under the coordinates row/column
    return gamelist[int(wins[i][pos][0])][int(wins[i][pos][1])]


# loop through all the board to check if board is full
# empty position is represented with value 0
def is_board_full():
    for i in gamelist:
        if 0 in i:
            return False  # Board is not full
    return True  # Board is full


def player_move(i):
    incorrect_move = True
    # loop to validate if user enter a wrong play position
    while incorrect_move:
        move = input('Player {}, please introduce your move\n'.format(i)).split(',')
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


def question_play_again():
     incorrect_response = True
     while incorrect_response:
        response = input('Do you want to play again?\n'
                      'Introduce yes or no\n').lower()
        if response == "yes":
            # Keep playing
            return 1
        elif response == "no":
            # End the game
            return 0
        else:
            print('The answer is not clear')


def game_tictactoe():
    global gamelist
    # initial empty board
    gamelist = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
    introduction()
    print_board()
    keep_play = True
    while keep_play:
        turn = [1, 2, 1, 2, 1, 2, 1, 2, 1]
        # loop for every player turn in the game
        for i in turn:
            player_move(i)
            print_board()
            player = check_win()
            board = is_board_full()
            # check who is the winner and print it
            if player == 1 or player == 2:
                print('Player {} won the game'.format(player))
                keep_play = False
                break
            # if no winner & board full then it's a tie
            elif board is True:
                print('It\'s a tie, no one won the game')
                keep_play = False
                break
    # ask if user wants to play again
    answer = question_play_again()
    if answer == 1:
        game_tictactoe()
    else:
        print('Thanks for playing! See you soon!')


game_tictactoe()