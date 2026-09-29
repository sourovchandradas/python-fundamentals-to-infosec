# Exercise 8-13: Cars

def make_car(manufacturer, model, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

# Example call with required info + two extra details
car = make_car(
    'Mercedes-Benz',
    'C-Class',
    color='Black',
    sunroof=True
)

print(car)
