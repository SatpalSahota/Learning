squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

print("\n")

#Same as above loop, but made more concise - known as a list comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)
