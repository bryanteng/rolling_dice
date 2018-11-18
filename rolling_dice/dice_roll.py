import random

def roll(num):
    rolls= []
    index = 0
    while index < num:
        rolls.append(random.randint(1,6))
        index+=1
    return rolls

print(roll(6))
