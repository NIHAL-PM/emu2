#!/usr/bin/env python3
"""
Generate an encryption key for the application
"""
from cryptography.fernet import Fernet

if __name__ == "__main__":
    key = Fernet.generate_key()
    print("Generated encryption key:")
    print(key.decode())
    print("\nAdd this to your environment variables as ENCRYPTION_KEY")
