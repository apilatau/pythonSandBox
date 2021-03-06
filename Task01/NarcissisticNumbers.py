def print_narcissistic_numbers(minNumber, maxNumber):
    input_list = list(range(minNumber, maxNumber + 1))
    for input_Item in input_list:
        if input_Item == narcissistic_function(input_Item):
            print(input_Item, end=" ")


def n_of_digits(num):
    i = 0
    while num > 0:
        num //= 10
        i += 1
    return i


def narcissistic_function(num):
    i = n_of_digits(num)
    s = 0    
    while num > 0:
        digit = num % 10
        num //= 10
        s += pow(digit, i)        
    return s

print_narcissistic_numbers(1, 1000)