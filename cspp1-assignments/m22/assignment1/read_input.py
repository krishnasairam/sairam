'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''printing string'''
    int_input = int(input())
    for _ in range(int_input):
        string = input()
        print(string)

if __name__ == '__main__':
    main()
