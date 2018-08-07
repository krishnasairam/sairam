'''This function takes in one number and returns one number.'''
def factorial_num(n_input):
    '''returns: a positive integer, the factorial of n.'''
    if n_input == 0:
        return 1
    return n_input * factorial_num(n_input - 1)
def main():
    '''enter integer'''
    int_a = input()
    print(factorial_num(int(int_a)))

if __name__ == "__main__":
    main()
