# 32) Hangman (HANGMAN PART 3)

# Write the complete game of Hangman
# User only has 6 incorrect guesses (head, body, 2 legs, 2 arms)
# Inform the user how many guesses he has left
# If user guess a letter that they already guessed, don't count them
# When player win or loses, let them start a new game

import random


def print_figure(wrongletters):
    if len(wrongletters) == 0:
        print("  +---+\n"
              "  |   |\n"
              "      |\n"
              "      |\n"
              "      |\n"
              "      |\n"
              "=========\n")
    elif len(wrongletters) == 1:
        print("    +---+\n"
              "    |   |\n"
              "    O   |\n"
              "        |\n"
              "        |\n"
              "        |\n"
              "  =========\n")
    elif len(wrongletters) == 2:
        print("    +---+\n"
              "    |   |\n"
              "    O   |\n"
              "    |   |\n"
              "        |\n"
              "        |\n"
              "  =========\n")
    elif len(wrongletters) == 3:
        print("    +---+\n"
              "     |   |\n"
              "     O   |\n"
              "    /|   |\n"
              "         |\n"
              "         |\n"
              "   =========\n")
    elif len(wrongletters) == 4:
        print("    +---+\n"
              "     |   |\n"
              "     O   |\n"
              "    /|\  |\n"
              "         |\n"
              "         |\n"
              "   =========\n")
    elif len(wrongletters) == 5:
        print("    +---+\n"
              "     |   |\n"
              "     O   |\n"
              "    /|\  |\n"
              "    /    |\n"
              "         |\n"
              "   =========\n")
    elif len(wrongletters) == 6:
        print("    +---+\n"
              "     |   |\n"
              "     O   |\n"
              "    /|\  |\n"
              "    / \  |\n"
              "         |\n"
              "   =========\n")


def select_word():
    wlist = []
    with open('hangman_list.txt', 'r') as open_file:
        line = open_file.readline().rstrip('\n')
        while line:
            wlist.append(line)
            line = open_file.readline().rstrip('\n')
    return (wlist[random.randint(0, len(wlist))])


def print_word(wordlist, worddic):
    for letters in wordlist:
        if worddic[letters] == 0:
            print('_', end='')
        else:
            print(letters, end='')


def check_letter(wordlist, worddic, wrongletters):
    not_letter = True
    while not_letter:
        newletter = input('Please introduce a letter\n').lower()
        if newletter.isalpha():
            if len(newletter) == 1:
                not_letter = False
    if newletter in wordlist:
        if worddic[newletter] == 0:
            worddic[newletter] += 1
        else:
            print('You already enter letter {}'.format(newletter))
    else:
        if newletter in wrongletters:
            print('You already enter letter {}'.format(newletter))
        else:
            wrongletters.append(newletter)
            print('Letter {} is incorrect'.format(newletter))


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


def check_ending(worddic):
    for v in worddic.values():
        if v == 0:
            return 0
    return 1


def game_hangman():
    # Select an aleatory word
    word = select_word().lower()
    wrongletters = []
    # Create a list to keep the order of the letters in the word
    wordlist = list(word)
    # Create a dictionary to keep a value (1 if user discover the word, 0 otherwise)
    worddic = {}
    for let in word:
        worddic[let] = 0
    # game
    play = True
    while play:
        print('------------------------------------------')
        check_letter(wordlist, worddic, wrongletters)
        print_word(wordlist, worddic)
        print('')
        print('')
        print_figure(wrongletters)
        print('')
        print('Wrong letters: {}'.format(wrongletters))
        print(' ')
        end = check_ending(worddic)
        if end == 1:
            print('You won the game!')
            print('------------------------------------------')
            play = False
        else:
            if len(wrongletters) == 6:
                print('The word was: {}'.format(word))
                print('You have no more turns, you lost the game!')
                print('------------------------------------------')
                play = False
            else:
                print('You have {} guesses left'.format(6 - len(wrongletters)))
    # ask if user wants to play again
    answer = question_play_again()
    if answer == 1:
        game_hangman()
    else:
        print('Thanks for playing! See you soon!')


game_hangman()
