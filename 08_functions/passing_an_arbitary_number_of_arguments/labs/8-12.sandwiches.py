# Exercise 8-12: Sandwiches

def make_sandwich(*items):
    print("\nMaking a sandwich with the following item:")
    for item in items:
        print("- " + item)

# Call the function three times with different number of argumments
make_sandwich('chicken', 'lettuce', 'mayo')

make_sandwich('egg', 'tomato')

make_sandwich('mutton', 'cheese', 'onion', 'mastard', 'pickles')
