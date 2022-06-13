# Chapter 10: Try it Yourself. 10-05: Programming Poll.

while True:
    name = input("\nA simple poll to ask people about their favorite programming language."
                 "\n(Note: Please enter 'quit' when you are finished.)"
                 "\nPlease enter your name: ")
    if name == 'quit':
        break
    else:
        fave_language = input("Please enter your favorite programming language: ")
        reason = input("Please enter why: ")

        with open('pcc_responses.txt', 'a') as file_object:
            print(f"{name.title()}'s favorite programming language is {fave_language.upper()}"
                  f" because {reason}.")
            file_object.write(f"Name: {name.title()},"
                              f" Favorite Programming Language: {fave_language.upper()},\n"
                              f"\tReason: {reason}\n")
