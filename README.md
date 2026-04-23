# 🔒 Encrypted Credentials Manager

A simple, secure, and locally-hosted password manager built with Python. 

Instead of storing passwords in plain text, this script uses the `cryptography` library (Fernet symmetric encryption) to encrypt your credentials before saving them to a local JSON file.

## ✨ Features
* **Secure Storage:** Passwords are encrypted before they are written to the disk.
* **Auto-Key Generation:** Automatically creates a `secret.key` file to manage encryption.
* **Lightweight:** Uses simple JSON for easy data management.

## 🛠️ Prerequisites
Make sure you have Python installed, then install the required encryption library:
```bash
pip install cryptography
```
