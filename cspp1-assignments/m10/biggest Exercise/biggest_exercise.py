#Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: The key with the largest number of values associated with it
    '''
    value_list = []
    count_list = []
    key_list = []
    for value in aDict:
        value_list = aDict[value]
        count_list.append(len(value_list))
        key_list.append(value)    
    return key_list[count_list.index(max(count_list))]   
def main():
    '''enter input'''
    n=input()
    aDict={}
    for i in range(int(n)):
        s=input()
        l=s.split()
        if l[0] not in aDict:
            aDict[l[0]]=[l[1]]
        else:
            aDict[l[0]].append(l[1])
    print(biggest(aDict))
if __name__ == "__main__":
    main()
