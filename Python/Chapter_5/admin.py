names = ['admin', 'john', 'luke', 'lindy', 'martin']
name = 'admin'

if name in names:
    if name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + name.title() + ", thank you for logging in.")
else:
    print("We need to find some users!")