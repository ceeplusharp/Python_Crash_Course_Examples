# Chapter 10: Working with Multiple Files

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the filename '{filename}' does not exist.")
        pass
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file '{filename}' has about {num_words} words.")


filenames = ['pcc_alice.txt', 'pcc_siddhartha.txt', 'pcc_moby_dick.txt', 'pcc_little_women.txt']
for filename in filenames:
    count_words(filename)
