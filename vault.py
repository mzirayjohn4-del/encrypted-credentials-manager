import json

def save_password(site, password):
    # Try to load existing passwords, or create a new dictionary
    try:
        with open("vault.json", "r") as file:
            vault = json.load(file)
    except FileNotFoundError:
        vault = {}
    
    # Add the new password
    vault[site] = password
    
    # Save it back to the file
    with open("vault.json", "w") as file:
        json.dump(vault, file, indent=4)
    print(f"Saved password for {site}")

save_password("github.com", "my_super_secret_password")
