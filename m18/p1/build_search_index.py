'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
import re
# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return list(stopwords.keys())

def word_list2(text):
    '''
    all words in a list
    '''
    test_list = []
    for one_str in text:
        one_str = re.sub(r'[^a-z\s]', '', one_str)
        one_str.split()
        test_list.append(one_str)
    return test_list

def word_list(text):
    '''
        input1 = re.sub(r'[^a-z\s]', '', input1)
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    test_list = []
    for one_str in text:
        one_str = re.sub(r'[^a-z\s]', '', one_str)
        one_str.split()
        test_list.extend(one_str)
    return test_list

def build_search_index(docs, docs2):
    '''
        Process the docs step by step as given below
    '''
    new_dict={}
    for one_doc in docs:
        for one_word in docs2:
            new_dict[one_doc]=(docs2.index(one_word), docs2.count(one_word) )
    return new_dict
        

    # initialize a search index (an empty dictionary)

    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index

# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1
    stopwords="stopwords.txt"
    stopers=load_stopwords(stopwords)
    all_wordlist_in_list=(word_list2(documents))
    all_words_in_list=(word_list(documents))
    no_stop_list=[word for word in all_words_in_list if word not in stopers]
    # call print to display the search index
    print_search_index(build_search_index(no_stop_list, all_wordlist_in_list))

if __name__ == '__main__':
    main()
