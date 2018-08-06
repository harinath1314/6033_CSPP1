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
    ans=1
    for i in (num_):
        ans=i*(i+1)
    print(ans)

if __name__ == "__main__":
    main()
