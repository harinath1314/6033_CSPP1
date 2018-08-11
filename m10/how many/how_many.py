''' this program is
to find how many values are assosiated with dictionary
'''



def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    values_ofdic = aDict.values()
    sum_ = 0 
    for x in values_ofdic:
        lenof_x = len(x)
        sum_ = sum_ + lenof_x

    return sum_,values_ofdic

    

def main():
    '''
    this exuecutes the main solution
    to find number of values
    assosiated in the dictionary
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
    print(how_many(aDict))
    print(how_many(aDict)[1])




if __name__ == "__main__":
    main()