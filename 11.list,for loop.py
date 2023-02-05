# list - to store multiple items in a single variable.
# for loop - it is used to iterate over a sequence (like a list)
# .split() - splits a string into list eg- 10 20 30 40 -> [10,20,30,40]
calculation_to_hours = 24
name_of_unit = "hour"


def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculation_to_hours} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(int(user_input_number))
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0, please enter positive number")
        else:
            print("its a negative number, please enter positive number")
    except ValueError:
        print("Invalid Number")


user_input = ""
while user_input != "exit":
    user_input = input("Enter number of days and i will convert it to hours!, for exiting the program type exit\n")
    for num_of_days_element in user_input.split():
        validate_and_execute()
