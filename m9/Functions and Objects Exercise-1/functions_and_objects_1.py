'''
this is a program which uses function
as object and provides
the solution
'''

def apply_to_each(L, f):
	'''
	#uses function as a object
	'''
	for i in range (len(L)):
		L[i]=f(L[i])
	return L
def main():
	'''
	the main program uses function
	and in function other function is used as object
	'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, abs))

if __name__ == "__main__":
    main()
