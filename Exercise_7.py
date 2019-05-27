
# Exercise 7: Area of a Rectangular Room
# 2019-05-24
# Notes: Calculate area of a room

# Declare variables and constants
feet_to_meters_factor = 0.09290304
user_room_length = int(input("What is the length of the room in feet? "))
user_room_width = int(input("What is the width of the room in feet? "))


# Calculate ft^2 then m^2 to 3 decimal places
square_feet = user_room_length * user_room_width
square_meters = round(square_feet * feet_to_meters_factor, 3)

message_return = f'You entered dimensions of {user_room_length} feet by {user_room_width} feet. \nThe area is'
message_sqft = f'{square_feet} square feet'
message_sqm = f'{square_meters} square meters'

message_output = f'{message_return} \n{message_sqft} \n{message_sqm}'

print(message_output)
