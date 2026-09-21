# Exercise 7-04: Pizza Toppings

prompt = "\nPlease enter a pizza topping you'd like:"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    
    if topping.lower() != 'quit':
        print(f"I'll add {topping} to your pizza!")
    else:
        break
