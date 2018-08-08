'''Exercise: Assignment-2'''
def get_guessed_word(secret_word, letters_guessed):
    '''what letters in secret_word have been guessed so far.'''
    string_new = ''
    for char_1 in secret_word:
        if char_1 in letters_guessed:
            string_new += char_1
        else:
            string_new += '_'
    return string_new
def main():
    '''Main function for current assignment'''
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
    print(get_guessed_word(secret_word, list1))
if __name__ == "__main__":
    main()
