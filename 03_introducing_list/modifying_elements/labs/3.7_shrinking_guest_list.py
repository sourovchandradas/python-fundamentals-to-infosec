# Create an initial guest list
guests = ['virat kohli', 'novak djokovic', 'leonel messi', 'ms dhoni', 'sergio ramos', 'michael phelps']

print("Notice: The new table will not arrive in time. Only two guests can be accommodated.\n")

# Remove guests until only two remain
removed_guest = guests.pop()
print(f"Sorry, {removed_guest.title()}, I can no longer invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry, {removed_guest.title()}, I can no longer invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry, {removed_guest.title()}, I can no longer invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry, {removed_guest.title()}, I can no longer invite you to dinner.")

# Confirm remaining guests
print(f"\nDear {guests[0].title()}, you are still invited to dinner.")
print(f"Dear {guests[1].title()}, you are still invited to dinner.")

# Clean up remaining list elements
del guests[0]
del guests[0]

print("\nFinal guest list state:", guests)
