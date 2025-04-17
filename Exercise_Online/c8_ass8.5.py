fname = input("Enter file name: ")
try: 
    fhand = open(fname)
except:
    print("File name not found")
    quit()

count = 0

for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        lst = line.split()
        print(lst[1])
        count = count + 1
print("There were", count, "lines in the file with From as the first word")