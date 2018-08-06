"""Functions - Assignment-3 - Using Bisection Search to Make the Program Faster."""
def paying_debt(previous_balance, annual_interest_rate):
    """ Calculating the interest"""
    monthly_interest_rate = (annual_interest_rate) / 12.0
    monthly_payment_lower_value = previous_balance / 12.0
    monthly_payment_upper_value = (previous_balance * (1 + monthly_interest_rate)**12) / 12.0
    updated_balance = previous_balance
    epsilon_input = 0.0001
    guess_input = (monthly_payment_lower_value + monthly_payment_upper_value)/2.0
    while True:
        month = 1
        while month <= 12:
            updated_balance = updated_balance - guess_input
            updated_balance = updated_balance + (monthly_interest_rate * updated_balance)
            month += 1
        if updated_balance > 0 and updated_balance > epsilon_input:
            monthly_payment_lower_value = guess_input
            updated_balance = previous_balance
        elif updated_balance < 0 and updated_balance < -epsilon_input:
            monthly_payment_upper_value = guess_input
            updated_balance = previous_balance
        else:
            return round(guess_input, 2)
        guess_input = (monthly_payment_lower_value + monthly_payment_upper_value)/2
def main():
    """Writing inside this function"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:", paying_debt(data[0], data[1]))
if __name__ == "__main__":
    main()
