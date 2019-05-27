
# Exercise 14: Tax Calculator
# 2019-05-24
# Notes: If user is in Wisconsin charge tax, else no tax

# Declare and assign variables and constants
tax_rate = .055
user_order = float(input("What is the order amount? "))
user_state = str(input("What is the state? "))

# Charge tax if Wisconsin
if user_state == 'WI':
    tax_amount = round(user_order * tax_rate, 2)
    total_amount = user_order + tax_amount
    message_WI = f'The subtotal is ${round(user_order, 2)}. \nThe tax is ${tax_amount}. \nThe total is ${total_amount}.'
    print(message_WI)

message_output = f'The total is ${round(user_order, 2)}.'

print(message_output)
