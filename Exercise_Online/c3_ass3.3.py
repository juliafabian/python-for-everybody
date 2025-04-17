#promt for a score between 0.0 and 1.0

input_score = input("Enter Score:")
try:
    score_float = float(input_score)
except:
    print("Error")
    exit(1)

if score_float < 0.0: 
    print("Error")
elif score_float > 1.0:
    print("Error")
elif score_float >= 0.9:
    print("A")
elif score_float >= 0.8:
    print("B")
elif score_float >= 0.7:
    print("C")
elif score_float >= 0.6:
    print("D")
elif score_float < 0.6:
    print ("F")
