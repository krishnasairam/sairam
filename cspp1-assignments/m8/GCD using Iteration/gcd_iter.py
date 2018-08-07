'''gcd of two number'''
def gcd_iter(a_input, b_input):
    '''a_input, b_input: positive integers'''
    if a_input > b_input:
        temp = b_input
    else:
        temp = a_input
    while temp >= 1:
        if a_input % temp == 0 and b_input % temp == 0:
            break
        temp = temp - 1
    return temp
def main():
    ''' enter positive integers'''
    data = input()
    data = data.split()
    print(gcd_iter(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
