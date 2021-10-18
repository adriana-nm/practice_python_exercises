# 1) Character Input

# Ask name and age of user
# Print out a message informing when they will turn 100 years old
# Extra 1: Request them another number/age continuously
# Extra 2: Print out the messages on separate lines

data= input('Please enter your name and age')
wlist = data.split(' ')
year100 = 2021+ (100 -(int(wlist[-1])))
print('On {}, you will turn 100 years old'.format(year100))
while True:
    age = input('Please enter a new age\n')
    if int(age) == 0: break
    else:
        year100 = 2021 + (100 - (int(age)))
        print('On {}, you will turn 100 years old'.format(year100))