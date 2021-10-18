# 4) Divisors

# Ask the user a number & print a list with the divisors of that number


divlist = []
numb = input('Please enter a number')
for div in range(1,int(numb)):
    if int(numb)%div == 0:
        divlist.append(div)
print(divlist)