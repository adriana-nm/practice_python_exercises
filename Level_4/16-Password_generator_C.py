# 16) Password Generator

# Write a password generator function
# Ask the user if they want a strong or weak password
# Weak password: Choose two words from a list
# Strong password: Mix of lowercase/uppercase letters, numbers & symbols
# Password should be random, generating a new password in every request


# Option C: With string tool + At least (1 low, 1 upper, 1 num & 1 symbol)

import string
import random

def weak_password3():
    lw = ['xylophone','dolomite','orchid','archipelago','rhinoceros']
    passw = lw[random.randint(0, 4)] + lw[random.randint(0, 4)]
    return passw

def strong_password3():
    spflag = 0
    numflag = 0
    while numflag == 0:
        length3 = int(input('How many digits do you want for your password?'))
        if length3 >3:
            while spflag == 0:
                passw = "".join(
                    [random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length3)])
                upper = [i for i in passw if ((i.isupper()) and (i in string.ascii_letters))]
                lower = [i for i in passw if ((i.islower()) and (i in string.ascii_letters))]
                digit = [i for i in passw if (i in string.digits)]
                symbol = [i for i in passw if (i in string.punctuation)]
                if (bool(upper) and bool(lower) and bool(digit) and bool(symbol)) is True:
                    spflag = 1
            return passw

def password3():
    flag = 0
    while flag == 0:
        type_pass = input('Do you want a weak or strong password? (Introduce weak or strong)').lower()
        if type_pass == "weak":
            return weak_password3()
        elif type_pass == 'strong':
            return strong_password3()

password3()