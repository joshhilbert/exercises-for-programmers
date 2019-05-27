
# Exercise 11: Currency Conversion
# 2019-05-24
# Notes: Convert currency to another currency
# Unable to solve due to exchange rate conversion issues

# Define variables
user_euro = int(input("How many euros are you exchanging? "))
user_exchange_rate = float(input("What is the exchange rate? "))

# Unsure how to calculate exchange rates
us_dollar = round(user_euro * user_exchange_rate, 2)

# Construct output
message_output = f'{user_euro} euros at an exchange rate of {user_exchange_rate} is \n{us_dollar} U.S. dollars.'

print(message_output)  # WRONG
