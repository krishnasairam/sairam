"""Write a python program to find the square root of the given number"""
def main():
    """approximation square root """
    squ_are = int(input())
    eps_ilon = 0.01
    gue_ss = 0.0
    incr_ement = 0.1
    while abs(gue_ss**2 - squ_are) >= eps_ilon and gue_ss <= squ_are:
        gue_ss += incr_ement
    if abs(gue_ss**2 - squ_are) >= eps_ilon:
        print('Failed on cube root of', squ_are)
    else:
        print(gue_ss)
if __name__ == "__main__":
    main()
