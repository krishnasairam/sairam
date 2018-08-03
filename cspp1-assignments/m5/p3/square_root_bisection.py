"""python program to find the square root of the given number"""
def main():
    """square root bisection method"""
    in_p = int(input())
    ep_silon = 0.01
    l_ow = 0.0
    h_igh = in_p
    a_ns = (h_igh + l_ow)/2.0
    while abs(a_ns**2 - in_p) >= ep_silon:
        if a_ns**2 < in_p:
            l_ow = a_ns
        else:
            h_igh = a_ns
        a_ns = (h_igh + l_ow)/2.0
    print(str(a_ns))
if __name__ == "__main__":
    main()
