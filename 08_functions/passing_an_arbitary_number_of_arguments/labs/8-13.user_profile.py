# Exercise 8-13: User Profile

# Function that builds a user profile using keyword argument
def build_profile(first, last, **user_info):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Build own profile
user_profile = build_profile(
    'Sourov', 'Das', 
    location='Dhaka', 
    field='IT', 
    university='Jahangirnagar University'
)

print(user_profile)
