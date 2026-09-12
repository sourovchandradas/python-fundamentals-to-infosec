# Exercise 5-10: Checking Usernames

current_users = ['rahul','krunal','shardul','surya','manish','unadkat','dube']
new_users = ['patidar','shardul','samson','nitish','dube','unadkat','kishan']

# Convert all current usernames to lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    # Convert new_user to lowercase before searching in the reference list
    if new_user.lower() in current_users_lower:
        print(f"Sorry,'{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"Great, '{new_user}' is available!")
