'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
def is_four_of_kind(hand):
    '''
    input is a hand of five cards
    output is true if four cards have same face value
    '''
    test_list = []
    freq_dict = []
    for card in hand:
        test_list.append(card[0])
    for x_s in test_list:
        freq_dict.append(test_list.count(x_s))
    if max(freq_dict) >= 4:
        return True
    return False
def is_full_house(hand):
    '''
    input set of cards
    ouput true if 2 cards and 3 cards are of same face value
    '''
    test_list = []
    freq_dict = []
    for card in hand:
        test_list.append(card[0])
    for dani in test_list:
        freq_dict.append(test_list.count(dani))
    sorted(freq_dict)
    if freq_dict == [2, 3]:
        return True
    return False
def is_three_of_kind(hand):
    '''
    input is a hand of five cards
    output is true if four cards have same face value
    '''
    test_list = []
    freq_dict = []
    for card in hand:
        test_list.append(card[0])
    for danis in test_list:
        freq_dict.append(test_list.count(danis))
    if max(freq_dict) == 3:
        return True
    return False
def is_two_pair(hand):
    '''
    if input set of cards contains two pairs of cards
    with same facevalue
    output id true
    '''
    test_list = []
    for card in hand:
        test_list.append(card[0])
    if len(set(test_list)) == 3:
        return True
    return False
def is_one_pair(hand):
    '''
    if input set of cards contains only pairs of cards
    with same facevalue
    output id true
    '''
    test_list = []
    test_list2 = []
    for card in hand:
        test_list.append(card[0])
    for num_freq in test_list:
        if test_list.count(num_freq)==2:
            test_list2.append(num_freq)
    if len(test_list2)==0:
        return False
    return ,max(test_list2)
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
    test_list = []
    for every in hand:
        if every[0] == 'A':
            test_list.append(int(Converters[every[0]]))
        elif every[0] == 'J':
            test_list.append(int(Converters[every[0]]))
        elif every[0] == 'Q':
            test_list.append(int(Converters[every[0]]))
        elif every[0] == 'K':
            test_list.append(int(Converters[every[0]]))
        elif every[0] == 'T':
            test_list.append(int(Converters[every[0]]))
        else:
            test_list.append(int(every[0]))
    test_list.sort()
    for i in range(len(test_list) - 1):
        if test_list[i + 1] == test_list[i] + 1:
            pass
        else:
            return False
    return True
def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    test_list = []
    for card in hand:
        test_list.append(card[1])
    if test_list.count(test_list[0]) == len(test_list):
        return True
    return False

def is_high_card(hand):
    '''
    returns the hand with high card value
    '''
    test_list = []
    for card in hand:
        if card[0] in ['J', 'K', 'Q', 'A', 'T']:
            test_list.append(Converters[card[0]]/int(10))
        else:
            test_list.append(int(card[0])/int(10))
    return max(test_list)/100

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    if is_flush(hand) and is_straight(hand):
        return 9
    elif is_four_of_kind(hand):
        return 8
    elif is_full_house(hand):
        return 7
    elif is_straight(hand):
        return 5
    elif is_flush(hand):
        return 6
    elif is_three_of_kind(hand):
        return 4
    elif is_two_pair(hand):
        return 3
    elif is_one_pair(hand):
        return (1, is_one_pair(hand))
    return is_high_card(hand)

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''
    return max(hands, key=hand_rank)
Converters = {'A':14, 'J':13, 'Q':12, 'K':11, 'T':10}

if __name__ == "__main__":
    COUNT = int(input())
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    print(' '.join(poker(HANDS)))