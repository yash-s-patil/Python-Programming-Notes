# Function is a block of code which can be used multiple times, it avoids writing the same code again and again
calculation_to_hours = 24
name_of_unit = "hour"


def days_to_units(number_of_days, custom_message):
    print(f"{number_of_days} days are {number_of_days * calculation_to_hours} {name_of_unit}")
    print(custom_message)


days_to_units(35, "Awesome")
days_to_units(20, "Looks great")
