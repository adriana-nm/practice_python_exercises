# 31) Guess Letters (HANGMAN PART 2)

# User must enter a letter
# It must be displayed if letter is correct and where in the unknown word
# If it's incorrect inform it to the user
# Avoid that user enters incorrectly 2 times the same letter


# Code Steps:
# Graph function:
#       Provide the word, in spaces or letter
# Check letter function:
#       Request input from user
#       Check if letter has been entered before (display a message)
#       Check if letter is/is not in the word
#       Print an appropriate message
# Print the graph function after every letter

# Need a list of the word with the correct order
# Need a dictionary to know if the letter has been discovered or not

# 0 not been discovered, 1 discovered


def print_word():
    for letters in wordlist:
        if worddic[letters] == 0:
            print('_', end='')
        else:
            print(letters,end='')


def check_letter():
    newletter = input('Please introduce a letter')
    if newletter in wordlist:
        worddic[newletter] += 1
    else:
        wrongletters.append(newletter)
        print('Letter {} is incorrect'.format(newletter))


def check_ending():
    for v in worddic.values():
        if v == 0:
            return 0
    return 1


word = 'PELLICANO'.lower()
wrongletters = []
wordlist = list(word)
worddic = {}
for let in word:
    worddic[let] = 0
play = True
while play:
    check_letter()
    print_word()
    print('')
    print('Wrong letters: {}'.format(wrongletters))
    print(' ')
    end = check_ending()
    if end == 1:
        play = False