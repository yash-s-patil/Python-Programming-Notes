# dictionary - are used to store values in key:value pairs
# is a collection, which does not allow duplicate values


def days_to_units(number_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{number_of_days} days are {number_of_days * 24} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{number_of_days} days are {number_of_days * 24 * 60} {conversion_unit}"
    else:
        return "unsupported unit"


def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0, please enter positive number")
        else:
            print("its a negative number, please enter positive number")
    except ValueError:
        print("Invalid Number")


user_input = ""
while user_input != "exit":
    try:
        user_input = input("Enter number of days and conversion unit\n")
        days_and_unit = user_input.split(":")
        print(days_and_unit)
        days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
        print(days_and_unit_dictionary)
        validate_and_execute()
    except IndexError:
        print("Wrong input")
