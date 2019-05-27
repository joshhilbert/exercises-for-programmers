
# Exercise 13: Determining Compound Interest
# 2019-05-24
# Notes: Get principle, compound interest rate and terms

user_principal = int(input("What is the principal amount? "))
user_interest = float(input("What is the rate? "))
user_years = int(input("Wat is the number of years? "))
user_compound = int(input("What is the number of times the interest is compounded each year? "))

# Intermediate calculations
interest_rate = user_interest / 100

# Calculate return
investment_return = round(user_principal * (1 + (interest_rate / user_compound)) ** (user_compound * user_years), 2)

# Construct output
message_return = f'${user_principal} invested at {user_interest}% for {user_years} years'
message_interest = f'compounded {user_compound} times per year is ${investment_return}.'

message_output = f'{message_return} \n {message_interest}'

print(message_output)
