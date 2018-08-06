'''credit card company each month.'''
def paying_debtoff(previous_balance, annual_interest, monthly_payment_rate):
    '''updated_balance'''
    monthly_interest = (annual_interest) / 12.0
    updated_balance = previous_balance
    i_temp = 1
    while  i_temp <= 12:
        monthly_payment = monthly_payment_rate * updated_balance
        monthly_unpaid_balance = updated_balance - monthly_payment
        updated_balance = monthly_unpaid_balance + (monthly_interest * monthly_unpaid_balance)
        x_out = round(updated_balance, 2)
        i_temp += 1
    return x_out
def main():
    '''enter previous_balance, annual_interest, monthly_payment_rate'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("remaining balance:" + str(paying_debtoff(data[0], data[1], data[2])))

if __name__ == "__main__":
    main()
