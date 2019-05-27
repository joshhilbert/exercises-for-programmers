
# Exercise 28: Adding numbers
# 2019-05-25
# Notes: Add five numbers together with a loop to get numbers


def number():
    value = int(input("Enter a number: "))

    return value


def main():
    x = int(input("How many numbers would you like to add? "))
    j = 0
    counter = 1

    while counter <= x:
        i = number()
        j = j + i
        counter += 1

    message_output = f'The total is {j}.'

    print(message_output)


# Call main
main()
