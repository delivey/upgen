import random
import json

def name_generator():
    names = json.loads(open('names.json').read()) # Loads names.json
    name = random.choice(names).lower() # Select a random value from the list, makes it lowercase

    name_extra = str(random.randint(1, 999)) # Generates a random number between 1 and 999
    username = name + name_extra # Concatenates the random name and the random number
    return username # Returns the concatenated string
