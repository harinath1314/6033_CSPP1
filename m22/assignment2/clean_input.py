'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
re.sub(r'[^a-z\s]', '', one_str)
'''
import re

def clean_string(string):
	'''
	cleans the given string
	'''
    string = re.sub('[^a-z,0-9]','', string)
    return string

def main():
	'''
	this is th amain function
	'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
