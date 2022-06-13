# Chapter 10: Saving and Reading User-Generated Data

import json

filename = 'pcc_username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
