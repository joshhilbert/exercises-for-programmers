
# Exercise 1: Saying Hello
# 2019-05-24: First build
# 2019-05-25: Convert to main and functions
# Notes: Ask user for name, concatenate string, msg output

# user_name = input("What is your name? ")
# output_message = "Hello, " + user_name + ", nice to meet you!"
#
# print(output_message)


def response(name):
    value = f'"Hello, {name}, nice to meet you!'

    return value


def main():
    user_name = input("What is your name? ")

    message_output = response(user_name)

    print(message_output)


# Call main
main()
