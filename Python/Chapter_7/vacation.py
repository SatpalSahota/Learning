vacation = {}

vacation_polling = True

while vacation_polling:
    name = input("\nWhat is your name? ")
    place = input("Where would you like to go on holiday? ")
    vacation[name] = place
    repeat = input("Would you like to let another person respond? yes/no ")
    if repeat == 'no':
        vacation_polling = False

print("\n\n--- Results---")
for name, place in vacation.items():
    print(name.title() + " would like to go to " + place.title())
