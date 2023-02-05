# condition correct - True (1)
# condition incorrect - False (0)
calculation_to_hours = 24
name_of_unit = "hour"


def days_to_units(number_of_days):
    if number_of_days > 0:
        return f"{number_of_days} days are {number_of_days * calculation_to_hours} {name_of_unit}"
    elif number_of_days == 0:
        return "You entered 0, please enter positive number"


def validate_and_execute():
    if user_input.isdigit():
        calculated_value = days_to_units(int(user_input))
        print(calculated_value)
    else:
        print("Invalid Number")


user_input = input("Enter number of days and i will convert it to hours!\n")
validate_and_execute()
