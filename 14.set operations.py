# create a set with elements
my_set = {1, 2, 3, 4, 2}
for element in my_set:
    print(element, end=" ")
print("")

# add element to set
my_set.add(0)
for element in my_set:
    print(element, end=" ")
print("")

# remove the element
my_set.remove(2)
for element in my_set:
    print(element, end=" ")
print("")
# my_set.discard(2) -> Use the discard method if you want to remove an element that may not be in the set
# this will not raise an error even if 2 is not in the set

# creating two sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
# union of two sets
s3 = s1.union(s2)
print(s3)

# intersection of two sets
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1.intersection(s2)
print(s3)

# difference of sets ( belong to s1 but not to s2 )
s3 = s1.difference(s2)
print(s3)
