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
    print(' '.join(is_high_card(HANDS)))
