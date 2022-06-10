# Chapter 10: Try it Yourself. 10-04: Guest Book.

while True:
    name = input("\nA simple greeting and guest book for all the Guests."
                 "\n(Note: Please enter 'quit' when you are finished.)"
                 "\nPlease enter your name: ")

    if name == 'quit':
        break
    else:
        with open('pcc_guest_book.txt', 'a') as file_object:
            print(f"Welcome, {name.title()}!")
            file_object.write(f"{name.title()}, your visit has been recorded.\n")
