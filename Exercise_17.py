
# Exercise 17: Blood Alcohol Calculator
# 2019-05-24
# Notes: create BAC calculator
# Errors in BAC formula... not validating

import sys

# Declare and define variables and constraints
alcohol_dist: 0.0
alcohol_dist_male = 0.73
alcohol_dist_female = 0.66
user_weight = int(input("What is your weight? "))
user_gender = str(input("What is your gender (M/F)? "))
user_drink_count = int(input("How many drinks have you had (ounces)? "))
user_drink_alcohol_content = float(input("Alcohol by volume of drinks? "))
user_time_last_drink = int(input("How many hours since last drink? "))

# Validate gender and assign alcohol distribution ratio
# in later programs run this immediately after input
if user_gender == 'M':
    alcohol_dist = alcohol_dist_male
elif user_gender == 'F':
    alcohol_dist = alcohol_dist_female
else:
    print("Invalid gender entry! Please try again")
    sys.exit()

bac_calc_consumed = user_drink_count * (user_drink_alcohol_content / 100)

b_a_c = round((bac_calc_consumed * 5.14 / user_weight * alcohol_dist) - 0.015 * user_time_last_drink, 4)

message_bac = f'Your BAC is {b_a_c}.'

if b_a_c <= 0.08:
    message_return = 'It is legal for you to drive.'
else:
    message_return = 'It is not legal for you to drive.'

message_output = f'{message_bac} \n{message_return}'

print(message_output)