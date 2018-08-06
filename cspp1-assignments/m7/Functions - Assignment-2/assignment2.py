'''Assignment-2 - Paying Debt off in a Year'''
def paying_debt(input_balance, annual_interest_rate):
    '''updated balance'''
    monthly_payment = 0
    updated_balance = input_balance
    while updated_balance > 0:
        monthly_interest_rate = annual_interest_rate / 12.0
        updated_balance = input_balance
        monthly_payment = monthly_payment + 10
        month_count = 1
        while month_count <= 12:
            monthly_unpaid_balance = updated_balance - monthly_payment
            temp_x = monthly_interest_rate * monthly_unpaid_balance
            updated_balance_each_month = monthly_unpaid_balance + temp_x
            updated_balance = updated_balance_each_month
            month_count += 1
    return monthly_payment
def main():
    ''' enter input balance '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest payment: "+str(paying_debt(data[0], data[1])))
if __name__ == "__main__":
    main()
