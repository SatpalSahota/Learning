# Start with users that need to be identified, and an empty list to hold users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until no more unconfirmed_users remain, and move each into confirmed_users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Confirm new users
print("\nThe following users have been confirmed: ")
for user in confirmed_users:
    print(user.title())
