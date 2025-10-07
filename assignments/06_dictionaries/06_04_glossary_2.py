# 6-4, Glossary 2, 142


glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'variable': 'A name that stores a value.',
    'loop': 'A structure that repeats a block of code multiple times.',
    'string': 'A series of characters enclosed in quotes.',
    'function': 'A named block of code designed to do a specific job.',
    }

for word, meaning in glossary.items():
    print(f"\n{word.title()}: {meaning}\n")
