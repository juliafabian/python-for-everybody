# The famous word in python 'in' can be used for many things such as
# in looping or checking if a list contains something

# create your own 'In' function to check if a list contains something
# The function should take a list as a parameter and should take an object to check
# The function should return true or false

# example_1 = ["apple", "banana", "orange"] -> check if "banana" in the list



def In(lst, object) -> bool:
    found = False
    for i in lst:
        if i == object:
            found = True
            break
    return found

example_1 = ["apple", "banana", "orange"]
result = In(example_1, "orange")

print(result)