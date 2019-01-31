height = input("How tall are you in cm? ")
height = int(height)
limit = 2.54*36

if height >= limit:
    print("\nYou are tall enough ot ride!")
else:
    print("You'll be able to ride whe you're a little older.")