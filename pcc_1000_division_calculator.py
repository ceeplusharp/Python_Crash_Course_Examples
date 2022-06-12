# Chapter 10: Handling the ZeroDivisionError Exception

# Using try-except blocks.

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# # Using Exceptions to Prevent Crashes.
#
# print("\nGive me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
#
# while True:
#     first_number = input("First number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     else:
#         try:
#             answer = int(first_number) / int(second_number)
#         except ZeroDivisionError:
#             print("You can't divide by zero!")
#             continue
#     print(f"Result: {answer}")

# The else Block.

print("\nGive me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(f"Result: {answer}")
