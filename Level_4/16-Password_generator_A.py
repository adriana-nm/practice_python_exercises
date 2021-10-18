# 16) Password Generator

# Write a password generator function
# Ask the user if they want a strong or weak password
# Weak password: Choose two words from a list
# Strong password: Mix of lowercase/uppercase letters, numbers & symbols
# Password should be random, generating a new password in every request

# Option A: Using as base a list of characters

letmin = ['a','b','c','d','z']
letmay = ['A','B','C','D','Z']
numeros = ['1','2','3','4','5']
caracteres = ['!','#','$','%','&']
letmin.extend(letmay)
letmin.extend(numeros)
letmin.extend(caracteres)

import random

def weak_password():
    lw = ['xylophone','dolomite','orchid','archipelago','rhinoceros']
    passw = lw[random.randint(0, 4)] + lw[random.randint(0, 4)]
    return passw

def strong_password(question='Introduce the lenght of the password'):
    ilenght = int(input(question))
    passw = []
    for position in range(1,ilenght+1):
        n = random.randrange(1,19,1)
        passw.append(letmin[n])
    return ''.join(passw)

def password():
    flag = 0
    while flag == 0:
        type_pass = input('Do you want a weak or strong password? (Introduce weak or strong)').lower()
        if type_pass == "weak":
            return weak_password()
        elif type_pass == 'strong':
            return strong_password()

password()
