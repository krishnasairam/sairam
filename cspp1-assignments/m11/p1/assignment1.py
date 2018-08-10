'''Exercise: Assignment-1'''
def get_word_score(word, n):
    SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
    sum = 0
    for letter in word:
        if letter in SCRABBLE_LETTER_VALUES:
            sum = sum + SCRABBLE_LETTER_VALUES[letter]
    if n == len(word):      
        return sum*n + 50
    return sum*n        
def main():
    '''
    Main function for the given problem
    '''
    data = input()
    data = data.split()
    print(get_word_score(data[0],int(data[1])))
if __name__ == "__main__":
    main()
