# Chapter 10: Try it Yourself. 10-08: Cats and Dogs.

def print_file(filename):
    """Printing the contents of a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"\nSorry, the filename '{filename}' does not exist.")
    else:
        print(f"\n'{filename}'")
        print(contents.rstrip())


filenames = ['pcc_dogs.txt', 'pcc_birds.txt', 'pcc_cats.txt']
for filename in filenames:
    print_file(filename)
