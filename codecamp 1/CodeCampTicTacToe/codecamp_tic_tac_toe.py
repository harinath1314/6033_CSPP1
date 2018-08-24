'''
this is a program for
tic_tac_toe winner
'''
def read_matrix():
    rows = 3
    columns = 3
    mat = []
    for i in range(rows):
        inputt = input().split(' ')
        if inputt.count('x')+inputt.count('o')+inputt.count('.') == 3:
            for j in range(columns):
                mat[i][j] = (inputt[j])
        else:
            print('invalid input')
            return False
    return mat
def is_game_valid(tic_tac):
    temp = 0
    for i in range(len(tic_tac)):
        if len(set(tic_tac[i])) == 1:
            temp+=1
    if temp <= 1:
        return True
    return False


def winner_ti_ta(tic_tac):
    if is_game_valid(tic_tac):
        return None
    else:
        return 'invalid game'



def main():
    '''
    the main function starts here
    '''
    #read the inputs
    tic_tac = read_matrix()
    if tic_tac:
        print(winner_ti_ta(tic_tac))



if __name__ == '__main__':
    main()











