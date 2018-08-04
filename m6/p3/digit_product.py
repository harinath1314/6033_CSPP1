'''
Given a  number int_input, find the product of all the digits
example: 
	input: 123
	output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    num_= int(input())
    ans = 1
    cod = 1
    i=0
    while True:
    	i<=num_
    	ans=num_*(num_-1)
    	cod = cod*ans
    	i=i+1
    	num_ = num_-1

    print(cod)


if __name__ == "__main__":
    main()
