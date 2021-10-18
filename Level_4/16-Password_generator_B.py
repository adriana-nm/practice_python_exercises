# 16) Password Generator

# Write a password generator function
# Ask the user if they want a strong or weak password
# Weak password: Choose two words from a list
# Strong password: Mix of lowercase/uppercase letters, numbers & symbols
# Password should be random, generating a new password in every request


# Option B: With string tools
# string.ascii_letters
# string.digits
# string.punctuation

import string
import random

def weak_password2():
    lw = ['xylophone','dolomite','orchid','archipelago','rhinoceros']
    passw = lw[random.randint(0, 4)] + lw[random.randint(0, 4)]
    return passw

def strong_password2():
    length2 = int(input('How many digits do you want for your password?'))
    return "".join([random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length2)])

def password2():
    flag = 0
    while flag == 0:
        type_pass = input('Do you want a weak or strong password? (Introduce weak or strong)').lower()
        if type_pass == "weak":
            return weak_password2()
        elif type_pass == 'strong':
            return strong_password2()

password2()
