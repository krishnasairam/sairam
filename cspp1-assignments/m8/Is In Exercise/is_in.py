'''This function takes in two arguments character and String.'''
def isIn(char, a_str):
    '''returns: True if char is in aStr; False otherwise'''
    length_str = len(a_str)
    middle = length_str//2
    if  length_str == 0:
        return False
    if length_str == 1:
        if char == a_str:
            return True
        else:
            return False
    if a_str[middle] == char:
        return True        
    elif a_str[middle] > char:
        return isIn(char,a_str[0:middle])
    elif a_str[middle]<char:
     return isIn(char,a_str[middle:length_str+1])      
def main():
    '''enter input'''
    data = input()
    data = data.split()
    print(isIn((data[0][0]), data[1]))
    
if __name__ == "__main__":
    main()