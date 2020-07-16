import random
import string

def password_generator():
    password_length = random.randint(8, 16) # Generates the password length 
    characters = string.ascii_letters + string.digits + string.punctuation # Characters the password generator can use
    # Generates a random character for the range of password_length
    password_list = [random.choice(characters) for i in range(password_length)]
    password = ''.join(password_list) # Makes the list into a single string
    return password # Returns the single string
