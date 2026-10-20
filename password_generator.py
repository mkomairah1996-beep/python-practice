import secrets
import string
def generate_password(length):
    characters=string.ascii_letters+string.digits
    return ''.join(secrets.choice(characters)for _ in range (length))
length =int(input("enter password length:"))
password= generate_password(length)
print(password)