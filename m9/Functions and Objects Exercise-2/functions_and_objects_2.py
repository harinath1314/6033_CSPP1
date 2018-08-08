'''Function and Objects Exercise-2
this is a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]
'''
def inc(x):
	'''
	this is function to increase number by 1
	'''
	x=x+1
	return x
def apply_to_each(L, f):
	'''
	optimising solution
	'''
	for i in range (len(L)):
	    L[i] = f(L[i])
	return L

def main():
	'''
	this is the main program
	for given problem
	on functions and objects2
	'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, inc))

if __name__ == "__main__":
    main()
