# Exercise 6-04: Glossary 2

glossary = {
    'variable': 'A named storage location in memory for holding data.',
    'string': 'A series of characters enclosed in quotes.',
    'list': 'A collection of items in a particular order.',
    'loop': 'A structure used to repeat a block of code multiple times.',
    'dictionary': 'A collection of key-value pairs.',
    # Five new terms added below
    'bolean': 'A data type that has one of two possible values: True or False.',
    'tuple': 'An immutable, ordered collection of items.',
    'method': 'An action that Python can perform on a piece of data.',
    'slice': 'A specific group of items from a list or string.',
    'function': 'A name block of code designed to perform a specific task.',
}

# Loop through the dictionary's keys and values
for word, definition in glossary.items():
    print(f"\n{word.title()}:")
    print(f"    {definition}")
