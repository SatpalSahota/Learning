from random import *

stop = 30
for i in range(5):
    for x in range(6):
        assign = []
        for x in range(5):
            dice_roll = randint(1, 6)
            assign.append(dice_roll)
        print(assign)
    print("\n")
