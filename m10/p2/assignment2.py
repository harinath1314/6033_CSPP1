'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    string_ = "abcdefghijklmnopqrstuvwxyz"
    for letter in string_:
        if letter in letters_guessed:
            string_=string_.replace(letter,'')

    return string_


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    post = len(secret_word)
    for vari_able in secret_word:
        if vari_able in letters_guessed:
            post = post-1
    if post == 0:
        return True
    return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    string = ''
    for vari_able in secret_word:
        if vari_able in letters_guessed:
            string = string + vari_able
        else:
            string = string + "_"
    return string
wordlist = loadWords()



def hangman(secret_word):
 
    word_ = len(secret_word)
    print("you are going to guess a",word_,"letter word")
    flag = 8
    letters_guessed = []
    while flag >= 1:
        print("you have",flag,"guesses")
        print("your available letters",(get_available_letters(letters_guessed)))
        user_input = input("guess the letters in secretWord ")
        if user_input not in letters_guessed:
            letters_guessed.append(user_input)
            if user_input in secret_word :
                print("good guess",get_guessed_word(secret_word, letters_guessed))
            else:
                print("oops you have put leg on banana - ",get_guessed_word(secret_word, letters_guessed))
                flag -= 1
            
            if secret_word == get_guessed_word(secret_word, letters_guessed):
                break
        else:
            print("please select other letter")
        print("---------------------------------")
    if secret_word == get_guessed_word(secret_word, letters_guessed):
        print()
        print("$$$$$$$$$$$you are the winner$$$$$$$$$$$$", "your secretword is   ",secret_word)
    else:
        print("you get out of the game ","the secretWord is ",secret_word)

            
def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)


if __name__ == "__main__":
    main()
