'''
this pyhton file performs the multoplication and addition of
two matrices
'''
def mult_matrix(m1_, m2_):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''

    if len(m1_[0]) == len(m2_):
        mat_mul = []
        for i in range(len(m1_)):
            mat_mul.append([])
        for i in range(len(m1_)):
            for j in range(len(m2_[0])):
                mat_mul[i].append(j)
                mat_mul[i][j] = 0
        for i in range(len(m1_)):
            for j in range(len(m2_[0])):
                for k in range(len(m1_[0])):
                    mat_mul[i][j] += m1_[i][k] * m2_[k][j]
        return mat_mul
    else:
        print("Error: Matrix shapes invalid for mult")
        return None
def add_matrix(rows, columns, m1_, m2_):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    try:
        if len(m1_) == len(m2_) and len(m1_[0]) == len(m2_[0]):
            mat_add = []
            for i in range(rows):
                mat_add.append([])
            for i in range(rows):
                for j in range(columns):
                    mat_add[i].append(j)
                    mat_add[i][j] = 0
            for i in range(rows):
                for j in range(columns):
                    mat_add[i][j] = m1_[i][j] + m2_[i][j]
            return mat_add
        print("Error: Matrix shapes invalid for addition")
        return None 
    except Exception as e:
        print("Error: Matrix shapes invalid for addition")
def read_matrix(rows, columns):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    try:
        mat = []
        for i in range(rows):
            mat.append([])
        for i in range(rows):
            for j in range(columns):
                mat[i].append(j)
                mat[i][j] = 0
        for i in range(rows):
            inputt = input().split(' ')
            for j in range(columns):
                assert len(inputt) == len(mat[0])
                mat[i][j] = int(inputt[j])
        return mat
    except:
        raise Exception("Error: Invalid input for the matrix")


def main():
    '''
    the main funtion
    '''
    # read matrix 1
    try:
        inpu = input()
        (rows, columns) = (inpu.split(','))
        row = int(rows)
        column = int(columns)
        m1_ = read_matrix(row, column)
        # read matrix 2
        inpu = input()
        (rows, columns) = (inpu.split(','))
        row = int(rows)
        column = int(columns)
        m2_ = read_matrix(row, column)
        # add matrix 1 and matrix 2
        m14_ = add_matrix(row, column, m1_, m2_)
        print(m14_)


        # multiply matrix 1 and matrix 2
        m3_ = mult_matrix(m1_, m2_)
        print(m3_)
    except Exception as e_o:
        print(e_o)



if __name__ == '__main__':
    main()
