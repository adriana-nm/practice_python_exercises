# 18) Game Cows&Bulls

# Create a program that will play the game "cows and bulls" with the user
# Randomly generate a 4-digit number (no repeated digits)
# Ask the user to guess a 4-digit number
# For every digit guesses correctly in the correct place, user gets a "cow"
# For every digit guesses correctly in the wrong place, user gets a "bull"
# Keep track of the number of guesses and tell them at the end

import random
import string

def show_title():
    print('======================================================================')
    print(" _____ _____  _    _ _____                   _  ______       _ _       \n" \
        "/  __ \  _  || |  | /  ___|                 | | | ___ \     | | |      \n" \
        "| /  \/ | | || |  | \ `--.    __ _ _ __   __| | | |_/ /_   _| | |___   \n" \
        "| |   | | | || |/\| |`--. \  / _` | '_ \ / _` | | ___ \ | | | | / __|  \n" \
        "| \__/\ \_/ /\  /\  /\__/ / | (_| | | | | (_| | | |_/ / |_| | | \__ \  \n" \
        " \____/\___/  \/  \/\____/   \__,_|_| |_|\__,_| \____/ \__,_|_|_|___/' \n")
    print('Welcome, you are about to play "Cows&Bulls"')
    print('======================================================================')

def game_instructions():
    show_title()
    intflag = 0
    while intflag == 0:
        inst = input('If you never played it and need the instructions write: yes (otherwise write: no)').lower()
        if inst == "yes":
            print("You will have to guess a number of 4 digit\n"
                  "To achieve this, you will enter a number of 4 digit\n"
                  "Every time the right number is in the correct place you'll have a COW\n"
                  "Every time a correct number is in the wrong place you'll have a BULL\n"
                  "Once you guess the correct order of the 4 digits, you WIN")
            intflag = 1
        elif inst == "no":
            print('Great, then let\'s start playing')
            intflag = 1
        else:
            print('Sorry the response was not clear')

game_instructions()

def game_num():
    while True:
        gamenum = [random.choice(string.digits) for i in range(4)]
        gsetnum = set(gamenum.copy())
        if len(gamenum) == len(gsetnum):
            return gamenum

def user_num():
    while True:
        usernum = list(input('Please introduce a 4 digit number (don\'t repeat the number)'))
        usetnum = set(usernum.copy())
        if len(usernum) == 4:
            if len(usernum) == len(usetnum):
                return usernum

def gamecondition(gamenum, usernum):
    global cow
    cow = 0
    bull = 0
    for i,j in zip(gamenum, usernum):
        if i == j:
            cow += 1
    for i in usernum:
        if i in gamenum:
            bull += 1
    bull = bull - cow
    print('You have: {} cows and {} bulls'.format(cow,bull))

def game():
    game_instructions()
    gamenum = game_num()
    count = 0
    while True:
        usernum = user_num()
        print(gamenum)
        print(usernum)
        gamecondition(gamenum,usernum)
        count += 1
        if cow == 4:
            print('You used {} tries'.format(count))
            return ('You just won the game!!')

game()
