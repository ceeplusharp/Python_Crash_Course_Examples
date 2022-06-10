# Chapter 10: Try it Yourself. 10-02: Learning C.

filename = 'pcc_learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    rev_line = line.replace('Python', 'C')
    print(rev_line.rstrip())
