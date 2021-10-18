# 8) Rock Paper Scissors

# Make a two-player game Rock-Paper-Scissors
# Rules: Rock beat scissors, scissors beats paper, paper beats rock

def rsp():
    while True:
        play1 = readNextPlay("Player 1")
        play2 = readNextPlay("Player 2")

        show_result(play1, play2)

        playdecision = input('Do you wanna keep playing?').lower()
        if playdecision == 'no':
            break

def readNextPlay(playerName):
    intro_message = '{}, please enter one option: Rock/Scissors/Paper'.format(playerName)
    playmove = input(intro_message).lower()
    while playmove not in ('rock','scissors','paper'):
         print('You enter a wrong option')
         playmove = input(intro_message).lower()
    return playmove


def show_result(play1, play2):
    if play1 == play2:
        print('It\'s a tie')
    elif (play1 == 'rock') and (play2 == 'scissors'):
        print('Congratulations Player 1, you win')
    elif (play1 == 'scissors') and (play2 == 'paper'):
        print('Congratulations Player 1, you win')
    elif (play1 == 'paper') and (play2 == 'rock'):
        print('Congratulations Player 1, you win')
    elif (play2 == 'rock') and (play1 == 'scissors'):
        print('Congratulations Player 2, you win')
    elif (play2 == 'scissors') and (play1 == 'paper'):
        print('Congratulations Player 2, you win')
    elif (play2 == 'paper') and (play1 == 'rock'):
        print('Congratulations Player 2, you win')


rsp()

