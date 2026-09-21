# Exercise 7-05: Movie Tickets

while True:
    prompt = (input("Enter your age(or type 'quit' to exit): "))

    # Allow the user to stop the loop
    if prompt.lower() == 'quit':
        break

    # Convert input to an integer for age comparison
    person_age = int(prompt)
    ticket_price = 0
    if person_age < 3:
        ticket_price = 0
    elif person_age >= 3 and person_age <= 12:
        ticket_price = 10
    elif person_age > 12:
        ticket_price = 15

    print(f"The cost of your movie ticket is {ticket_price}$.")
