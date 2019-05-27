
# Exercise 4: Mad Lib
# 2019-05-24: first build
# 2019-05-25: Convert to main and functions
# Notes: Ask for language parts and then use string interpolation for output

# # Declare variables and constants
# user_noun = input("Enter a noun: ")
# user_verb = input("Enter a verb: ")
# user_adjective =  input("Enter an adjective: ")
# user_adverb =  input("Enter an adverb: ")
#
# output_message = f'Do you {user_verb} your {user_adjective} {user_noun} {user_adverb}? That\'s hilarious!'
#
# print(output_message)


def mad_lib(noun, verb, adjective, adverb):

    value = f'Do you {verb} your {adjective} {noun} {adverb}? That\'s hilarious!'

    return value


def main():
    u_noun = input("Enter a noun: ")
    u_verb = input("Enter a verb: ")
    u_adjective = input("Enter an adjective: ")
    u_adverb = input("Enter an adverb: ")

    message_output = mad_lib(u_noun, u_verb, u_adjective, u_adverb)

    print(message_output)


# Call main
main()
