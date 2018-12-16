guest_list = ['nelson mandela', 'sadiq khan', 'bruce lee']

invite = ", you are hereby invited to dinner."

print(guest_list[0].title() + invite)
print(guest_list[1].title() + invite)
print(guest_list[2].title() + invite)
print(guest_list[0].title() + invite)
print("\n")

regret = "Sadly, " + guest_list[2].title() + " is unable to attend dinner."

print (regret)

guest_list[2] = 'bill gates'

print(guest_list[0].title() + invite)
print(guest_list[1].title() + invite)
print(guest_list[2].title() + invite)
