

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    atup_ans=()

    for i in range(len(aTup)):
        if i%2==0:

            atup_ans+=(aTup[i],)
    return atup_ans

    

def main():
    data = input()
    data = data.split( )
    aTup=()
    for j in range(len(data)):
        aTup += (data[j],)
    print(oddTuples(aTup))
if __name__ == "__main__":
    main()