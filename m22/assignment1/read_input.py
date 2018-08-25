'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    lines = int(input())
    output=[]
    for line_ in range(lines):
    	output.append(input())
    	output.append("\n")
    	''.join(output)
    print(''.join(output))


if __name__ == '__main__':
    main()
