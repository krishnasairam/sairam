def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    result = [[0 for row in range(len(m1))] for col in range(len(m2[0]))]                                            
    for i in range(len(m1)):
        for j in range(len(m1[0])): 
            for k in range(len(m2)):             
                    result[i][j] += int(m1[i][k]) * int(m2[k][j])    
    return result
def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    result = m1
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            result[i][j] = int(m1[i][j]) + int(m2[i][j])
    return result        
def read_matrix(a,b):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    if a[0] == b [0] and a[1] == b [1]: 
        return True
    return False    
def main():
    int_row_col = input()
    lis1 = int_row_col.split(',')
    matrix1 = []
    for _ in range(0,int(lis1[0])):
        col = input().split()
        matrix1.append(col)
    int_row_col = input()
    lis2 = int_row_col.split(',')
    matrix2 = []
    for _ in range(0,int(lis2[0])):
        col = input().split()
        matrix2.append(col)
    if read_matrix(lis1,lis2):
        print(add_matrix(matrix1,matrix2))
        print(mult_matrix(matrix1,matrix2))
    else:
        print("Error: Invalid input for the matrix")
if __name__ == '__main__':
    main()
