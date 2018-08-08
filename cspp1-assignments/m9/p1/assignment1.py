'''Exercise: Assignment-1'''
def is_word_guessed(secret_word, letters_guessed):
    '''letters_guessed: True and False otherwise'''
    count_word = 0
    for char_1 in secret_word:
        if char_1 in letters_guessed:
            count_word += 1
    if count_word == len(secret_word):
        return True
    return False
def main():
    '''
    Main function for the program
    '''
    user_input = input()
    if user_input:
        data = user_input.split()
        secret_word = data[0]
    else:
        data = []
        secret_word = ""
    list1 = []
    for j in range(1, len(data)):
        list1.append(data[j][0])
    print(is_word_guessed(secret_word, list1))
if __name__ == "__main__":
    main()
