my_list = ["january", "february", "march"]

# print the original list
print("original list: ", my_list)

# print the specific element from the list
print(my_list[1])

# append an element to the list
my_list.append("april")
print("list after appending an element: ", my_list)

# insert an element at specific position
my_list.insert(2, "December")
print("list after inserting an element at index 2: ", my_list)

# remove an element from the list
my_list.remove("December")
print("list after removing december: ", my_list)

# get the index of an element
index = my_list.index("february")
print("index of ele february: ", index)

# get the count of a particular element in the list
count = my_list.count("january")
print("count of element january:", count)

# sort the list in ascending order
my_list.sort()
print("list after sorting in ascending order:", my_list)

# reverse the list
my_list.reverse()
print("list after reversing:", my_list)

# copy the list
new_list = my_list.copy()
print("copy of the original list: ", new_list)

# clear the list
my_list.clear()
print("list after clearing: ", my_list)
