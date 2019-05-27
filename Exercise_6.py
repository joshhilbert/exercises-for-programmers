
# Exercise 6: Retirement Calculator
# 2019-05-24
# Notes: Get current age and retirement age, then calcuate years left to retirement and the year

import datetime
import sys

# Declare variables
now = datetime.datetime.now()
user_age = int(input("What is your current age? "))
user_age_retire = int(input("At what age would you like to retire? "))

# Calculate years until retirement
years_to_retirement = user_age_retire - user_age

# Notify user they can already retire if negative number
if years_to_retirement <= 0:
    print("You can retire now!")
    sys.exit()

# Calculate year of retirement
year_of_retirement = years_to_retirement + int(now.year)

# Construct message_output
message_work_years = f'You have {years_to_retirement} years left until you can retire.'
message_retirement_year = f'It\'s {now.year}, so you can retire in {year_of_retirement}.'

message_output = f'{message_work_years}\n{message_retirement_year}'

print(message_output)
