import random
import hashlib

def generate_password(length=10):
    """
    Generate a strong password of given length consisting of alphanumeric characters.

    Args:
        length (int): Length of the password. Default is 10.

    Returns:
        str: A strong password.
    """
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def encrypt_password(password):
    """
    Encrypt the given password using MD5 hashing.

    Args:
        password (str): The password to encrypt.

    Returns:
        str: Encrypted password (MD5 hash).
    """
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    return md5_hash

# Generate a strong password
password = generate_password()

# Encrypt the password using MD5 hashing
encrypted_password = encrypt_password(password)

print(f"Your Password is : {encrypted_password}")

