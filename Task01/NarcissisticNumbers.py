import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main():
    print_NarcissisticNumbers(1,1000)

def print_NarcissisticNumbers(minNumber,maxNumber):
    input_list = list(range(minNumber,maxNumber,1))
    for input_Item in input_list:
        if input_Item == narcissistic_function(input_Item):
            print(input_Item, end =" ")

def n_of_digits(num):
    i = 0
    while num > 0:
        num //= 10
        i+=1

    return i

def narcissistic_function(num):
    i = n_of_digits(num)
    s = 0
    
    while num > 0:
        digit = num % 10
        num //= 10
        s += pow(digit, i)        
    return s

if __name__=="__main__":
    main()

