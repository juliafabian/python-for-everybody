frucht = "banana"

# zeichen = frucht[1]               -> Buchstabe an Position 1
# print(zeichen)
# len(frucht)                       -> Gesamtanzahl d. Buchstaben im Wort
# length = len(frucht)
# letzter = frucht[length - 1]      -> letzter Buchstabe d. Worts ist -1, vorletzter -2 usw. 

index = 0
length = len(frucht)

while index < len(frucht):
    letzter = frucht[length -1 - index]     # es gibt keinen Buchstaben mit dem Index 6 (da ab 0 gezählt wird), deshalb length -1 und dann - index
    print(letzter)
    index = index + 1

