
# Exercise 29: Handling Bad Input
# 2019-05-25
# Notes: Keep requesting for valid input


def question():
    value = input("What is the rate of return? ")

    return value


def validate_int(rate):
    if str.isnumeric(rate):
        if rate == "0": # CHALLENGE ACCEPTED
            print("Enter a non-zero rate of return.")
            value = 0
        else:
            value = int(rate)
    else:
        print("Sorry. That\'s not a valid input.")
        value = 0

    return value


def main():
    r = 0

    while r <= 0:
        rate = question()
        r = validate_int(rate)

    message_value = round(72 / r, 1)

    message_output = f'It will take {message_value} years to double your initial investment.'

    print(message_output)


# Call main
main()
