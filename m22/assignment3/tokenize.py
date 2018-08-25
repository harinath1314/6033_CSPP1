'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string):
    '''
    returns a dictonary
    of frequency of words in input given
    '''
    token = {}
    list_2 = string.split()
    list_1 = string.split()
    list_1 = list(set(list_1))
    for i in range(len(list_1)):
        if i not in list_2:
            token[list_1[i]] = list_2.count(list_1[i])
    return token
def main():
    '''
    this is the main function
    '''
    lines = int(input())
    output = []
    for _ in range(lines):
        input_ = input()
        input_ = re.sub('[^A-Za-z0-9]+', '', input_)
        output.append(input_)
        output.append("\n")
    ''.join(output)
    inp_ = ''.join(output)
    print(tokenize(inp_))
if __name__ == '__main__':
    main()
