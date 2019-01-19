import random

number = random.randint(1,101)
print(number)

print("Guess the number between 1 and 100!")
guess = input()

if guess == number:
    print("Well done, that's right!")

print("Wrong! Guess again!")
number = input