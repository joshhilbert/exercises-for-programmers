
# Exercise 35: Picking a Winner
# 2019-05-26
# Notes: Populate an array then pick a random winner

import random


# Get names for array
def get_entrant():
    value = input("Enter a name: ")
    return value


# Pick winner after all names entered
def pick_winner(n):
    value = random.randint(0, n)
    return value


def main():
    contestant = []
    entrant = " "

    # Get names for array
    while len(entrant) > 0:
        entrant = get_entrant()
        if len(entrant) > 0:
            contestant.append(entrant)

    # Pick winner after all names entered
    max_number = len(entrant)
    ticket = pick_winner(max_number)

    # Get name from array at index
    winner = contestant[ticket]

    message_output = f'The winner is.... {winner}.'
    print(message_output)


# Call main
main()
