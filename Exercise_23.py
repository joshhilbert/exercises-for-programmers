
# Exercise 23: Troubleshooting Car Issues
# 2019-05-24
# Notes: Create expert system diagnostic tool

import sys

# Define variables and constraints

question_one = input("Is the car silent when you turn the key? ")

if question_one.upper() == "Y":
    question_two_a = input("Are the battery terminals corroded? ")
    if question_two_a.upper() == "Y":
        print("Clean the terminals and try starting again.")
    elif question_two_a.upper() == "N":
        print("Replace cables and try again.")
    else:
        print(f'Error!')
        sys.exit()
elif question_one.upper() == "N":
    question_two_b = input("Does the car make a clicking noise? ")
    if question_two_b.upper() == "Y":
        print("Replace the battery.")
    elif question_two_b.upper() == "N":
        question_three = input("Does the car crank up but fail to start? ")
        if question_three.upper() == "Y":
            print("Check spark plug connections.")
        elif question_three.upper() == "N":
            question_four = input("Does the engine start and then die? ")
            if question_four.upper() == "Y":
                question_five = input("Does your car have fuel injection? ")
                if question_five.upper() == "Y":
                    print("Get it in for service.")
                elif question_five.upper() == "N":
                    print("Check to ensure the choke is opening and closing.")
                else:
                    print(f'Error!')
                    sys.exit()
            else:
                print(f'Error!.')
                sys.exit()
        else:
            print(f'Error!')
            sys.exit()
    else:
        print(f'Error!')
        sys.exit()
else:
    print(f'Error!')
    sys.exit()
