'''
this is a simple solution stating that how a computer guesses
a number which the user thinks
and keeps it a secret.
the program uses guess and check method
it uses the bisection method to guess the secret number
'''

def main():
    '''
    # now computer tries the guess and check method
    to guess the secret number
    '''
    print("ask user to set a secret number s")
    print("enter code as 'h' if your number is less than 50 ")
    print("ener code as 'a' if your number is greater than 50 ")
    print("enter code as 'r' if your number is equal to 50")
    low_level = 0
    higest_level = 100
    mid_level = ((low_level+higest_level)//2)
    while True: 
        secret = input("enter the code developed")
        if secret == "h":
            higest_level = mid_level
        if secret == "a":
            low_level = mid_level
        if secret == "r":
            break
        mid_level == ((low_level+higest_level)//2)
        print("is your number" + str(mid_level))

    print("your number is " + str(mid_level))

if __name__ == "__main__":
    main()