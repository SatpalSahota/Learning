import random

number = random.randint(1,101)

prompt = "Guess the number between 1 and 100! "

while True:
    guess = int(input(prompt))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct!")
        break
