'''Exercise: Assignment-2'''
def updateHand(hand, word):
    """word: string
        hand: dictionary (string -> int)    
        returns: dictionary (string -> int)"""
    for letter in word:
        if letter in hand:
            hand[letter] = hand[letter]- 1
    return hand    
def main():
	n=input()
	adict={}
	for i in range(int(n)):
		data=input()
		l=data.split()
		adict[l[0]]=int(l[1])
	data1=input()
	print(updateHand(adict,data1))

if __name__ == "__main__":
	main()