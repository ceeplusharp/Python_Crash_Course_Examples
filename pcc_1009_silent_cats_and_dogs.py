# Chapter 10: Try it Yourself. 10-09: Silent Cats and Dogs.

def print_file(filename):
    """Printing the contents of a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(f"\n'{filename}'")
        print(contents.rstrip())


filenames = ['pcc_dogs.txt', 'pcc_birds.txt', 'pcc_cats.txt']
for filename in filenames:
    print_file(filename)
