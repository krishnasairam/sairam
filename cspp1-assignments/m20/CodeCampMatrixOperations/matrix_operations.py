"""Matrix operations"""
def mult_matrix(m_1, m_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(m_1) == len(m_2[0]) and len(m_1[0]) == len(m_2):
        result = [[0 for row in range(len(m_1))] for col in range(len(m_2[1]))]
        for i in range(len(m_1)):
            for j in range(len(m_2[1])):
                for k in range(len(m_2)):
                    result[i][j] += int(m_1[i][k]) * int(m_2[k][j])
        return result
    print("Error: Matrix shapes invalid for mult")
    return None
def add_matrix(m_1, m_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    for i in range(len(m_1)):
        if len(m_1) == len(m_2) and len(m_1[i]) == len(m_2[i]):
            result = [[0 for row in range(len(m_1))] for col in range(len(m_2[0]))]
            result = [[int(m_1[i][j]) + int(m_2[i][j]) for j in range(len(m_1[0]))] for i in range(len(m_1))]
            return result
    print('Error: Matrix shapes invalid for addition')
    return None
def read_matrix(lis_1):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix = []
    for _ in range(0, int(lis_1[0])):
        col = input().split(' ')
        if len(col) == int(lis_1[1]):
            matrix.append(col)
        else:
            print("Error: Invalid input for the matrix")
            return None
    return matrix
def main():
    '''Main function'''
    int_row_col = input()
    lis_1 = int_row_col.split(',')
    matrix1 = read_matrix(lis_1)
    int_row_col = input()
    lis_2 = int_row_col.split(',')
    matrix2 = read_matrix(lis_2)
    if matrix1 is not None and matrix2 is not None:
        print(add_matrix(matrix1, matrix2))
        print(mult_matrix(matrix1, matrix2))
if __name__ == '__main__':
    main()
