# Chapter 10: Using json.dump() and json.load()

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'pcc_numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
