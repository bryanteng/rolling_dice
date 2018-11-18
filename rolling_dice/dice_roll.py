import random

def roll(num):
    rolls= []
    index = 0
    while index < num:
        rolls.append(random.randint(1,6))
        index+=1
    for x in rolls:
        print_roll(x)

def print_roll(num):
    if num == 6:
        print("--------")
        print("|O     O|")
        print("|O     O|")
        print("|O     O|")
        print("--------")
    elif num == 5:
        print("--------")
        print("|O     O|")
        print("|   O   |")
        print("|O     O|")
        print("--------")
    elif num == 4:
        print("--------")
        print("|O     O|")
        print("|       |")
        print("|O     O|")
        print("--------")
    elif num == 3:
        print("--------")
        print("|      O|")
        print("|   O   |")
        print("|O      |")
        print("--------")
    elif num == 2:
        print("--------")
        print("|      O|")
        print("|       |")
        print("|O      |")
        print("--------")
    elif num == 1:
        print("--------")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print("--------")

roll(6)
