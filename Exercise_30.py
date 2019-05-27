
# Exercise 30: Multiplication Table
# 2019-05-25
# Notes: Create a program that generates multiplication tables for 0 to 12


def calculation(x, y):
    value = x * y
    return value


def main():
    for x in range(0, 13):
        for y in range(0, 13):
            z = calculation(x, y)
            print(f'{x} x {y} = {z}')


# Call main
main()
