
# Exercise 32: Guess the Number game
# 2019-05-25
# Notes: Let a user select difficulty then guess a number
# Note: Unable to solve

import random


def validate_integer(test_value):
    if str.isnumeric(test_value):
        value = int(test_value)
    else:
        value = False
    print(value)
    return value


def get_difficulty():
    u_difficulty = input("Pick a difficulty level (1, 2, 3): ")

    diff = validate_integer(u_difficulty)

    if diff:
        if diff == 1:
            value = 10
        elif diff == 2:
            value = 100
        elif diff == 3:
            value = 1000
        else:
            print(f'{u_difficulty} is not a valid difficulty level.')
            value = False
    else:
        print(f'{u_difficulty} is not a valid difficulty level.')
        value = False

    return value


def get_target(max_number):
    value = random.randint(1, max_number)
    print(value)
    return value


def get_guess(target):
    u_guess = input("I have my number. What's your guess? ")
    guess = validate_integer(u_guess)

    if guess == target:
        value = 'fuck'
    elif guess < target:
        value = "Too low!"
    elif guess > target:
        value = "Too high!"
    else:
        value = False

    return value


def extra_guess(wrong_guess, target):
    u_new_guess = input(f'{wrong_guess}. Guess again: ')

    new_guess= validate_integer(u_new_guess)

    if new_guess == target:
        value = True
    elif new_guess < target:
        value = "Too low!"
    elif new_guess > target:
        value = "Too high!"
    else:
        value = False

    return value


def main():
    level = False
    counter = 1
    print("Let\'s play Guess the Number.")

    # Force a valid difficulty selection
    while not level:
        level = get_difficulty()

    # Get target number
    target = get_target(level)

    winner = get_guess(target)

    # Ask for guesses until correct
    while not winner:
        counter += 1
        extra_guess(winner, target)

    message_outcome = f'You got it in {counter} guesses!'

    print(message_outcome)


# Call main
main()
