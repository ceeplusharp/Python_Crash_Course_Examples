# Chapter 10: Try it Yourself. 10-06: Addition.

print("\nGive me two numbers, and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You can't add strings!")
    else:
        print(f"Result: {answer}")
