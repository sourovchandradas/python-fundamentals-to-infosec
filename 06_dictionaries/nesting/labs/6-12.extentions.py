# Exercise 6-12: Extended Cities Program

cities = {
    'ahmedabad': {
        'country': 'india',
        'population': '8.4 million',
        'best_time_to_visit': 'october to march',
        'famous_food': ['dhokla', 'khandvi', 'fafdapale'],
        'fact': 'it is india\'s first unesco world heritage city and home to sabarmati ashram.',
    },
    'bengaluru': {
        'country': 'india',
        'population': '13.1 million',
        'best_time_to_visit': 'september to february',
        'famous_food': ['masala dosa', 'bisi bele bath', 'filter coffee'],
        'fact': 'it is known as the "silicon valley of india" due to its thriving tech sector.',
    },
    'lucknow': {
        'country': 'india',
        'population': '3.8 million',
        'best_time_to_visit': 'october to march',
        'famous_food': ['tunday kabab', 'lucknawi biryani', 'sheermal'],
        'fact': 'it is historically known as the "city of nawabs" and famous for chikankari embroidery.',
    },
}

print("=" * 110)
print("                                       CITY GUIDE & EXPLORER PROGRAM       ")
print("=" * 110)

# Loop through all cities with improved visual formatting
for city, info in cities.items():
    print(f"\n📍 CITY: {city.upper()}")
    print("-" * 107)
    print(f"  Country          : {info['country'].title()}")
    print(f"  Population       : {info['population']}")
    print(f"  Best Time Visit  : {info['best_time_to_visit'].title()}")
    print(f"  Fact             : {info['fact'].capitalize()}")
    
    # Printing nested list of foods nicely
    print("  Famous Foods     :")
    for food in info['famous_food']:
        print(f"    • {food.title()}")

print("\n" + "=" * 110)
