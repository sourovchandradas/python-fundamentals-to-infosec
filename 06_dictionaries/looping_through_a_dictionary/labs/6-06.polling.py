# Exercise 6-06: Polling

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'bash'
}

# List of people who should take the poll
people_to_poll= ['jen', 'edward','matt','sarah','elena']

# Loop of people who should take the poll
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you for responding, {person.title()}!")
    else:
        print(f"Hi {person.title()}, please take our favorite languages poll!")
