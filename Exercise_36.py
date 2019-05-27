
# Exercise 36: Computing Statistics
# 2019-05-26
# Notes: Allow user to enter numbers then perform aggregates


def validate_integer(test_value):
    if str.isnumeric(test_value):
        value = str.isnumeric(test_value)
    else:
        value = str.isnumeric(test_value)
    return value


# If not an integer, treat as done
def get_number():
    u_number = input("Enter a number: ")

    test_int = validate_integer(u_number)

    if test_int:
        value = int(u_number)
    else:
        value = "done"

    return value


def calc_average(numbers):
    a = sum(numbers)
    b = len(numbers)
    value = a / b
    return value


def calc_standard_deviation(numbers):
    squared = []

    # Calculate mean
    m = sum(numbers) / len(numbers)

    # Difference from mean into new list
    for x in numbers:
        y = (x - m)**2
        squared.append(y)

    a = sum(squared)
    b = len(squared)

    # Square root of new mean
    value = round((a / b)**0.5, 2)

    return value


def main():
    aggregate = []

    while True:
        number = get_number()
        if number == "done":
            break
        aggregate.append(number)

    print("Numbers: ")
    print(*aggregate, sep=', ')
    calc_avg = calc_average(aggregate)
    calc_minimum = min(aggregate)
    calc_maximum = max(aggregate)
    calc_std_dev = calc_standard_deviation(aggregate)

    # Construct output
    message_output = f'The average is {calc_avg}.'
    message_output = f'{message_output}\nThe minimum is {calc_minimum}.'
    message_output = f'{message_output}\nThe maximum is {calc_maximum}.'
    message_output = f'{message_output}\nThe standard deviation is {calc_std_dev}.'

    print(message_output)


# Call main
main()
