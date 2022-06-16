# Chapter 10: Try it Yourself. 10-11: Favorite Number.

# Input number prompt

import json

filename = 'pcc_fave_numbers.json'

try:
    fave_numbers = int(input("Please enter your favorite number: "))
    with open(filename, 'w') as f:
        json.dump(fave_numbers, f)
except ValueError:
    print("Oops. Please enter valid numbers only.")
