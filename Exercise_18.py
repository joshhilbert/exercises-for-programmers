
# Exercise 18: Temperature Converter
# 2019-05-24
# Notes: C to F and F to C and allow for upper and lower

import sys

# Declare and assign variables and constants
# user_temp = 0
# user_scale = ""
# user_system = ""


# Get temp system
print("Press C to convert from Fahrenheit to Celsius. \nPress F to convert from Celsius to Fahrenheit.")
user_scale = str(input("Your choice: "))

# Get degrees to convert
if user_scale.upper() == "C":
    user_system_from = "Celsius"
    user_system_to = "Fahrenheit"
    user_temp = int(input(f'Please enter the temperature in {user_system_from}: '))
    temp_output = (user_temp * (9/5)) + 32
    message_output = f'The temperature in {user_system_to} is {temp_output}.'
elif user_scale.upper() == "F":
    user_system_from = "Fahrenheit"
    user_system_to = "Celsius"
    user_temp = int(input(f'Please enter the temperature in {user_system_from}: '))
    temp_output = round((user_temp - 32) * (5/9), 2)
    message_output = f'The temperature in {user_system_to} is {temp_output}.'
else:
    print("Invalid temperature system! Please try again.")
    sys.exit()

print(message_output)
