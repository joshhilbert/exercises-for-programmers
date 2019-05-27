
# Exercise 31: Karvonen Heart Rate
# 2019-05-25
# Notes: Create a program for optimal heart rate


# Validate age and resting pulse are integers
def validate_int(test_value):
    if str.isnumeric(test_value):
        value = int(test_value)
    else:
        print(f'{test_value} is not a number!')
        value = 0
        main()

    return value


# Ask for pulse
def user_pulse():
    u_resting_pulse = input("Enter resting pulse: ")

    value = validate_int(u_resting_pulse)

    return value


# Ask for age
def user_age():
    u_age = input("Enter age: ")

    value = validate_int(u_age)

    return value


# Calculate rate at an intensity
def calculate_rate(a, hr, intensity):
    i = intensity / 100
    value = int((((220 - a) - hr) * i) + hr)
    return value


def header_row():
    print("Intensity | Rate")
    print("----------|----------")


def main():
    resting_pulse = user_pulse()
    age = user_age()

    intensity = 55

    header_row()

    while intensity <= 95:
        bpm = calculate_rate(age, resting_pulse, intensity)
        message_output = f'{intensity}%       | {bpm} bpm'
        print(message_output)
        intensity += 5

    exit()


# Call main
main()
