# 32) Hangman (HANGMAN PART 3)

# Write the complete game of Hangman
# User only has 6 incorrect guesses (head, body, 2 legs, 2 arms)
# Inform the user how many guesses he has left
# If user guess a letter that they already guessed, don't count them
# When player win or loses, let them start a new game

import random


MAX_INCORRECT_GUESSES = 6
KEEP_PLAYING = 0
WORD_GUESSED = 1
END_GAME = 1


def print_figure(wrong_letters):
    if len(wrong_letters) == 0:
        print("  +---+\n"
              "  |   |\n"
              "      |\n"
              "      |\n"
              "      |\n"
              "      |\n"
              "=========\n")
    elif len(wrong_letters) == 1:
        print("  +---+\n"
              "  |   |\n"
              "  O   |\n"
              "      |\n"
              "      |\n"
              "      |\n"
              "=========\n")
    elif len(wrong_letters) == 2:
        print("  +---+\n"
              "  |   |\n"
              "  O   |\n"
              "  |   |\n"
              "      |\n"
              "      |\n"
              "=========\n")
    elif len(wrong_letters) == 3:
        print("  +---+\n"
              "  |   |\n"
              "  O   |\n"
              " /|   |\n"
              "      |\n"
              "      |\n"
              "=========\n")
    elif len(wrong_letters) == 4:
        print("  +---+\n"
              "  |   |\n"
              "  O   |\n"
              " /|\  |\n"
              "      |\n"
              "      |\n"
              "=========\n")
    elif len(wrong_letters) == 5:
        print("  +---+\n"
              "  |   |\n"
              "  O   |\n"
              " /|\  |\n"
              " /    |\n"
              "      |\n"
              "=========\n")
    elif len(wrong_letters) == 6:
        print("  +---+\n"
              "  |   |\n"
              "  O   |\n"
              " /|\  |\n"
              " / \  |\n"
              "      |\n"
              "=========\n")


def select_word():
    game_words = []
    with open('hangman_list.txt', 'r') as open_file:
        line = open_file.readline().rstrip('\n')
        while line:
            game_words.append(line)
            line = open_file.readline().rstrip('\n')
    return game_words[random.randint(0, len(game_words))]


def print_word(letters_to_guess, correct_letters):
    for letters in letters_to_guess:
        if letters in correct_letters:
            print(letters, end='')
        else:
            print("_", end='')
    print('\n')


def check_letter(letters_to_guess, correct_letters, wrong_letters):
    not_letter = True
    while not_letter:
        new_letter = input('Please introduce a letter\n').lower()
        if new_letter.isalpha():
            if len(new_letter) == 1:
                not_letter = False
    if new_letter in letters_to_guess:
        if new_letter in correct_letters:
            print('You already enter letter {}'.format(new_letter))
        else:
            correct_letters.add(new_letter)
    else:
        if new_letter in wrong_letters:
            print('You already enter letter {}'.format(new_letter))
        else:
            wrong_letters.append(new_letter)
            print('Letter {} is incorrect'.format(new_letter))


def question_play_again():
    while True:
        response = input('Do you want to play again?\n'
                         'Introduce yes or no\n').lower()
        if response == "yes":
            return KEEP_PLAYING
        elif response == "no":
            return END_GAME
        else:
            print('The answer is not clear')


def game_status(letters_to_guess, correct_letters):
    for letter in letters_to_guess:
        if letter not in correct_letters:
            return KEEP_PLAYING
    return WORD_GUESSED


def display_hangman_info(correct_letters, letters_to_guess, wrong_letters):
    print('------------------------------------------')
    check_letter(letters_to_guess, correct_letters, wrong_letters)
    print('')
    print_figure(wrong_letters)
    print_word(letters_to_guess, correct_letters)
    print('Wrong letters: {}'.format(wrong_letters))
    print(' ')


def game_hangman():
    # Select an aleatory word
    word = select_word().lower()
    letters_to_guess = list(word)
    wrong_letters = []
    correct_letters = set()

    # game start
    play = True
    while play:
        display_hangman_info(correct_letters, letters_to_guess, wrong_letters)
        if game_status(letters_to_guess, correct_letters) == WORD_GUESSED:
            print('You won the game!')
            print('------------------------------------------')
            play = False
        else:
            if len(wrong_letters) == MAX_INCORRECT_GUESSES:
                print('The word was: {}'.format(word))
                print('You have no more turns, you lost the game!')
                print('------------------------------------------')
                play = False
            else:
                print('You have {} guesses left'.format(MAX_INCORRECT_GUESSES - len(wrong_letters)))
    
    # ask if user wants to play again
    answer = question_play_again()
    if answer == KEEP_PLAYING:
        game_hangman()
    else:
        print('Thanks for playing! See you soon!')


game_hangman()
