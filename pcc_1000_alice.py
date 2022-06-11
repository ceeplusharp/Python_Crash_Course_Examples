# Chapter 10: Handling the FileNotFoundError Exception

# Analyzing Text
#
# title = "Alice in Wonderland"
# print(title.split())

filename = 'pcc_alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the filename '{filename}' does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file '{filename}' has about {num_words} words.")
