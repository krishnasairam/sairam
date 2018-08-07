'''This function takes in two numbers and returns one number.'''
def gcdRecur(a, b):
    '''a, b: positive integer'''
    if b != 0:
        return gcdRecur(b,a % b);
    else:
        return a   
def main():
    '''enter input are not 0'''
    data = input()
    data = data.split()
    print(gcdRecur(int(data[0]),int(data[1])))

if __name__== "__main__":
    main()