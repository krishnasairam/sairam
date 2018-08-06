'''Exercise: fourth power
This function takes in one number and returns one number.'''
def square(x_input):
    '''x_input: int or float.'''
def fourthPower(x_input):
    '''x_input: int or float.'''
    return x_input**4
def main():
    '''enter the number'''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(fourthPower(int(float(str(data)))))
    else:
        print(fourthPower(data))
if __name__ == "__main__":
    main()
