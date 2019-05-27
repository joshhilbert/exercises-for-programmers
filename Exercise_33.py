
# Exercise 33: Magic 8 Ball
# 2019-05-26
# Notes: Give a random response to a user input

import random


def get_question():
    value = input("What's your question? ")
    return value


def shake():
    response = ["Yes.", "No.", "Maybe.", "Ask again later."]

    hmm = random.randint(0, 3)
    value = response[hmm]

    print(value)


def main():

    get_question()
    shake()


# Call main
main()
