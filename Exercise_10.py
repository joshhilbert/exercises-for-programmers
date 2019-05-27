
# Exercise 10: Self-Checkout
# 2019-05-24
# Notes: Create self checkout system and calculate subtotal, tax, total
# Current build only allows for integer inputs

# Define variables
tax_rate = 0.055
user_item_one_price = float(input("Enter the price of item 1: "))
user_item_one_qty = int(input("Enter the quantity of item 1: "))
user_item_two_price = float(input("Enter the price of item 2: "))
user_item_two_qty = int(input("Enter the quantity of item 2: "))
user_item_three_price = float(input("Enter the price of item 3: "))
user_item_three_qty = int(input("Enter the quantity of item 3: "))

sum_item_one = user_item_one_price * user_item_one_qty
sum_item_two = user_item_two_price * user_item_two_qty
sum_item_three = user_item_three_price * user_item_three_qty

sum_subtotal = sum_item_one + sum_item_two + sum_item_three * 1.0

sum_tax = sum_subtotal * tax_rate

sum_total = sum_subtotal + sum_tax

message_output = f'Subtotal: ${sum_subtotal} \nTax: ${sum_tax} \nTotal: ${sum_total}'

print(message_output)

