''' this program is
to find how many values are assosiated with dictionary
'''



def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    values_ofdic = aDict.values()
    sum = 0 
    for x in values_ofdic:
        lenof_x = len(x)
        sum = sum + lenof_x
    return sum

    

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
    


if __name__ == "__main__":
    main()