
# Exercise 8: Pizza Party
# 2019-05-24
# Notes: Evenly divide number of pizza slices

# Declare variables
user_people = int(input("How many people? "))
user_pizza = int(input("How many pizzas do you have? "))
user_slice = int(input("How many slices per pizza? "))

# Calculations
slice_count = user_pizza * user_slice

slice_per_person = int(slice_count / user_people)

leftover_slice = slice_count - (slice_per_person * user_people)

# Construct output
message_return = f'{user_people} people with {user_pizza} pizzas and {user_slice} slices per pizza'
message_slice = f'Each person gets {slice_per_person} pieces of pizza.'
message_leftover = f'There are {leftover_slice} leftover pieces.'

message_output = f'{message_return} \n{message_slice} \n{message_leftover}'

print(message_output)
