'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    """fizz buzz"""
    n_um = int(input())
    i_x = 1
    while i_x <= n_um:
        if i_x % 3 == 0 and i_x % 5 == 0:
            print("Fizz")
            print("Buzz")
        elif i_x % 3 == 0:
            print("Fizz")
        elif i_x % 5 == 0:
            print("Buzz")
        else:
            print(i_x)
        i_x += 1

if __name__ == "__main__":
    main()
