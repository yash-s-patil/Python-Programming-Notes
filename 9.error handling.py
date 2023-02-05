# try block - lets you "test" a block of code for errors
# except block - catches the error and lets you handle it
calculation_to_hours = 24
name_of_unit = "hour"


def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculation_to_hours} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(int(user_input_number))
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0, please enter positive number")
        else:
            print("its a negative number, please enter positive number")
    except ValueError:
        print("Invalid Number")


user_input = input("Enter number of days and i will convert it to hours!\n")
validate_and_execute()
