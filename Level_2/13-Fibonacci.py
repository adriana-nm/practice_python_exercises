# 13) Fibonacci

# Ask user how many Fibonnaci numbers wants
# Generate this amount Fibonnaci numbers

def amount_num(text='Please introduce a number'):
    num = 0
    while num <= 0:
        num = int(input(text))
    return num

def fibonacci_serie(length):
    a =[1,1]
    if length == 1:
        print(a[0])
    elif length == 2:
        print(a)
    else:
        for long in range(2,length):
            last = a[-1] + a[-2]
            a.append(last)
        print(a)


num = amount_num()
fibonacci_serie(num)