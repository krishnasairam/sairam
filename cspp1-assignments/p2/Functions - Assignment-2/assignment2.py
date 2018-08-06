'''In this problem, we will not be dealing with a minimum monthly payment rate.
The following variables contain values as described below:
balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal'''
def payingDebtOffInAYear(inp_balance, annual_interest):
    '''updated_balance'''
    monthly_payment = 0
    balance = inp_balance
    while balance > 0:
        balance = inp_balance
        monthly_payment = monthly_payment + 10
        month = 1
        while month <= 12:
            monthly_interest_rate = (annual_interest_rate) / 12.0
            monthly_unpaid_balance = (balance) - (monthly_payment)
            updated_balance_each_month = (monthly_unpaid_balance) + \
            (monthly_interest_rate * monthly_unpaid_balance)
            balance = updated_balance_each_month
            month += 1
    return monthly_payment
    return round(balance, 2)
def main():
    '''enter balance, annual_interest'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(payingDebtOffInAYear(data[0],data[1]))
    
if __name__== "__main__":
    main()