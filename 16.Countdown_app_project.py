from datetime import datetime

user_input = input("enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
# print(input_list)

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()

# calculate how many days from now till deadline
time_till = deadline_date - today_date
hours = int(time_till.total_seconds() / 60 / 60)
print(f"Dear user time remaining for your goal : {goal} is {time_till.days} days and { hours } hours")
