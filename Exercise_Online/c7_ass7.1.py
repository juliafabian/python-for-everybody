# Write a program that prompts for a file name
# Then opens that file and reads through it
# And prints the contents of the file in upper case

fname = input('File name: ')
try:
    fhand = open(fname)
except:
    print('File name not found')
    quit()

for line in fhand:
    line = line.rstrip()
    upper_case = line.upper()
    print(upper_case)