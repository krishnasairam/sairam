'''# Assignment-3'''

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    l = len(word)
    c = 0
    if word in wordList:
        for letters in word:
            if letters in hand:
                c += 1
    if l == c:        
        return True                       
    return False          
def main():
    word=input()
    n=int(input())
    adict={}
    for i in range(n):
        data=input()
        l=data.split()
        adict[l[0]]=int(l[1])
    l2=input().split()
    print(isValidWord(word,adict,l2))
        


if __name__== "__main__":
    main()