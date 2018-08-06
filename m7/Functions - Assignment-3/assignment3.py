
def payingdebtoffina_year(balance_in, annual_interestrate):
    '''
    this is thu function uses bisection for fast programming
    '''
    initial_balance = balance_in
    monthly_interest_rate = annual_interestrate / 12
    lower_payment = initial_balance / 12
    upper_payment = (initial_balance * (1 + monthly_interest_rate) ** 12) / 12.0
    elipson_x= 0.03
    while abs(balance_in > elipson_x):
        moynthly_payrate = (upper_payment + lower_payment) / 2
        balance_in = initial_balance
        for _ in range(12):
            ans_is = balance_in - moynthly_payrate
            balance_in = ans_is + (ans_is * monthly_interest_rate)
        if balance_in > elipson_x:
            lower_payment = moynthly_payrate
        elif balance_in < -elipson_x:
            upper_payment = moynthly_payrate
        else:
            break
    return str(round(moynthly_payrate, 2))
def main():
    '''
    this is the fast final program
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(payingdebtoffina_year(data[0],data[1]))
    
if __name__ == "__main__":
    main()
