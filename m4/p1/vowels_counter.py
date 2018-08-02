'''
the program is about count the number of vowels present in the given string
if you give string as hari then number of vowels = 2
'''

def main():
    s = input()
    number_of_vowels = 0
    # s is the given input
    for letter in s:
        if letter in ('a','e','i','o','u'):
            number_of_vowels += 1
    print(number_of_vowels)

if __name__ == '__main__':
    main()