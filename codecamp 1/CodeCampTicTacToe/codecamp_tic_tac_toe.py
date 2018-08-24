'''
this is a program for
tic_tac_toe winner
'''
def read_matrix():
    rows = 3
    columns = 3
    mat = []
    for i in range(rows):
        mat.append([])
    for i in range(rows):
        for j in range(columns):
            mat[i].append(j)
            mat[i][j] = '.'
    print(mat)
    for i in range(rows):
        inputt = input().split(' ')
        if inputt.count('x')+inputt.count('o')+inputt.count('.') == 3:
            for j in range(columns):
                mat[i][j] = int(inputt[j])
        print('invalid input')
        return False
    return mat

import re
def main():
    '''
    the main function starts here
    '''
    #read the inputs
    read_matrix()
    if read_matrix:
        pass


if __name__ == '__main__':
    main()











