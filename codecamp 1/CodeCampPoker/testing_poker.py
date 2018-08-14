def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    test_list=[]
    converters={'A':14,'J':13,'Q':12,'K':11,'T':10}
    for card in HANDS:
        for every in card:
            if every[0] == 'A':
                test_list.append(int(converters[every[0]]))
            elif every[0] == 'J':
                test_list.append(int(converters[every[0]]))
            elif every[0] == 'Q':
                test_list.append(int(converters[every[0]]))
            elif every[0] == 'K':
                test_list.append(int(converters[every[0]]))
            elif every[0] == 'T':
                test_list.append(int(converters[every[0]]))
            else:
                test_list.append(int(every[0]))
        test_list.sort()
        print(test_list)
        for i in range (len(test_list)-1):
            if test_list[i+1]==test_list[i]+1:
                return True 
            else:
                return False
def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    test_list=[]
    for card in HANDS:
        for every in card:
            test_list.append(every[1])
        if test_list.count(test_list[0])==len(test_list):
            return True
        else:
            return False

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    if is_flush(hand) and is_straight(hand):
        return 3
    elif is_flush:
        return 2
    elif is_straight:
        return 1
    else:
        return 0



if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    print(hand_rank(HANDS))