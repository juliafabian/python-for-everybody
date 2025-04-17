# Write a function called chop that takes a list and modifies it, removing the first and last elements and returns None.
# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements

# 1.:
def chop(lst):
    del lst[0]
    del lst[-1]
    return lst

fruit = ['banana', 'apple', 'banana', 'kiwi', 'banana', 'pineapple']
chop(fruit)
print(fruit)

# 2.:
def middle(lst):
    return lst[1:-1]

fruit = ['banana', 'apple', 'banana', 'kiwi', 'banana', 'pineapple']
rest = middle(fruit)
print(rest)