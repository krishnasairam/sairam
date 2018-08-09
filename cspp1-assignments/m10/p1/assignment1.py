'''Exercise : Assignment-1'''
def get_available_letters(letters_guessed):
    '''param letters_guessed: '''
    import string
    letter_count = dict((key, 0) for key in string.ascii_lowercase)
    string_new = ''
    for char in letter_count.keys():
        if char not in letters_guessed:
            string_new = string_new + char
    return string_new
def main():
    '''Main function for the given program'''
    user_input = input()
    user_input = user_input.split()
    data = []
    for char in user_input:
        data.append(char[0])
    print(get_available_letters(data))
if __name__ == "__main__":
    main()
