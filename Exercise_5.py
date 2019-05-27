
# Exercise 5: Simple Math
# 2019-05-24
# 2019-05-25: Convert to main and functions
# Notes: Get two numbers, perform basic math functions, return work on new lines

# Declare variables and constants
user_first = int(input("What is the first number? "))
user_second = int(input("What is the second number? "))

# Calculate values
v_add = user_first + user_second
v_sub = user_first - user_second
v_mul = user_first * user_second
v_div = user_first // user_second # // is used for integer division

# Construct string for each function
output_add = f'{user_first} + {user_second} = {v_add}'
output_sub = f'{user_first} - {user_second} = {v_sub}'
output_mul = f'{user_first} * {user_second} = {v_mul}'
output_div = f'{user_first} / {user_second} = {v_div}'

# Concatenate strings onto new lines
output_message = output_add + '\n' + output_sub + '\n' + output_mul + '\n' + output_div

print(output_message)
