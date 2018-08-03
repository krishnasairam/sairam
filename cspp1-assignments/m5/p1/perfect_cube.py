"""python program to find if the given number is a perfect cube or not"""
def main():
    """perfect cube"""
    x_in = int(input("Enter an integer:"))
    ans_in = 0
    while ans_in**3 < x_in:
        ans_in = ans_in + 1
    if ans_in**3 != x_in:
        print(str(x_in) +" is not a perfect cube")
    else:
        print("Cube root of "+str(x_in)+" is "+ str(ans_in))
if __name__ == "__main__":
    main()
