"""
Dice roll simulator
The goal is to create a program 
that will simulate the roll of dice.

Topics: random module, looping, and if-else
Hint: Using a random module generate a random https://github.com/JeffreyAsuncion/PythonCodingProjects.git
number between the range from 1 to 6 when the user wants.
"""

import random

num_sided_dice = 6

print("-" * 50)
print(" "*15 + "Dice roll simulator")
print("-" * 50)
print()
num_sided_dice = int(input("How many sided dice (minimum=6): "))
if num_sided_dice < 6:
    print("Defaulting to 6 sided dice")
    num_sided_dice = 6


while True:
    print("Please choose one of the following: ")
    print("\t1. roll the dice")
    print("\t2. exit")
    choice = int(input(">>> "))
    if choice == "":
        True
    elif choice == 1:
        print()
        print("@"*25)
        print("rolling dice...")
        print("You rolled")
        print(random.randint(1, num_sided_dice))
        print("@"*25+"\n")
    elif choice == 2:
        print("Goodbye, Signing off.")
        break
    else:
        print("*" *25)
        print("*" *25+"\n")