
# Exercise 20: Multi-state Sales Tax Calculator
# 2019-05-24
# Notes: Add tax for specific counties within a state

# Declare and assign variables and constants
tax_rate_WI = .055
tax_rate_Il = .08
tax_rate_WI_Eau_Claire = 0.005
tax_rate_WI_Dunn = 0.004
user_county = ""
tax_rate = 0.0

# Get input
user_order = float(input("What is the order amount? "))
user_state = str(input("What is the state? "))

# Set tax rate
if user_state == 'Wisconsin':
    user_county = str(input("What is your county? "))
    if user_county == "Eau Claire":
        tax_rate = tax_rate_WI + tax_rate_WI_Eau_Claire
    elif user_county == "Dunn":
        tax_rate = tax_rate_WI + tax_rate_WI_Dunn
    else:
        tax_rate = tax_rate_WI
elif user_state == "Illinois":
    tax_rate = tax_rate_Il

# Calculate tax rate
order_tax = round(user_order * tax_rate, 2)

order_total = user_order + order_tax

message_output = f'The tax is ${order_tax}. \nThe total is ${order_total}.'

print(message_output)
