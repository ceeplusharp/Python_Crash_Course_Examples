# Chapter 9: Try it Yourself. 9-15: Lottery Analysis.

from random import randint, choice
import string
import random

a = 0
b = 0
c = 0
d = 0
lottery_list = []
lottery_pick = []
my_ticket = []

while a < 10:
    random_no = randint(1, 55)
    lottery_list.append(random_no)
    while a < 5:
        random_ltr = random.choice(string.ascii_uppercase)
        lottery_list.append(random_ltr)
        break
    a += 1

print(f"\nLottery Machine: {lottery_list}")

while b < 4:
    picked = choice(lottery_list)
    lottery_pick.append(picked)
    b += 1

print(f"\nAny ticket matching with the Lottery Pick: {lottery_pick} wins a prize!")

while c < 4:
    my_pick = choice(lottery_list)
    my_ticket.append(my_pick)
    c += 1
    if c == 4:
        d += 1
        if lottery_pick != my_ticket:
            c = 0
            my_ticket = []
            continue
        else:
            print(f"\nCongratulations! Your ticket: {my_ticket} wins a prize!"
                  f"\nTotal number of tries: {d}")
