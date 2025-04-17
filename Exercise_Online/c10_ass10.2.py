# Write a program to read through the mbox-short.txt.
# Figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fhand = open(name)

counts = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        piece = time.split(':')
        counts[piece[0]] = counts.get(piece[0], 0) + 1

for k, v in sorted(counts.items()):
    print(k, v)