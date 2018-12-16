motorbikes = []

motorbikes.append('honda')
motorbikes.append('yamaha')
motorbikes.append('suzuki')
motorbikes.append('ducati')
print(motorbikes)

# ~ pop() is a function that deletes from the last position in a list (or [-1]).
# ~ popped_motorbike = motorbikes.pop()
# ~ print(motorbikes)
# ~ last_owned = (popped_motorbike).title()
# ~ print(last_owned)

# ~ motorbikes.insert(2, 'ducati')
# ~ print(motorbikes)

# ~ del motorbikes[0]
# ~ print(motorbikes)

# ~ del motorbikes[1]
# ~ print(motorbikes)

first_owned = motorbikes.pop(0)
print("The first motorbike I owned was a " + first_owned.title() + ".\n")

# ~ Showing that you can remove string values of lists using list.remove().
print(motorbikes )
motorbikes.remove('ducati')
print(motorbikes )
print("\n")


motorbikes.append('ducati')

print(motorbikes)
too_expensive = 'ducati'
motorbikes.remove(too_expensive)
print(motorbikes)
print("\nA " + too_expensive.title() + " is too expensive for me.\n")
