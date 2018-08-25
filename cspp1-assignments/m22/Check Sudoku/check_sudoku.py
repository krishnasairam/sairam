'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    count = 0
    for row in sudoku:
        if len(set(row)) == 9 and int(max(row))-int(min(row)) == 8:
            count += 1
    for i in range(0, 9):
        lis1 = []
        for j in range(0, 9):
            lis1.append(sudoku[j][i])
        if len(set(lis1)) == 9 and int(max(lis1))-int(min(lis1)) == 8:
            count += 1
    for _ in range(0, 9):
        lis1 =[]
        lis2 =[]
        lis3 =[]
        for i in range(0, 3):
            for j in range(0, 3):
                lis1.append(sudoku[i][j])
            for j in range(3, 4):
                lis2.append(sudoku[i][j])
            for j in range(4, 9):
                lis3.append(sudoku[i][j])
        for i in range(3, 4):
            for j in range(0, 3):
                lis1.append(sudoku[i][j])
            for j in range(3, 4):
                lis2.append(sudoku[i][j])
            for j in range(4, 9):
                lis3.append(sudoku[i][j])
        for i in range(4, 9):
            for j in range(0, 3):
                lis1.append(sudoku[i][j])
            for j in range(3, 4):
                lis2.append(sudoku[i][j])
            for j in range(4, 9):
                lis3.append(sudoku[i][j])
        if len(set(lis1)) == 9 and int(max(lis1))-int(min(lis1)) == 8:
            count += 1
        if len(set(lis2)) == 9 and int(max(lis2))-int(min(lis2)) == 8:
            count += 1
        if len(set(lis3)) == 9 and int(max(lis3))-int(min(lis3)) == 8:
            count += 1
    if count == 45:
        return True
    return False
def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
