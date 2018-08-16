''' Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands'''
def is_straight(hand):
    '''  straight '''
    card_values = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':2, '3':3,
                    '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    face_values = []
    for h_in in hand:
        face_values.append(card_values[h_in[0]])
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
    suit = hand[0]
    for h_input in hand:
        if suit[1] != h_input[1]:
            return False
    return True
def four_of_a_kind(hand):
    for i in range(len(hand)):
        suit = hand[i]
        count = 0
        for h_input in hand:
            if suit[0] == h_input[0]:
                count += 1
        if count == 4:
            return True
    return False
def full_house(hand):
    card_values = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':2, '3':3,
                    '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    face_values = []
    for h_in in hand:
        face_values.append(card_values[h_in[0]])
    face_values.sort()
    face = set(face_values)
    if len(face) == 2:
        return True
    return False
def Three_of_akind(hand):
    for i in range(len(hand)):
        suit = hand[i]
        count = 0
        for h_input in hand:
            if suit[0] == h_input[0]:
                count += 1
        if count == 3:
            return True
    return False
def Two_pair(hand):
    card_values = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':2, '3':3,
                    '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    face_values = []
    for h_in in hand:
        face_values.append(card_values[h_in[0]])
    face_values.sort()
    face = set(face_values)
    if len(face) == 3:
        return True
    return False
def one_pair(hand):   
    card_values = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':2, '3':3,
                    '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    face_values = []
    for h_in in hand:
        face_values.append(card_values[h_in[0]])
    face_values.sort()
    face = set(face_values)
    if len(face) == 4:
        face1 = max(face)
        lis1[face1] = hand
        lis2 = list(lis1.values())
        if lis2 == HANDS:
            hand = lis1[max(lis1.keys())]
            return True  
        return False
lis1={}
def high_card(hand):
    card_values = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':2, '3':3,'4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    face_values = []
    for h_in in hand:
        face_values.append(card_values[h_in[0]])
    face = max(face_values)
    lis1[face]=hand
    lis2 = list(lis1.values())
    if lis2 == HANDS:
        hand = lis1[max(lis1.keys())]
        return True  
    return False
      
def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    if is_straight(hand) and is_flush(hand):
        return 9
    elif four_of_a_kind(hand):
        return 8 
    elif full_house(hand):
        return 7       
    elif is_flush(hand):
        return 6
    elif is_straight(hand):
        return 5
    elif Three_of_akind(hand):
        return 4
    elif Two_pair(hand):
        return 3
    elif one_pair(hand):
        return 2
    elif high_card(hand):
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
