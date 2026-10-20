import secrets
import string
def generate_password(length):
    characters=string.ascii_letters+string.digits
    return ''.join(secrets.choice(characters)for _ in range (length))
password= generate_password(12)
print(password)