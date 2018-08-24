'''
tic_tac_toe winner selection
'''
def read_matrix():
    '''
    reads a matrix
    '''
    rows = 3
    mat = []
    for i in range(rows):
        inputt = input().split(' ')
        if inputt.count('x') + inputt.count('o') + inputt.count('.') == 3:
            mat.append(inputt)
        else:
            print('invalid input')
            return False
    return mat
def is_game_valid(tic_tac):
    '''
    shows whether matrix is valid or not
    '''
    temp_, x_co, o_co = 0, 0, 0
    for i in range(len(tic_tac)):
        x_co += tic_tac[i].count('x')
        o_co += tic_tac[i].count('o')
        if len(set(tic_tac[i])) == 1:
            temp_ += 1
    if temp_ <= 1 and (x_co - o_co) != 3:
        return True
    return False
def winner_ti_ta(tic_tac):
    '''
    outputs the winner
    '''
    x_i, o_i, tes_i = 0, 0, 0
    if is_game_valid(tic_tac):
        for i in range(len(tic_tac)):
            x_i += tic_tac[i].count('x')
            o_i += tic_tac[i].count('o')
            tes_i += tic_tac[i].count('.')
        if (x_i - o_i == 1 or o_i - x_i == 1) and tes_i == 0:
            return 'draw'
        if x_i > o_i:
            return 'x'
        return 'o'
    return 'invalid game'
def main():
    '''
    the main function starts here
    '''
    tic_tac = read_matrix()
    if tic_tac:
        print(winner_ti_ta(tic_tac))
if __name__ == '__main__':
    main()
