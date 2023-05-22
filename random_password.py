import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits 
    password_characters = random.choices(characters, k=length)
    password = ''.join(password_characters)
    return password
password = generate_password(10)
print(password)