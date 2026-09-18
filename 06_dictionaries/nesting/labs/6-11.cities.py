# Exercise 6-11: Cities

# Create a dictionary called cities with nested dictionaries for each city
cities = {
    'ahmedabad': {
        'country': 'india',
        'population': '8.4 million',
        'fact': 'it is india\'s first unesco world heritage city, famous for sabarmati ashram.',
    },
    'bengaluru': {
        'country': 'india',
        'population': '13.1 million',
        'fact': 'it is widely regarded as the "silicon valley of india" for its tech industry',
    },
    'lucknow': {
    'country': 'india',
    'population': '3.8 million',
    'fact': 'it is historically known as the "city of nawabs" and famous for its chikankari embroidery.', 
    }
}

# Loop through the dictionary and print details for each city
for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact']

    print(f" Coutnry\t: {country}")
    print(f" Population\t: {population}")
    print(f" Fact\t\t: {fact.capitalize()}")
