# Exercise 5-8: Hello Admin

usernames = ['admin', 'hardik', 'iyer', 'samson','kartik','siraj']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")
