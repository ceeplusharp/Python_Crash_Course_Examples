# Chapter 10: Using json.dump() and json.load()

import json

filename = 'pcc_numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)
