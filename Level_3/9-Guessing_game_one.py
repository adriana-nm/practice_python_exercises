# 9) Guessing game one

# Generate a random number between 1 and 9 (including 1 & 9)
# Ask the user to guess the number.
# Tell them if they guess too low, too high or exactly right.
# Keep track of how many guesses the user has taken. Print it at the end.


import random

def jugar():
    number = random.randint(1, 9)
    count = 0
    play = True
    while play:
        usernum = input('Please introduce a number').lower()
        intusernum = int(usernum)
        count += 1
        if number < intusernum:
            print('Your answer is too high')
        elif number > intusernum:
            print('Your answer is too low')
        else:
            print('Your answer is correct!')
            print('You made {} guesses'.format(count))
            play = False


def volver_jugar():
    game = input('Do you wanna keep playing?  (yes/no)').lower()
    return not game == 'no'


def guessthenumber():
    keepplay = True
    while keepplay:
        jugar()
        keepplay = volver_jugar()
    print('Bye!')

guessthenumber()