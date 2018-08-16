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
    for card in hand:
        test_list.append(card[0])
    if len(set(test_list)) == 4:
        return True
    return False
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
    converters = {'A':14, 'J':13, 'Q':12, 'K':11, 'T':10}
    test_list = []
    for every in hand:
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
def test_hand_value(hand):
    test_list=[]
    for card in hand:
        test_list.append(card[0])
    return max(test_list)
def is_high_card(hands):
    '''
    returns the hand with high card value
    '''
    return max(hands, key=test_hand_value)


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
        return 2
    return 0
    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''
    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)
converters = {'A':14, 'J':13, 'Q':12, 'K':11, 'T':10}
if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
    if poker(HANDS) == 0:
        print(' '.join(is_high_card(HANDS)))

