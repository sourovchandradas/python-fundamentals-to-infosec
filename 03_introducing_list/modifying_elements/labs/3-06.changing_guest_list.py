# Create an initial guest list
guests = ['virat kohli', 'leonel messi', 'cristiano ronaldo']

# Identifying unavailable guest and replace them
cant_make_it = guests[2]

print(f"Unfornately, {cant_make_it.title()} cann't make it to dinner.\n")

guests[2] = 'novak djokovic'

# Re-issue invitations
print(f"Dear {guests[0].title()}, you are invited to the dinner!")
print(f"Dear {guests[1].title()}, you are invited to the dinner!")
print(f"Dear {guests[2].title()}, you are invited to the dinner!")
