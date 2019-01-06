guest_list = ['nelson mandela', 'sadiq khan', 'bruce lee']

invite = ", you are hereby invited to dinner."

for guest in guest_list:
    print(guest.title() + invite)

print("\n")

regret = "Sadly, " + guest_list[2].title() + " is unable to attend dinner.\n"

print (regret)

guest_list[2] = 'bill gates'

for guest in guest_list:
    print(guest.title() + invite)
