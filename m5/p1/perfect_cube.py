''''
we are writing a program to find if the given number
is a perfect cube or not
using guess and check alogorithm method
for example if we give input as 136 
output must be: 136 is a perfect 
'''

def main():
	'''
	input a number 
	show output whether the input is a perfect cube or not
	'''
	s = int(input("cube = "))
	epsilon = 0.01
	guess = 0.0
	num_guesses = 1
	increment = 0.001
	while abs(guess**3-s) >= epsilon:
		  guess += increment
		  num_guesses += 1
	print('num_guesses =', num_guesses)

	if abs(guess**3-s) >= epsilon:
		print("cube root does not exist for ", s)
	else:
		print(guess, "is the perfect cube")

if __name__ == "__main__":
	main()
