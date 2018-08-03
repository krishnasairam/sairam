"""Guess My Number Exercise"""
def main():
    """random number"""
IN_A = 0
IN_B = 100
IN_D = int((IN_A+IN_B)/2)
ST_A = 'h'
while ST_A != 'c':
    print("Is your secret number", IN_D, "?")
    print("Enter 'h' if the guess is too high. Enter 'l' to if the guess is too low.")
    ST_A = input("Enter 'c' to if I guessed correctly")
    if ST_A == 'h':
        IN_B = IN_D
        IN_D = int((IN_A + IN_B)/2)
    if ST_A == 'l':
        IN_A = IN_D
        IN_D = int((IN_A + IN_B)/2)
    if ST_A != 'c':
        print("Sorry, I did not understand your input.")
print("your secret number is", IN_D)
print("game over")
if __name__ == "__main__":
    main()
