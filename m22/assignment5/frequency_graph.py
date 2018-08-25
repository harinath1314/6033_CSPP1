'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''
def frequency_graph(dictionary):
    '''
    returns frequency dictionary
    '''
    list_1 = list(dictionary.keys())
    list_1.sort()
    for i in range(len(list_1)):
        dictionary[list_1[i]] = "#" * dictionary[list_1[i]]
        print(list_1[i], "-", dictionary[list_1[i]], end=('\n'))
def main():
    '''
    tiis  is the main function
    '''
    dictionary = eval(input())
    frequency_graph(dictionary)
if __name__ == '__main__':
    main()
