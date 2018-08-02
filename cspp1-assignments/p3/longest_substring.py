"""Finding the substring"""

def main():
    """to print the longest alphabetical series"""
    count_x = 0
    g_x = 0
    m_x = 0
    v_x = input()
    for i in range(len(v_x)-1):
        if v_x[i] <= v_x[i+1]:
            count_x += 1
        else:
            count_x = 0
        if g_x < count_x:
            g_x = count_x
            m_x = i
    x_m = m_x - g_x + 1
    print(v_x[x_m:x_m+g_x+1])
if __name__ == "__main__":
    main()
