=====================================================================================================================================================
                                                            LOOPING THROUGH A DICTIONARY
=====================================================================================================================================================

OVERVIEW
-----------------------------------------------------------------------------------------------------------------------------------------------------
A single Python dictionary can contain just a few key-value pairs or millions of pairs. Because a dictionary can contain large amounts of data, 
Python lets you loop through a dictionary. Dictionaries can be used to store information in a variety of ways; therefore, several different 
ways exist to loop through them. You can loop through all of a dictionary's key-value pairs, through its keys, or through its values.


1. LOOPING THROUGH ALL KEY-VALUE PAIRS
-----------------------------------------------------------------------------------------------------------------------------------------------------
* Definition: You can loop through all key-value pairs in a dictionary using a for loop along with the items() method.
* The items() Method: Returns a list of key-value pairs. The for loop then stores each pair in two variables provided (e.g., key and value).

Code Example:
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

Output:
Key: last
Value: fermi

Key: first
Value: enrico

Key: username
Value: efermi

* Variable Naming: You can choose any descriptive variable names for the key and value (e.g., for name, language in favorite_languages.items():).

Code Example:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

Output:
Jen's favorite language is Python.
Sarah's favorite language is C.
Phil's favorite language is Python.
Edward's favorite language is Ruby.


2. LOOPING THROUGH ALL THE KEYS IN A DICTIONARY
-----------------------------------------------------------------------------------------------------------------------------------------------------
* The keys() Method: Useful when you don't need to work with all of the values in a dictionary. It pulls all the keys from the dictionary.
* Default Behavior: Looping through keys is the default behavior when looping through a dictionary. Writing `for name in favorite_languages:` 
  produces the exact same output as `for name in favorite_languages.keys():`.

Code Example:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in favorite_languages.keys():
    print(name.title())

Output:
Jen
Sarah
Phil
Edward

* Accessing Values During Key Loops: You can access the value associated with any key inside the loop using the dictionary name and the current key.

Code Example:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("  Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

Output:
Edward
Phil
  Hi Phil, I see your favorite language is Python!
Sarah
  Hi Sarah, I see your favorite language is C!
Jen

* Checking Key Membership: The keys() method returns a sequence of keys, allowing you to check if a key exists using `not in` or `in`.

Code Example:
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

Output:
Erin, please take our poll!


3. LOOPING THROUGH A DICTIONARY'S KEYS IN ORDER
-----------------------------------------------------------------------------------------------------------------------------------------------------
* Unordered Nature: Dictionaries maintain connections between keys and values, but items are not returned in any predictable order during iteration.
* Sorting Keys with sorted(): Use the sorted() function wrapped around dictionary.keys() to get a copy of the keys in sorted order before looping.

Code Example:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

Output:
Edward, thank you for taking the poll.
Jen, thank you for taking the poll.
Phil, thank you for taking the poll.
Sarah, thank you for taking the poll.


4. LOOPING THROUGH ALL VALUES IN A DICTIONARY
-----------------------------------------------------------------------------------------------------------------------------------------------------
* The values() Method: Returns a list of values without any keys.

Code Example:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

Output:
The following languages have been mentioned:
Python
C
Python
Ruby

* Removing Duplicates with set(): To pull values without repetitions, wrap the set() function around dictionary.values(). A set is a collection 
  where each item must be unique.

Code Example:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

Output:
The following languages have been mentioned:
Python
C
Ruby


5. TRY IT YOURSELF EXERCISES
-----------------------------------------------------------------------------------------------------------------------------------------------------
File naming standard: Use descriptive, lowercase snake_case names (e.g., glossary_2.py).

- 6-4. Glossary 2:
  Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 by replacing your series of print statements with a loop 
  that runs through the dictionary's keys and values. When you're sure that your loop works, add five more Python terms to your glossary. 
  When you run your program again, these new words and meanings should automatically be included in the output.

- 6-5. Rivers:
  Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
  * Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
  * Use a loop to print the name of each river included in the dictionary.
  * Use a loop to print the name of each country included in the dictionary.

- 6-6. Polling:
  Use the code in favorite_languages.py.
  * Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
  * Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. 
    If they have not yet taken the poll, print a message inviting them to take the poll.
