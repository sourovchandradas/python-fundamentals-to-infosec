# Create an initial guest list
guests = ['virat kohli', 'leonel messi', 'novak djokovic']

print("Great news! A larger table has been reserved.\n")

# Add new guests: start, middle and end
guests.insert(0, 'ms dhoni')
guests.insert(2, 'sergio ramos')
guests.append('michael phelps')

# Re-issue invitations
print(f"Dear {guests[0].title()}, you are invited to the dinner!")
print(f"Dear {guests[1].title()}, you are invited to the dinner!")
print(f"Dear {guests[2].title()}, you are invited to the dinner!")
print(f"Dear {guests[3].title()}, you are invited to the dinner!")
print(f"Dear {guests[4].title()}, you are invited to the dinner!")
print(f"Dear {guests[5].title()}, you are invited to the dinner!")
