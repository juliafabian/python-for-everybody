# Open the file romeo.txt √
# For each line, split the line into a list of words using the split() method -> the program should build a list of words √
# For each word on each line check to see if the word is already in the list 33
# If not append it to the list
# When the program completes, sort and print the resulting words in python sort() order

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File name not found")
    quit()

lst = list()

for line in fhand:
    line = line.rstrip()
    single_lst = line.split()
    for word in single_lst:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)