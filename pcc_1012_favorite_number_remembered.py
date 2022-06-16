# Chapter 10: Try it Yourself. 10-12: Favorite Number Remembered.

import json


def get_new_fave_number():
    """Prompt for a favorite number."""
    fave_number = int(input("Please enter your favorite number: "))
    filename = 'pcc_fave_numbers2.json'
    with open(filename, 'w') as f:
        json.dump(fave_number, f)
    return fave_number


def get_stored_fave_number():
    """Acknowledge favorite number if available."""
    filename = 'pcc_fave_numbers2.json'
    try:
        with open(filename) as f:
            fave_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fave_number


def greet_new_fave_number():
    """Acknowledge the favorite number."""
    fave_number = get_stored_fave_number()
    if fave_number:
        print(f"I know your favorite number! It's {fave_number}.")
    else:
        fave_number = get_new_fave_number()
        print(f"We'll remember that {fave_number} is your favorite number!")


get_new_fave_number()
greet_new_fave_number()
