#noch erledigen, ist noch genau der code von chapter 3


input_hours = input("Enter Hours: ")
input_rate = input("Enter Rate: ")
hours_float = float(input_hours)
rate_float = float(input_rate)
payout = 0

if hours_float <= 40:
    #over_time = hours_float - 40
    payout = hours_float * rate_float 
else:
    over_time = hours_float - 40
    payout = (40 * rate_float) + (rate_float * over_time * 1.5)
print("Pay:", payout)