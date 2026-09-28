# Exercise 8-15: Printing Models


# printing_functions.py
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)



# printing_models.py
# Import functions from printing_functions.py

import printing_functions

unprinted_designs = ['car toy', 'flower vase', 'chess board']
completed_models = []

# Call functions using dot notation
printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)
