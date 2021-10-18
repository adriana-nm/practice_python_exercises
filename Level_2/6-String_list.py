# 6) String List

# Request a string from the user.
# Check if the string is palindrome or not.

# Solution 1 (With .reverse() )
word = input('Please enter a word').lower()
wlist = list(word)
invertlist = wlist.copy()
invertlist.reverse()
if wlist == invertlist:
    print('The word is palindrome')
else:
    print('The word is not palindrome')

# Solution 2 (with list[] )
word = input('Please enter a word').lower()
inverse = word[::-1]
if word == inverse:
    print('The word is palindrome')
else:
    print('The word is not palindrome')