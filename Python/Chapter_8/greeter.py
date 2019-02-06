def greet_user(username):
    """Display a simple greeting."""
    print("Hello " + username.title() + "!")

user = input("Enter name here: ")
greet_user(user)
