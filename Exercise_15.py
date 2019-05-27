
# Exercise 15: Password Validation
# 2019-05-24
# Notes: Validate a password

# Declare and assign variables and constants
stored_password = 'abc'
user_password = str(input("What is the password? "))

if user_password == stored_password:
    message_output = 'Welcome!'
else:
    message_output = 'I don\'t know you.'

print(message_output)
