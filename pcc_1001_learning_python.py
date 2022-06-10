# Chapter 10: Try it Yourself. 10-01: Learning Python.

# Reading an Entire File.

with open('pcc_learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)

# Reading Line by Line.

filename = 'pcc_learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Making a List of Lines from a File

filename = 'pcc_learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
