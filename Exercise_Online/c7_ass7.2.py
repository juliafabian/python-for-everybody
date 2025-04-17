# Write a program that prompts for a file name
# Then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# Compute the average of those values and produce an output like:
# Average spam confidence: 0.7507185185185187


fname = input('File name: ')
try:
    fhold = open(fname)
except:
    print('File name not found')
    quit()
count = 0
total = 0
for line in fhold:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence'):
        count = count + 1
        string_number = line.split(":")             # bei der .split-function wird in Klammern der Ort angegeben, an dem getrennt werden soll. 
        string_number = string_number[1].lstrip()   # [1].lstrip() kann auch in line 21 direkt hinter ) stehen. 
        float_number = float(string_number)         # change the numbers into float
        total = total + float_number                # add them with one another
print('Average spam confidence:', total/count)      # calculate the average + print
