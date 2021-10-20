# 25) Guessing Game Two

# User will think in a number from 1-100
# Program will try to guess it. User will give feedback
# User must inform if the number is too high, too low or the correct one


def jugar():
    count = 0
    first = 0
    last = 100
    found = False
    while ((first != last) and (not found)):
        # Calculate pivot
        num = ((last-first)//2)+first
        # Ask feedback to the user
        # Call function(funcion que responda un numero)
        # If = finish
        # If low update last
        # If high update first
        print('Think of a number and I\'ll try to guess it!')
        print('My number is {}'.format(num))
        count += 1
        res = ask_feedback()
        if res == 1:
            first = num
        elif res == 2:
            last = num
        else:
            print('I guess the number!')
            print('I made {} guesses'.format(count))
            found = True

def ask_feedback():
    while True:
        usernum = input('Is my number: correct? Too low? Too high? (Respond: correct / low / high)\n').lower()
        if (usernum == 'too low') or (usernum == 'low'):
            return 1
        elif (usernum == 'too high') or (usernum == 'high'):
            return 2
        elif usernum == 'correct':
            return 0


jugar()