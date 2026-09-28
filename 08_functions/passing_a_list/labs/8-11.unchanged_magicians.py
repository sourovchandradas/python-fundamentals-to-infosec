# Exercise 8-11: Unchanged Magicians

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

# Create a new function to work with empty list
def great_magicians(magicians):
    # Create new empty list
    new_list = []
    for magician in magicians:
        # Append item into new empty list using append.() method
        new_list.append(magician + ", the Great.")
    return new_list

magicians = ['alice', 'david', 'carolina']

# Print Original list
print("Original List:")
show_magicians(magicians)

# Print Modified list
make_great = great_magicians(magicians)
print("\nModified List:")
show_magicians(make_great)
