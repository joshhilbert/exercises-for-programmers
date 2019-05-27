
# Exercise 21: Numbers to Names
# 2019-05-24
# Notes: Use switch to translate number to months // no switch in python

# Declare and assign variables and constants
month_output = ""

month_input = int(input("Please enter the number of the month: "))

if month_input == 1:
    month_output = "January"
elif month_input == 2:
    month_output = "February"
elif month_input == 3:
    month_output = "March"
elif month_input == 4:
    month_output = "April"
elif month_input == 5:
    month_output = "May"
elif month_input == 6:
    month_output = "June"
elif month_input == 7:
    month_output = "July"
elif month_input == 8:
    month_output = "August"
elif month_input == 9:
    month_output = "September"
elif month_input == 10:
    month_output = "October"
elif month_input == 11:
    month_output = "November"
elif month_input == 12:
    month_output = "December"

message_output = f'The name of the month is {month_output}.'

print(message_output)
