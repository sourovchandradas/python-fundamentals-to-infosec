languages = ['python', 'javascript', 'c++', 'bash']

# 1. len()
print(f"Initial list length: {len(languages)}")

# 2. append()
languages.append('go')

# 3. insert()
languages.insert(1, 'html')
print("After adding elements:", languages)

# 4. sorted()
print("Temporarily sorted:", sorted(languages))

# 5. reverse()
languages.reverse()
print("After reverse():", languages)

# 6. pop()
popped_lang = languages.pop()
print(f"Popped element: {popped_lang}")

# 7. remove()
languages.remove('html')

# 8. del
del languages[0]
print("After removals:", languages)

# 9. sort()
languages.sort()
print("Final permanently sorted list:", languages)
