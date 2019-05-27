
# Exercise 27: Validating Inputs
# 2019-05-25
# Notes: Use function to calculate months to pay off a credit card

u_first_name = str(input("Enter first name: "))
u_last_name = str(input("Enter last name: "))
u_zip_code = str(input("Enter Zip code: "))
u_emp_id = str(input("Enter EmployeeID: "))


# Validate first name 2 or more characters
def validation_first_name(f_name):
    if len(f_name) == 0:
        value = "The first name must be filled in."
    elif len(f_name) < 2:
        value = f'"{f_name}" is not a valid first name. It is too short'
    else:
        value = True

    return value


# Validate last name 2 or more characters
def validation_last_name(l_name):
    if len(l_name) == 0:
        value = "The last name must be filled in."
    elif len(l_name) < 2:
        value = f'"{l_name}" is not a valid last name. It is too short'
    else:
        value = True

    return value


# Validate ZIP code is a number
def validation_zip_code(zip_code):
    value = True if str.isdigit(zip_code) else 'The zip code must be numeric.'

    return value


# Validate EmpID, 2 letter, hyphen, 4 numbers
def validation_emp_id(emp_id):
    if len(emp_id) < 7:
        value = "Employee ID too short!"

        return value

    i = 0
    letter = emp_id[:2]
    hyphen = emp_id[2]
    number = emp_id[-4:]

    i = i + 1 if str.isalpha(letter) else i
    i = i + 1 if hyphen == '-' else i
    i = i + 1 if str.isnumeric(number) else i

    value = True if i == 3 else f'{emp_id} is not a valid ID.'

    return value


# Take all inputs and return errors, if any
def validate_input(i_first_name, i_last_name, i_zip_code, i_emp_id):
    message = ""
    valid_first = validation_first_name(i_first_name)
    valid_last = validation_last_name(i_last_name)
    valid_zip = validation_zip_code(i_zip_code)
    valid_emp_id = validation_emp_id(i_emp_id)

    if not valid_first == True:
        message = f'{valid_first}'

    if not valid_last == True:
        message = f'{message} \n{valid_last}'

    if not valid_zip == True:
        message = f'{message} \n{valid_zip}'

    if not valid_emp_id == True:
        message = f'{message} \n{valid_emp_id}'

    message = "There were no errors found." if message == "" else message

    return message


def main():
    message_output = validate_input(u_first_name, u_last_name, u_zip_code, u_emp_id)

    print(message_output)


# Call main
main()

