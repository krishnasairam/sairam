'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
def tokenize(list_in):
    '''tokenize'''
    dict_new = {}
    for i in range(len(list_in)):
        if list_in[i] not in dict_new:
            dict_new[list_in[i]] = list_in.count(list_in[i])
    return dict_new        
def main():
    '''input'''
    valid_letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789 '
    string_new = ''
    int_input = int(input())
    for _ in range(int_input):
        string_in = input()
        string_new += ' '
        for i in string_in:
            if i in valid_letters:
                string_new += i
    list_in = string_new.split()
    print(tokenize(list_in))         
if __name__ == '__main__':
    main()
