def mult_matrix(rows,columns, m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    mat_mul = []
    for i in range(rows):
        mat_mul.append([])
    for i in range(rows):
        for j in range(columns):
            mat_mul[i].append(j)
            mat_mul[i][j] = 0
    for i in range(rows):
        for j in range(columns):
            for k in range(columns):
                mat_mul[i][j] += m1[i][k] * m2[k][j]
    return mat_mul

def add_matrix(rows, columns, m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    mat_add = []
    for i in range(rows):
        mat_add.append([])
    for i in range(rows):
        for j in range(columns):
            mat_add[i].append(j)
            mat_add[i][j] = 0
    for i in range(rows):
        for j in range(columns):
            mat_add[i][j] = m1[i][j] + m2[i][j]
    return mat_add


def read_matrix(rows, columns):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    mat = []
    inputt = input().split(' ')
    for i in range(rows):
        mat.append([])
    for i in range(rows):
        for j in range(columns):
            mat[i].append(j)
            mat[i][j] = 0
    for i in range(rows):
        for j in range(columns):
            mat[i][j] = int(inputt[j])
    return mat


def main():
    # read matrix 1
    inpu = input()
    (rows, columns) = (inpu.split(','))
    row = int(rows)
    column = int(columns)
    
    m1 = read_matrix(row, column)
    print(m1)
    # read matrix 2
    m2 = read_matrix(row, column)
    print(m2)
    # add matrix 1 and matrix 2
    m14 = add_matrix(row, column, m1, m2)
    print(m14)


    # multiply matrix 1 and matrix 2
    m3 = mult_matrix(row, column, m1, m2)
    print(m3)

if __name__ == '__main__':
    main()
