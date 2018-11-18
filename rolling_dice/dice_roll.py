import random

def roll(num):
    rolls= []
    average = 0
    rolls_dict = {}
    index = 0

    while index < num:
        x = random.randint(1,6)
        rolls.append(x)
        index+=1
        average+= x
        print_roll(x)
        if x in rolls_dict:
            rolls_dict[x] = rolls_dict[x]+1
        else:
            rolls_dict[x] = 1

    print("The average roll was " +str(average/num) + " in " +str(num)+ " rolls.")
    for key,val in rolls_dict.items():
        print(str(key)+ " was rolled "+str(val) + " time(s)")




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

roll(input("Enter number of dices to roll: "))
