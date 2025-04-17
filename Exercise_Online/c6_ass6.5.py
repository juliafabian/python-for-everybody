# write code using find() and string slicing to extract the number at the end of the line
# Convert the extracted value to a floating point number and print it out

text = "X-DSPAM-Confidence:    0.8475"

first_pos = text.find("0")

last_pos = text.find("5")

number_extract = text[first_pos : ]

number_float = float(number_extract)
print(number_float)
