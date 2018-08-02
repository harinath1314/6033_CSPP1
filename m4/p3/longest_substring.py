'''
This a program that prints the longest substring of s, where s a string,
in which the letters occur in alphabetical order.
For example, if s = 'answer', then your program should print
Longest substring in alphabetical order is: answ
In the case of ties, print the first substring.
For example, if s = 'abcbcda', then your program should print
Longest substring in alphabetical order is: abc
'''

def main():
    '''
    give a input string
    and print the longest alphabetical sequence
    '''
    string = input()
    # the input string is in string
    count = 0
    highest = 0
    end = 0
    for i in range(len(string)-1):
        if string[i] <= string[i+1]:
            count += 1
            if count > highest:
                highest = count
                end = i + 1
        else:
            count = 0    
    sequence = end - highest
    print(string[sequence:end+1])
if __name__ == "__main__":
    main()
