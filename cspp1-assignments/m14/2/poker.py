''' Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands'''
def is_straight(ranks):
    '''  straight '''
    return len(set(ranks))==5 and (max(ranks)-min(ranks)==4)
def is_flush(hand):
    suit = hand[0]
    for h_input in hand:
        if suit[1] != h_input[1]:
            return False
    return True
def card_rank(hand):
    ranks =sorted(['--23456789TJQKA'.index(c) for c,s in hand],reverse=True)
    return ranks 
def kind(ranks,n):
    for r in ranks:
        if ranks.count(r)==n:
            return r
    return 0
def two_pair(ranks):
    one = kind(ranks,2)
    ranks.remove(one)
    two = kind(ranks,2)
    if one and two:
        return (one,two)
    return None    
def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    ranks = card_ranks(hand)
    if is_straight(ranks) and is_flush(hand):
        return (8,ranks)
    if kind(ranks,4):
        return (7,kind(ranks,4),ranks)
    if kind(ranks,3) and kind(ranks,2):
        return (6,kind(ranks,3),kind(ranks,2))
    if is_flush(hand):
        return(5,ranks)
    if is_straight(hand):
        return(4,ranks)   
    if kind(ranks,3):
        return (3,kind(ranks,3),ranks)
    if two_pair(ranks):
        return(2,two_pair(ranks),ranks)
    if kind(ranks,2):
        return(1,kind(ranks,2),ranks)
    return (0,ranks)        
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
