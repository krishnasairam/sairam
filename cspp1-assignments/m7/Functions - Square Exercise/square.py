'''This function takes in one number and returns its square.'''
def square(x_sq):
    '''x_sq: int or float.'''
    x_sq = x_sq*x_sq
    return x_sq
def main():
    ''' Your code here Correct'''
    da_ta = input()
    da_ta = float(da_ta)
    te_mp = str(da_ta).split('.')
    if te_mp[1] == '0':
        print(square(int(float(str(da_ta)))))
    else:
        print(square(da_ta))
if __name__ == "__main__":
    main()
