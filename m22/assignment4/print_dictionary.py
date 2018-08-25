'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    list_1 = list(dictionary.keys())
    list_1.sort()
    for i in range(len(list_1)):
    	print(list_1[i], "-", dictionary[list_1[i]], end=('\n'))

def main():
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
