import random

def roll():
    rolls= []
    rolls.append(random.randint(1,6))
    rolls.append(random.randint(1,6))
    rolls.append(random.randint(1,6))
    rolls.append(random.randint(1,6))
    rolls.append(random.randint(1,6))
    rolls.append(random.randint(1,6))
    return rolls
    
print(roll())
