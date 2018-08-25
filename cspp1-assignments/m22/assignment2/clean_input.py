'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
def clean_string(string_in):
    '''cleaning string'''
    string_new = ''
    valid_letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
    for i in string_in:
        if i in valid_letters:
            string_new += i
    return string_new
def main():
    '''input'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
