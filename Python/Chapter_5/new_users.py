current_users = ['john', 'mary', 'afobe', 'admin', 'rita']

new_users = ['harry', 'john', 'remus', 'mike', 'rita']
user_add = []

for user in new_users:
    if user in current_users:
        print("Sorry " + user.title() + ", you need to make a new username!")
    else:
        print("Welcome " + user.title() + "! Please make a username.")
        user_add.append(user)

current_users.append(user_add)
print("\n")
print(current_users)