# Chapter 10: Is Your Birthday Contained in Pi?

filename = 'pcc_pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

while True:
    birthday = input("\nLet us see if your birthday is in the first million digits of Pi!"
                     "\n(Note: Please enter 'quit' when you are finished.)"
                     "\nEnter your birthday, in the form mmddyy: ")

    if birthday == 'quit':
        break
    elif birthday in pi_string:
        print("Nice! Your birthday appears in the first million digits of Pi!")
    else:
        print("Oops. Your birthday does not appear in the first million digits of Pi.")
    continue
