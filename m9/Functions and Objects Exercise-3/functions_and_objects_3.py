'''
this will be the solution to find the squares of the
elements in the given testlist
for example: testlsit=[1, 2, 3, 4]
then output is [1, 4, 9, 16]
'''
def square(num_):
    '''
    #this gives square of number
    '''
    num_=num_*num_
    return num_

def apply_to_each(L, suare):
    '''
    optimisation technique
    '''
    for i in range (len(L)):
        L[i]=square(L[i])
    return L
    
def main():
    '''
    main program
    input=[1, 4, -9, 0]
    output=[1, 16, 81, 0]
    '''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, square))

if __name__ == "__main__":
    main()