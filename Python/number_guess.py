import random

number = random.randint(1, 101)

prompt = "Guess the number between 1 and 100! "

active = True

guess = int(input(prompt))


def main():
    while active == True:
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct!")
            break


if active == True:
    if guess < 1:
        print("Please enter a number higher than 0.")
        prompt
    elif guess > 100:
        print("Please enter a number lower than 101.")
        prompt
    else:
        main()
else:
    print("")
