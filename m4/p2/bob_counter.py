''' this problem deals with counting of certain word repetition in a given string
for example if we give a input string as hariiharioharimyhari and ask to find the number of times hari has been repeated, and the out should come as 3
'''

def main():
    '''
    in this solution we find the number of times the word bob in a given string has been repeated
    '''
    s = input()
    number_of_bobs = 0
    # the input string is in s
    for i in range(len(s)-2):
        if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
           number_of_bobs  += 1
    print(number_of_bobs)

if __name__ == "__main__":
    main()
