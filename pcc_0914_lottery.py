# Chapter 9: Try it Yourself. 9-14: Lottery.

from random import randint, choice
import string
import random


i = 0
j = 0
lottery_list = []
lottery_pick = []

while i < 10:
    random_no = randint(1, 55)
    lottery_list.append(random_no)
    while i < 5:
        random_ltr = random.choice(string.ascii_uppercase)
        lottery_list.append(random_ltr)
        break
    i += 1

print(f"Lottery Machine: {lottery_list}")

while j < 4:
    picked = choice(lottery_list)
    lottery_pick.append(picked)
    j += 1

print(f"\nAny ticket matching with the Lottery Pick: {lottery_pick} wins a prize!")
