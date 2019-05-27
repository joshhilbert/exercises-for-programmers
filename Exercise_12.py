
# Exercise 12: Computing Simple Interest
# 2019-05-24
# Notes: Get principle, interest rate and terms

user_principal = int(input("Enter the principal: "))
user_interest = float(input("Enter the rate of interest: "))
user_years = int(input("Enter the number of years: "))

# Intermediate calculations
interest_rate = user_interest / 100

# Calculate return
investment_return = round(user_principal * (1 + interest_rate * user_years), 2)

message_output = f'After {user_years} years at {user_interest}%, the investment will be worth ${investment_return}.'

print(message_output)
