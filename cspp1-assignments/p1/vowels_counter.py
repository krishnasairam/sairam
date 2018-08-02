"""vowels"""

def main():
    """Vowel"""
    str_inp = input()
    v_inp = 0
    c_inp = 0
    for i in str_inp:
        if i in 'aeiou':
            v_inp = v_inp + 1
        else:
            c_inp = c_inp + 1
    print(v_inp)

if __name__ == "__main__":
    main()
