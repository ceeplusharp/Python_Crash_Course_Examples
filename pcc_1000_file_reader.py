# Chapter 10: Reading from a File.

# Reading an Entire File.

with open('pcc_pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# Reading Line by Line.

filename = 'pcc_pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Making a List of Lines from a File

filename = 'pcc_pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

print(lines)
for line in lines:
    print(line.rstrip())
