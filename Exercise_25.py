
# Exercise 25: Password Strength Indicator
# 2019-05-24
# Notes: pass password through a function to determine strength of password

import sys


# Define main function
def main():
    u_pass = str(input("Please enter password: "))

    value = password_strength(u_pass)

    if value == 1:
        output_value = "very weak"
    elif value == 2:
        output_value = "weak"
    elif value == 3:
        output_value = "strong"
    elif value == 4:
        output_value = "very strong"
    else:
        print("Error!")
        sys.exit()

    output_message = f'THe password \'{u_pass}\' is a {output_value} password.'

    print(output_message)


# Function to count numbers and letters
def password_strength(password):

    number = sum(c.isdigit() for c in password)
    letter = sum(c.isalpha() for c in password)
    spaces = sum(c.isspace() for c in password)
    special = len(password) - number - letter - spaces

    if letter == 0 and len(password) < 8:
        value = 1
    elif number == 0 and len(password) < 8:
        value = 2
    elif number > 1 and letter >= 1 and len(password) >= 8:
        value = 3
    elif number > 1 and letter > 1 and special > 1 and len(password) >= 8:
        value = 4
    else:
        value = 0
    return value


# Call main function
main()
