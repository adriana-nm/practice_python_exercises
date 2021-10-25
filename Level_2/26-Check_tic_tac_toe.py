# 24) Check TIC TAC TOE (TIC TAC TOE PART 2)

# Representation of tic tac toe:
# game = [[1, 2, 0],
#      	 [2, 1, 0],
# 	     [2, 1, 1]]
# 0 means empty, 1 is player 1, 2 is player 2
# Win: 3 in a row, column or diagonal
# Check if anyone has won, and inform who it was, or inform no winner


gamelist = [[2, 1, 1],
            [1, 2, 2],
            [1, 2, 2]]

def check_win(gamelist):
    wins = [['00', '10', '20'], ['01', '11', '21'], ['02', '12', '22'], ['00', '01', '02'],
            ['10', '11', '12'], ['20', '21', '22'], ['00', '11', '22'], ['02', '11', '20']]
    for i in range(8):
        a = wins[i][0]
        b = wins[i][1]
        c = wins[i][2]
        if (gamelist[int(a[0])][int(a[1])] == gamelist[int(b[0])][int(b[1])] == gamelist[int(c[0])][int(c[1])]) and (
                gamelist[int(a[0])][int(a[1])] != 0):
            if gamelist[int(a[0])][int(a[1])] == 1:
                # 1 = Player 1 won
                return 1
            else:
                # 2 = Player 2 won
                return 2


def is_board_full(gamelist):
    for i in gamelist:
        if 0 in i:
            # Board is not full
            return False
    # Board is full
    return True


def game_tictactoe(gamelist):
    keep_play = True
    while keep_play:
        player = check_win(gamelist)
        board = is_board_full(gamelist)
        if player == 1 or player == 2:
            print('Player {} won the game'.format(player))
            keep_play = False
        elif board is True:
            print('It\'s a tie, no one won the game')
            keep_play = False



game_tictactoe(gamelist)
