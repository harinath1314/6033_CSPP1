'''
this is a program that gives the balance amount of credit card bill repayment at the end of year 
'''

def paying_debtoffinayear(balance_h, annual_interestrate, monthly_paymentrate):
	'''
	this is a function to find the balnce amount
	'''

	month_i = 0
	while month_i < 12:
		balance_h=balance_h-(monthly_paymentrate * balance_h)
		balance_h =balance_h + (annual_interestrate / 12.0 * balance_h)
		month_i = month_i + 1
	return round(balance_h, 2)
		
	

def main():
	'''
	this is a program that gives the solution to problem
	'''
	data = input()
	data = data.split(' ')
	data = list(map(float, data))
	print(paying_debtoffinayear(data[0],data[1],data[2]))

if __name__ == "__main__":
	main()

