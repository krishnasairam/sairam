''' Exercise: eval quadratic
Write a Python function, evalQuadratic(a, b, c, x),
that returns the value of the quadratic a . x 2 + b . x + c
This function takes in four numbers and returns a single number.'''
def eval_quadartic(a_in, b_in, c_in, x_in):
    '''solves quadratic expression'''
    return a_in*x_in*x_in + b_in*x_in + c_in
def main():
    '''give the values of a_in,b_in,c_in,x_in'''
    da_ta = input()
    da_ta = da_ta.split(' ')
    da_ta = list(map(float, da_ta))
    # print(da_ta)
    for x_t in range(len(da_ta)):
        te_mp = str(da_ta[x_t]).split('.')
        if te_mp[1] == '0':
            da_ta[x_t] = int(float(str(da_ta[x_t])))
        else:
            da_ta[x_t] = da_ta[x_t]
    print(eval_quadartic(da_ta[0], da_ta[1], da_ta[2], da_ta[3]))

if __name__ == "__main__":
    main()
