prompt = "\nPlease enter your age: "

age = int(input(prompt))

print(age)

while True:
    if age < 0:
        print("Please enter a valid age.")
        break
    elif age in range (0, 3):
        print("Price: FREE")
        break
    elif age in range (3, 13):
        print("Price: $10")
        break
    else:
        print("Price: $15")
        break
