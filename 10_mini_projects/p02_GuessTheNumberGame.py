"""
The main goal of the project is 
to create a program that 
randomly select a number in a range 
then the user has to guess the number. 
user has three chances to guess the number 
if he guess correct 
then a message print saying “you guess right 
“otherwise a negative message prints.

Topics: random module, for loop, f strings
"""

import random

high_end = 100
# be able to generate a random number
num = random.randint(1, high_end)
print(num)

guess = int(input("Enter your guess: "))
if guess == num:
    print("You Chose Wisely.")
else:
    print("You Chose Poorly.")




# import random
# number = random.randint(1,10)
# for i in range(0,3):
#     user = int(input("guess the number"))
#     if user == number:
#         print("Hurray!!")
#         print(f"you guessed the number right it's {number}")
#         break
# if user != number:
#     print(f"Your guess is incorrect the number is {number}")
