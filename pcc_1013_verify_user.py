# Chapter 10: Try it Yourself. 10-13: Verify User.

import json


def get_stored_username():
    """Greet stored username if available."""
    filename = 'pcc_username2.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'pcc_username2.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        prompt = input(f"Is '{username}' the right username? Type 'yes' or 'no': ")
        if prompt == 'yes':
            print(f"Welcome back, {username}!")
        elif prompt == 'no':
            username = get_new_username()
    elif not username:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()