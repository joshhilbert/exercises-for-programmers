
# Exercise 19: BMI Calculator
# 2019-05-24
# Notes: BMI within ranges

# Declare and define variables
user_weight = int(input("Please enter weight (pounds): "))
user_height = int(input("Please enter height (inches): "))

# Calculation
bmi_calc = round((user_weight / (user_height ** 2)) * 703, 1)

# Determine bucket
if bmi_calc < 18.5:
    message_results = "You are underweight, please see doctor."
elif bmi_calc > 25:
    message_results = "You are overweight, please see a doctor."
else:
    message_results = "You are within the ideal weight range."

# Construct output
message_output = f'Your BMI is {bmi_calc}. \n{message_results}'

print(message_output)
