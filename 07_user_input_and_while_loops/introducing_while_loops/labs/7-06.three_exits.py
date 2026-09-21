# Exercise 7-06: Three Exits

prompt = "Enter your age(or type 'quit' to exit): "

# Version 1: Conditional test in while statement
user_input = ""

while user_input.lower() != 'quit':
    user_input = input(prompt)
    if user_input.lower() != 'quit':
        person_age = int(user_input)
        ticket_price = 0
        if person_age < 3:
            ticket_price = 0
        elif person_age >= 3 and person_age <= 12:
            ticket_price = 10
        elif person_age > 12:
            ticket_price = 15

        print(f"The cost of your movie ticket is {ticket_price}$.")

# Version 2: Active variable (Flag)

active = True

while active:
    user_input = input(prompt)
    if user_input.lower() == 'quit':
        active = False
    else:
        person_age = int(user_input)
        ticket_price = 0
        if person_age < 3:
            ticket_price = 0
        elif person_age >= 3 and person_age <= 12:
            ticket_price = 10
        elif person_age > 12:
            ticket_price = 15
        print(f"The cost of your movie ticket is {ticket_price}$.")

# Version 3: Using break statement

while True:
    user_input = input(prompt)
    if user_input.lower() == 'quit':
        break
    person_age = int(user_input)
    if person_age < 3:
        ticket_price = 0
    elif person_age >= 3 and person_age <= 12:
        ticket_price = 10
    elif person_age > 12:
        ticket_price = 15
    print(f"The cost of your movie ticket is {ticket_price}$.")
