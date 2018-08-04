'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    pro_duct = 1
    a_x = 1
    if int_input == 0:
        print ('0')
    else:         
        while int_input != 0:
            a_x = int_input % 10
            pro_duct = pro_duct * a_x
            int_input = int_input // 10
        if int_input < 0:
            pro_duct = -pro_duct
        print(pro_duct)
if __name__ == "__main__":
    main()
