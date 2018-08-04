'''
this is a program that prints each number from 1 to N numbers on a new line.
for numbers which are multipe of 3 it prints "Fizz" instead of number.
and for number which is multipe of 3 it prints "Buzz" instead of number.
For numbers which are multiples of both 3 and 5, it prints "FizzBuzz" instead of the number.
'''
def main():
    '''
    Read number from the input, store it in variable N.
    '''
    N = int(input())
    for x in range(1,N+1):
        if x%3 == 0 and x%5 != 0:
            print("Fizz")
        elif x%5 == 0 and x%3 != 0:
            print("Buzz")
        elif x%3 == 0 and x%5 == 0:
            print("Fizz")
            print("Buzz")
        else:
            print(x)
        

if __name__ == "__main__":
    main()
