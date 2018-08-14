''' Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands'''
def is_straight(hand):
    card_values = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':2, '3':3,
                    '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    face_values = []
    for h in hand:
            face_values.append(card_values[h[0]])
    face_values.sort()
    for i in range(0, len(face_values)-1):
        if face_values[i+1]- face_values[i] != 1:
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
    temp = hand[0][1]
    count = 0
    for element in hand:
        if element[1] == temp:
            count += 1
        flag = bool(count == len(hand))
        return flag
def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    if is_straight(hand) and is_flush(hand):
        return 3
    elif is_flush(hand):
        return 2
    elif is_straight(hand):
        return 1
    else:
        return 0
def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.
        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation
        Output: Return the winning poker hand
    '''
    return max(hands, key=hand_rank)
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
    #for h in HANDS:
        #print(is_straight(h))
