
# Exercise 22: Comparing Numbers
# 2019-05-24
# Notes: Compare three numbers

import sys

# Declare and assign variables and constants
u_one = int(input("Enter the first number: "))
u_two = int(input("Enter the second number: "))
u_three = int(input("Enter the third number: "))
largest_number = 0

if u_one == u_two or u_one == u_three or u_two == u_three:
    print("Numbers are not unique.")
    sys.exit()

largest_number = u_two if u_one > u_two else u_two

largest_number = largest_number if largest_number > u_three else u_three

message_output = f'The largest number is {largest_number}.'

print(message_output)
