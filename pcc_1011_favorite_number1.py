# Chapter 10: Try it Yourself. 10-11: Favorite Number.

# Prints acknowledgement message

import json

filename = 'pcc_fave_numbers.json'

try:
    with open(filename) as f:
        fave_numbers = json.load(f)
except FileNotFoundError:
    print(f"Sorry! File does not exist.")
else:
    print(f"I know your favorite number! It's {fave_numbers}.")
