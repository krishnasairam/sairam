'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import string
def clean_string(string):
    string_new = ''
    letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    for i in string:
        if i in letters:
            string_new += i
    return string_new
def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
