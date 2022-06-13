# Chapter 10: Saving and Reading User-Generated Data

import json

username = input("What is your name? ")

filename = 'pcc_username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")
