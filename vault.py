import json
import os
from cryptography.fernet import Fernet

# 1. Generate or load a secret key (Keep this safe!)
KEY_FILE = "secret.key"


def load_key():
    """Loads the encryption key, or creates one if it doesn't exist."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


# Initialize the cipher tool
encryption_key = load_key()
cipher = Fernet(encryption_key)


def save_encrypted_password(site, password):
    """Encrypts the password before saving it to the vault."""
    # Encrypt the string (must be converted to bytes first)
    encrypted_pwd = cipher.encrypt(password.encode()).decode()

    # Load existing vault
    try:
        with open("secure_vault.json", "r") as file:
            vault = json.load(file)
    except FileNotFoundError:
        vault = {}

    # Save the unreadable, encrypted version
    vault[site] = encrypted_pwd

    with open("secure_vault.json", "w") as file:
        json.dump(vault, file, indent=4)
    print(f"Securely encrypted and saved password for {site}")


# Your impressive execution
save_encrypted_password("github.com", "my_super_secret_password")
print("\nTake a look at secure_vault.json - you won't be able to read the password!")
