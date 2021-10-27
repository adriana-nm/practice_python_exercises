# 28) Max of Three

# Create a function that takes as input 3 variables
# Must return the largest of the three
# Don't use the function max()

def max_of_three():
    varA = int(input('Please introduce variable 1'))
    varB = int(input('Please introduce variable 2'))
    varC = int(input('Please introduce variable 3'))
    if varA > varB:
        if varB > varC:
            return varA
        else:
            if varA > varC:
                return varA
            else:
                return varC
    else:
        if varB > varC:
            return varB
        else:
            return varC

max_of_three()