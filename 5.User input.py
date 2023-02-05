# ask the user for input
calculation_to_hours = 24
name_of_unit = "hour"


def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculation_to_hours} {name_of_unit}"


user_input = input("Enter number of days and i will convert it to hours!\n")
user_input_number = int(user_input)
calculated_value = days_to_units(user_input_number)
print(calculated_value)
