'''
this is a program
that gives the sum of
digits of the input number
'''
def sumof_digits(input_number):
    '''
    n is positive Integer
    returns: a positive integer, the sum of digits of n.
    '''
    if input_number//10 == 0:
        return input_number
    return input_number%10 + sumof_digits(input_number//10)
def main():
    '''
    this is main program that shows
    the sum of input digits
    as output
    '''
    input_number = input()
    print(sumof_digits(int(input_number)))
if __name__ == "__main__":
    main()
