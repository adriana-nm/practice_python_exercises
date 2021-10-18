# 15) Reverse Word Order

# Write a function
# Ask the user for a long string containing multiple words
# Print the sentence backwards


#Solution 1: With list[]
def reverse_string1():
    string = input('Please enter a long sentence')
    words = string.split(' ')
    return words[::-1]

reverse_string1()


#Solution 2: With .reverse()
def reverse_string2():
    string = input('Please enter a long sentence')
    words = string.split(' ')
    words.reverse()
    return words

reverse_string2()