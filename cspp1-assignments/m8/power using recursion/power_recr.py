'''This function takes in two numbers and returns one number.'''
def recur_power(base, exp):
    '''base: int or float.'''
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    return base * recur_power(base, exp-1)
def main():
    '''enter input'''
    data = input()
    data = data.split()
    print(recur_power(float(data[0]), int(data[1])))
if __name__ == "__main__":
    main()