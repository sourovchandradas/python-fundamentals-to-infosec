# Exercise 8-09: 

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

# Create great_magician to modify list.
def great_magician(magicians):
    for i in range(len(magicians)):
        magicians[i] = magicians[i] + " the Great."

magician_list = ['alice', 'david', 'carolina']

# Modify the list
great_magician(magician_list)

# Show the modify list
show_magicians(magician_list)
