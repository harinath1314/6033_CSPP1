'''
this is a program which uses recursive technique
to find the factorial of the given num_ber
'''

def factorial_of_given_number(num_ber):
    '''
    n is positive integer

    returns: a positive integer, the factorial of n.
    '''
    if num_ber == 0:
        return 1
    return num_ber*factorial_of_given_number(num_ber-1)
def main():
    '''
    this is the main program
    to calculate
    the factorial
    of the given positive integer
    '''
    give_input = input()
    print(factorial_of_given_number(int(give_input)))
if __name__ == "__main__":
    main()
