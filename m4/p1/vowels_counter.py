'''
the program is about count the number of vowels present in the given string
if you give string as hari then number of vowels = 2
'''

def main():
	'''
	if we give some input string we get the number of vowels present in it
	'''
    string = input()
    number_of_vowels = 0
    # s is the given input
    for letter in string:
        if letter in ('a', 'e', 'i', 'o', 'u'):
            number_of_vowels += 1
    print(number_of_vowels)

if __name__ == '__main__':
    main()
