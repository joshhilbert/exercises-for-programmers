
# Exercise 2: Counting the Number of Characters
# 2019-05-24: first build
# 2019-05-25: Convert to main and functions
# Notes: Get string then count length, return string and its length

# import sys
#
# user_string = input("What is the input string? ")
# string_count = len(user_string)
#
# # Challenge: If the user enters nothing, state that the user must enter something into the program.
# if string_count == 0:
#     print("Input required!")
#     sys.exit()
# elif string_count > 0:
#     string_count = str(string_count)
#
# output_message = user_string + " has " + string_count + " characters."
#
# print(output_message)


def string_count(string):
    s_count = len(string)

    if s_count == 0:
        value = "Input required!"
    else:
        value = f'{string} has {s_count} characters.'

    return value


def main():
    u_string = input("What is the input string? ")

    message_output = string_count(u_string)

    print(message_output)


# Call main
main()
