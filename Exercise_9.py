
# Exercise 9: Paint Calculator
# 2019-05-24
# Notes: Calculate gallons of paint necessary to paint ceiling

import math

# Declare variables and constants
gallon_coverage = 350  # in sqft
user_room_length = int(input("What is the length of the ceiling in feet? "))
user_room_width = int(input("What is the width of the ceiling in feet? "))

# Calculations
square_feet = user_room_length * user_room_width
gallon_required = math.ceil(square_feet / gallon_coverage)  # round up to next full gallon

message_output = f'You will need to purchase {gallon_required} gallons of \npaint to cover {square_feet} square feet.'

print(message_output)
