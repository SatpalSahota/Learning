alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = '5'

print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".\n")

alien_0['x_pos'] = 0
alien_0['y_pos'] = 25
alien_0['speed'] = 'medium'

print("Original position: " + str(alien_0['x_pos']) + ", " 
+ str(alien_0['y_pos']))

# Move alien to the right
# Determine how far to move based on speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3 # Must be a fast alien

# New = old + increment
alien_0['x_pos'] = alien_0['x_pos'] + x_increment
print("New position: " + str(alien_0['x_pos']) + ", "
+ str(alien_0['y_pos']) +"\n")

print(alien_0)
del alien_0['points']
print(alien_0)