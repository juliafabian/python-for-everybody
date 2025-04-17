# 1. prompting for integer numbers √
# 2. Until user enters "done" √
# 3. Once "done" is entered print out largest and smallest number ("Maximum is " and "Minimum is ") √
# 4. If user enters not a valid number catch it with try/except and put "Invalid input" √
# 5. Enter: 7, 2, bob, 10, 4 and done

largest = None
smallest = None

while True: 
    num = input("Enter a number: ")
    if num == "done":
        print("Maximum is", largest)
        print("Minimum is", smallest)
        break
    try:
        num_int = int(num)
        if smallest is None or num_int < smallest:
            smallest = num_int
        if largest is None or num_int > largest:
            largest = num_int
    except:
        print("Invalid input")
        continue

