'''
    Tiny Search Engine - Part 1 - Build a search index
    Here is the sample format of the output
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],..}
'''
import re
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return list(stopwords.keys())

def word_list2(documents):
    '''
    all words in a list
    '''
    test_list = []
    for one_str in documents:
        one_str = re.sub(r'[^a-z\s]', '', one_str)
        new_list = one_str.split()
        test_list.append(new_list)
    return test_list

def word_list(documents):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    test_list = []
    for one_str in documents:
        one_str = re.sub(r'[^a-z\s]', '', one_str)
        test_list.extend(one_str.split())
    return test_list

def build_search_index(docs, docs2):
    '''
        Process the docs step by step as given below
    '''
    new_dict = {}
    for one_doc in docs:
        for one_set in docs2:
            new_dict[one_doc] = [(docs2.index[one_set], docs2.count(one_doc))]
    return new_dict

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
        documents.append(input().lower())
        i += 1
    print(documents)
    stopwords = "stopwords.txt"
    stopers = load_stopwords(stopwords)
    print(stopers)
    all_wordlist_in_list = (word_list2(documents))
    all_words_in_list = (word_list(documents))
    print(all_words_in_list)
    print(all_wordlist_in_list)

    no_stop_list = [word for word in all_words_in_list if word not in stopers]
    print(no_stop_list)
    # call print to display the search index
    print(build_search_index(no_stop_list, all_wordlist_in_list))

if __name__ == '__main__':
    main()
