# Chapter 10: Try it Yourself. 10-10: Common Words.

def count_words(filename, find_word):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the filename '{filename}' does not exist.")

        pass
    else:
        # Count the approximate number of words in the file.
        num_words = contents.lower().count(find_word)
        print(f"\nIn the file '{filename}', the word '{find_word}' appeared {num_words} times.")


count_words('pcc_dragons_and_cherry.txt', 'dragons')
count_words('pcc_dragons_and_cherry.txt', 'cherry')
count_words('pcc_dragons_and_cherry.txt', 'the')
count_words('pcc_dragons_and_cherry.txt', 'the ')
count_words('pcc_dragons_and_cherry.txt', 'there')
