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
            mat.append(inputt)
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
    else:
        return False


def winner_ti_ta(tic_tac):
    x=0
    o=0
    tes=0
    if is_game_valid(tic_tac):
        for i in range(len(tic_tac)):
            x+=tic_tac[i].count('x')
            o+=tic_tac[i].count('o')
            tes+=tic_tac[i].count('.')

        if (x-o==1 or o-x==1) and tes==0:
            return 'draw'
        if x>o:
            return 'x'
        return 'o'
    else:
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











