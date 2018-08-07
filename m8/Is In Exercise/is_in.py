# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.

def is_in(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    length = len(aStr)
    if length == 0:
        return False
    if length == 1:
        if char == aStr[0]:
            return True
        else:
            return False
    else:
        mid=len(aStr)//2
        if char == aStr[mid]:
            return True
        elif char < aStr[mid]:
            return is_in(char, aStr[:mid])
        else:
            return is_in(char, aStr[mid:])
def main():
    data = input()
    data = data.split()
    hari = sorted(data[1])
    print(is_in((data[0]), hari))
if __name__ == "__main__":
    main()
