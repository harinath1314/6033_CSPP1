'''
problem deals with Paying Debt off in a Year

'''

def paying_debtoffinayear(start_balance, annual_interestrate):
    '''
    # In this problem, we will not be dealing with a minimum monthly payment rate.
    '''
    min_monthlypayment = 10
    temp = start_balance
    ha_ri = 1
    month_count = 0
    monthly_interest_rate = (annual_interestrate / 12.0)
    if start_balance < 0:
        ha_ri = 0
        min_monthlypayment = 0
    while ha_ri:
        month_count += 1
        monthly_unpaid_balance = (start_balance) - (min_monthlypayment)
        start_balance = (monthly_unpaid_balance) + (monthly_interest_rate*monthly_unpaid_balance)
        if start_balance <0:
            ha_ri = 0
        if month_count == 12 and ha_ri != 0:
            min_monthlypayment += 10
            month_count = 0
            start_balance = temp
    return min_monthlypayment
def main():
    '''
    this is final program to show the min_monthlypayment
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: ", (paying_debtoffinayear(data[0], data[1])))
    
if __name__ == "__main__":
    main()
