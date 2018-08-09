'''Exercise : Assignment-2'''
import random
WORD_LIST_FILENAME = "words.txt"
def loadWords():
    """Returns a list of valid words. Words are strings of lowercase letters."""
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORD_LIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print("  ", len(word_list), "words loaded.")
    return word_list
def chooseWord(word_list):
    """word_list (list): list of words (strings)"""
    return random.choice(word_list)
word_list = loadWords()
import random
def loadWords():
    WORD_LIST_FILENAME = "words.txt"
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORD_LIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print("  ", len(word_list), "words loaded.")
    return word_list
def chooseWord(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = loadWords()

def isWordGuessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    count_word = 0
    for char_1 in secret_word:
        if char_1 in letters_guessed:
            count_word += 1
    if count_word == len(secret_word):
        return True
    return False
def getGuessedWord(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secret_word have been guessed so far.'''
    string_new = ''
    for char_1 in secret_word:
        if char_1 in letters_guessed:
            string_new += char_1
        else:
            string_new += '_'
    return string_new
def getAvailableLetters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    letter_count = dict((key, 0) for key in string.ascii_lowercase)
    string_new = ''
    for char in letter_count.keys():
        if char not in letters_guessed:
            string_new = string_new + char
    return string_new
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the secret_word contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    intro = str(len(secret_word))
    letters_guessed = []
    guess = str
    mistakes_made = 8
    word_guessed = False
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+ str(intro) +' letters long.')
    print('------------')
    while mistakes_made > 0 and mistakes_made <= 8 and word_guessed is False:
        if secret_word == getGuessedWord(secret_word, letters_guessed):
            word_guessed = True
            break
        print('You have ' + str(mistakes_made) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(letters_guessed))
        guess = input('Please guess a letter: ').lower()
        if guess in secret_word:
            if guess in letters_guessed:
                print("Oops! You've already guessed that letter: " + getGuessedWord(secret_word, letters_guessed))
                print('------------')
            else:
                letters_guessed.append(guess)
                print('Good guess: ' + getGuessedWord(secret_word, letters_guessed))
                print('------------')
        else:
            if guess in letters_guessed:
                print("Oops! You've already guessed that letter: " + getGuessedWord(secret_word, letters_guessed))
                print('------------')
            else:
                letters_guessed.append(guess)
                mistakes_made -= 1
                print('Oops! That letter is not in my word: ' + getGuessedWord(secret_word, letters_guessed))
                print('------------')
    if word_guessed == True:
        print('Congratulations, you won!')
    elif mistakes_made == 0:
        print('Sorry, you ran out of guesses. The word was ' + secret_word)
def main():
    '''
    Main function for the given program 
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secret_word while you're testing)
    '''
    secret_word = chooseWord(word_list).lower()
    hangman(secret_word)
if __name__ == "__main__":
    main()
