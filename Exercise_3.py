
# Exercise 3: Printing Quotes
# 2019-05-24: First build
# 2019-05-25: Convert to main and functions
# Notes: Ask for a quote (add " " to variable) and speaker, then return

# user_quote = "\"""" + input("What is the quote? ") + "\""""
# user_speaker = input("Who said it? ")
#
# output_message = user_speaker + " says, " + user_quote
#
# print(output_message)


def quote_builder(quote, speaker):

    value = f'{speaker} says, "{quote}".'

    return value


def main():
    u_quote = input("What is the quote? ")
    u_speaker = input("Who said it? ")

    message_output = quote_builder(u_quote, u_speaker)

    print(message_output)


# Call main
main()