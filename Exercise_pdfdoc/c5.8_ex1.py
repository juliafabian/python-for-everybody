anzahl = 0
summing = 0

while True:
    user_input = input("Bitte eine Zahl eingeben: ")
    if user_input == "Done" or user_input == "done":
        print("You entered Done")
        average = summing / anzahl
        print("Anzahl: ", anzahl, ", Summe: ", summing, ", Durchschnitt: ", average)
        break
    try: 
        zahl_int = int(user_input)
    except: 
        print("Please enter a number")
    anzahl = anzahl + 1
    summing = summing + zahl_int