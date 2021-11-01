# 30) Pick Word (HANGMAN PART 1)

# Write a function that picks a random word from a list of words (Sowpods dictionary)
# Sowpods = word list commonly used in word puzzles and games like Scrabble

import random

def select_word():
    wlist = []
    with open('Sowpods_list.txt', 'r') as open_file:
        line = open_file.readline().rstrip('\n')
        while line:
            wlist.append(line)
            line = open_file.readline().rstrip('\n')
    return (wlist[random.randint(0,len(wlist))])


word = select_word()
print(word)