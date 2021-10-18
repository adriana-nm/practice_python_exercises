# 2) Odd or Even

# Ask the user for a number.
# Print if the number is odd or even.
# Extra 1: If the number is 4 print a different message.

number = input('Please introduce a number')
if int(number) == 4:
    print('The number is 4 (also even)')
elif int(number)%2 == 0:
    print('The number is even')
else:
    print('The number is odd')


# Extra 2: Follow the instructions
# Ask the user for two numbers.
# One will be the divisor and the other will be the number to be divided.
# Print if the divisor divides evenly or not


check = input('Please introduce a number')
num = input('Please introduce the divisor')
if int(check)%int(num) == 0:
    print('Divisor divides evenly')
else:
    print('Divisor doesn\'t divide evenly')