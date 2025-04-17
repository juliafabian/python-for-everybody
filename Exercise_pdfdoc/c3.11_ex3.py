#promt for a score between 0.0 and 1.0

input_score = input("Enter Score:")
try:
    score_float = float(input_score)
except:
    print("Bad Score")
    exit(1)

if score_float < 0.0: 
    print("Bad Score")
elif score_float > 1.0:
    print("Bad Score")
elif score_float >= 0.9:
    print("Grade A")
elif score_float >= 0.8:
    print("Grade B")
elif score_float >= 0.7:
    print("Grade C")
elif score_float >= 0.6:
    print("Grade D")
elif score_float < 0.6:
    print ("Grade F")
