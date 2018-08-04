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
    num_in = int(input())
    for num_ber in range(1, num_in+1):
        if num_ber%3 == 0 and num_ber%5 != 0:
            print("Fizz")
        elif num_ber%5 == 0 and num_ber%3 != 0:
            print("Buzz")
        elif num_ber%3 == 0 and num_ber%5 == 0:
            print("Fizz")
            print("Buzz")
        else:
            print(num_ber)

if __name__ == "__main__":
    main()
