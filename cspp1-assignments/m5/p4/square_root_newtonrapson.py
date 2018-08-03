"""psa_intthon program to find the square root of the given number"""
def main():
    """square root"""
    ep_silon = 0.01
    in_a = int(input())
    gu_ess = in_a/2.0
    while abs(gu_ess*gu_ess - in_a) >= ep_silon:
        gu_ess = gu_ess - (((gu_ess**2) - in_a)/(2*gu_ess))
    print(str(gu_ess))
if __name__ == "__main__":
    main()
