'''
    Document Distance - A plagarism calculator
'''
import math, re
STOP_FILE = 'stopwords.txt'
def similarity(input1, input2, cleande_words):
    '''
        Compute the document distance as given in the PDF
    '''
    temp1 = 0
    temp2 = 0
    temp3 = 0
    dictionary_ = {}
    for o_o_word in cleande_words:
        dictionary_[o_o_word] = [input1.count(o_o_word), input2.count(o_o_word)]
    for keys in dictionary_:
        temp1 += dictionary_[keys][0] * dictionary_[keys][1]
    for keys in dictionary_:
        temp2 += dictionary_[keys][0] **2
    for keys in dictionary_:
        temp3 += dictionary_[keys][1] **2
    return temp1/math.sqrt(temp2 * temp3)

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = []
    with open(filename, 'r') as data:
        for i in data:
            stopwords.append(i.strip())
    return stopwords


def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input1 = re.sub('[^a-z\s]', '', input1)

    clean_1 = input1.lower().split()

    input2 = input()
    input2 = re.sub('[^a-z\s]', '', input2)
    clean_2 = input2.lower().split()

    stop_words = load_stopwords(STOP_FILE)
    clean_2 = [word.strip() for word in clean_2 if word.strip() not in stop_words]
    clean_1 = [word.strip() for word in clean_1 if word.strip() not in stop_words]
    cleande_words = list(set(clean_1).union(set(clean_2)))
    print(len(cleande_words))
    print(similarity(clean_1, clean_2, cleande_words))
if __name__ == '__main__':
    main()
