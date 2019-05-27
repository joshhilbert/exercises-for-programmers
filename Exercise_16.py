
# Exercise 16: Legal Driving Age
# 2019-05-24
# Notes: Validate driving age

# Declare and define variables and constraints
user_age = int(input("What is your age? "))

message_output = 'You are not old enough to legally drive.' if user_age < 16 \
    else 'You are old enough to legally drive.'

print(message_output)
