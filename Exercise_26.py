
# Exercise 26: Months to Pay Off a Credit Card
# 2019-05-25
# Notes: Use function to calculate months to pay off a credit card

import math


# Define main function
def main():
    u_balance = int(input("What is your balance? "))
    u_interest_rate = int(input("What is the APR on the card (as a percent)? "))
    u_payment = int(input("What is the monthly payment you can make? "))

    number_of_months = calculate_months_until_paid_off(u_balance, u_interest_rate, u_payment)

    message_output = f'It will take you {number_of_months} months to pay off this card.'

    print(message_output)


# Define function
def calculate_months_until_paid_off(b, apr, p):
    # Calculate daily interest rate
    i = apr / 365 / 100

    # steps of formula
    step_one = (1 + i)**30
    step_two = 1 - step_one
    step_three = (b / p) * step_two
    step_four = 1 + step_three
    step_five = math.log(step_four) / math.log(1 + i)
    value = math.ceil((-1/30) * step_five)

    return value


# Call main
main()
