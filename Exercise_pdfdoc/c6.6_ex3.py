# word = 'Banane' 
# count = 0
# for zeichen in word:
#     if zeichen == 'a': 
#         count = count + 1
# print(count)

# Lagern sie den Code in eine Funktion namens count aus und verallgemeinern Sie diese so, dass sie die Zeichenmkette und den Bcuhstaben als Argumente akzeptieren

word = "banana"
counter = 0
def count(word, counter):
    for zeichen in word:
        if zeichen == 'a':
            counter = counter + 1
    print(counter)

count("ananasasas", 0)

