# Chapter 10: Try it Yourself. 10-03: Guest.

filename = 'pcc_guest.txt'

while True:
    name = input("\nA simple list for all the names of the Guests."
                 "\n(Note: Please enter 'quit' when you are finished.)"
                 "\nPlease enter your name: ")

    if name == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{name.title()}\n")
