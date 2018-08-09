'''
#the biggest key solution
'''
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    big = 0
    temp = []
    temp1 = []
    for vari_ in aDict:
        sum_ = len(aDict[vari_])
        temp += [sum_]
        ans_wer=max(temp)
    for vari_ in aDict:
        if ans_wer==len(aDict[vari_]):
            temp1 = temp1 + [vari_]
    return temp1
def main():
    '''
    params@ input a dictionary
    returns the higesth length key
    '''
    n=input()
    aDict={}
    for i in range(int(n)):
        s=input()
        l=s.split()
        if l[0][0] not in aDict:
            aDict[l[0][0]]=[l[1]]
        else:
            aDict[l[0][0]].append(l[1])
    print(biggest(aDict))
if __name__== "__main__":
    main()