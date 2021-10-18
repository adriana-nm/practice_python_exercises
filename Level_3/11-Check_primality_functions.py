# 11) Check Primality Functions

# Ask the user a number. Determine if the number is prime or not.

def get_number(question='Please provide a number:'):
    return int(input(question))

def prime(number):
    flagp = 0
    if (number <= 0) or (number == 1):
        flagp += 1
    for num in range (2,number):
        if number%num == 0:
            flagp += 1
    if flagp == 0:
        return print('The number is prime')
    else:
        return print('The number is not prime')

def is_num_prime():
    data = get_number()
    prime(data)

is_num_prime()
