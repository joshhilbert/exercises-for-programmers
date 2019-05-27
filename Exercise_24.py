
# Exercise 24: Anagram Checker
# 2019-05-24
# Notes: BMI within ranges


# Define main
def main():
    message_output = ""
    print("Enter two strings and I'll tell you if they \nare anagrams:")

    u_word_one = str(input("Enter the first word: "))
    u_word_two = str(input("Enter the second word: "))

    anagram_check = is_anagram(u_word_one, u_word_two)

    if anagram_check is True:
        message_output = f'\"{u_word_one}\" and \"{u_word_two}\" are anagrams.'
    elif anagram_check is False:
        message_output = f'\"{u_word_one}\" and \"{u_word_two}\" are not anagrams.'

    print(message_output)


# Define function to see if two words match
def is_anagram(word_one, word_two):
    one_sort = sorted(word_one)
    two_sort = sorted(word_two)

    if one_sort == two_sort:
        result = True
    else:
        result = False

    return result


main()
