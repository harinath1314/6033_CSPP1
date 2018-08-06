'''
Exercise: odd

# this is a Python function, odd, that takes in one number and returns
True when the number is odd and False otherwise.

# This function returns a boolean.
'''

def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    if x%2==1:
    	return(True)
    

def main():
    data = input()
    print(odd(int(data)))

if __name__ == "__main__":
    main()
