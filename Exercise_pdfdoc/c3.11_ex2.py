#Rewrite program using try and except to handle non-numeric input

input_hours = input("Enter Hours: ")
input_rate = input("Enter Rate: ")
try:
    hours_float = float(input_hours)
    rate_float = float(input_rate)
except:
    print("Error, please enter numeric input")
    exit(1)

payout = 0

if hours_float <= 40:
    #over_time = hours_float - 40
    payout = hours_float * rate_float 
else:
    over_time = hours_float - 40
    payout = (40 * rate_float) + (rate_float * over_time * 1.5)
print("Pay:", payout)