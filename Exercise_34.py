
# Exercise 34: Employee List Removal
# 2019-05-26
# Notes: Locate and remove entry


def employee_roster(employee):
    i = 0
    count = len(employee)
    print(f'There are {count} employees:')

    while i < count:
        print(employee[i])
        i += 1


def fire_employee(employee):
    u_emp = input("\nEnter an employee name to remove: ")

    if u_emp in employee:
        employee.remove(u_emp)
        employee_roster(employee)
    else:
        print("Employee does not exist!")


def main():
    employee = ["John Smith", "Jackie Jackson", "Chris Jones", "Amanda Cullen", "Jeremy Goodwin"]

    employee_roster(employee)

    fire_employee(employee)


# Call main
main()
