# Chapter 11: Testing a Function

from pcc_1100_name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    middle = input("Please give me a middle name (Press enter if not available): ")
    if middle == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last, middle)
    print(f"\tNeatly formatted name: {formatted_name}.")
