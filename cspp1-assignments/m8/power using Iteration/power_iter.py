'''This function takes in two numbers and returns one number.'''
def power(base, exp):
    '''returns: int or float, base^exp'''
    result = 1
    while exp > 0:
        result = result * base
        exp -= 1
    return result
def main():
    '''input base and exp'''
    data = input()
    data = data.split()
    print(power(float(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
