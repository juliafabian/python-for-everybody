# You should prompt the user for an integer. The user should be able to give only integer otherwise the program should retry with a friendly message.
# The number the user gives should be recursively multiplied by itself
# example: user gives 5 as input. The result should be 5*4*3*2*1. (n! = n * (n-1) * (n-2) * (n-3) etc.)

while True:
    number = input("Enter a number: ")
    try:
        int_number = int(number)
        break
    except:
        print("This is not a number, please try again")
        continue

# define the variable multiply so i can use it in the upcoming loop
carry_over = int_number
# create a for-loop, which runs the amount of times in the brackets, "range" means it runs downwards from the given variable
# the downward counting is "saved" in the variable "counter"

for counter in range(int_number-1): 
    #everytime the loop runs, i need to overwrite the int_number by decreasing it by 1
    int_number = int_number - 1
    # the carry_over has an initial value of the given int_number. 
    # Everytime the loop runs, i multiply the current carry_over with the current int_number which overwrites the variable carry_over !outside the loop!
    # So we multiply the given number recursively by itself round after round 
    carry_over = carry_over * int_number
print(carry_over)
