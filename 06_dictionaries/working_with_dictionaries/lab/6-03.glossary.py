# 6-03: Glossary

# Dictionary storing programming terms and their definitions
glossary = {
    'variable': 'A named storage location in memory for holding data.',
    'string': 'A series of characters enclosed in quotes.',
    'list': 'A collectioin of items in a particular order.',
    'loop': 'A structure used to repeat a block of code multiple times.',
    'dictionary': 'A collection of key-value pairs.'
}

# Print each word and its definition using newline characters for formatting
word = 'variable'
print(f"{word.title()}:\n  {glossary[word]}\n")

word = 'string'
print(f"{word.title()}:\n  {glossary[word]}\n")

word = 'list'
print(f"{word.title()}:\n  {glossary[word]}\n")

word = 'loop'
print(f"{word.title()}:\n  {glossary[word]}\n")

word = 'dictionary'
print(f"{word.title()}:\n  {glossary[word]}\n")
