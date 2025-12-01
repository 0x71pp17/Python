import string
import secrets

# Length value can be adjusted below; larger numbers enhance security further
def generate_secure_password(length=17):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

print("Password:", generate_secure_password())   
