#!/usr/bin/env python3
"""encryption module"""
import bcrypt


def hash_password(password):
    """hashing password"""
    salt = bcrypt.gensalt()

    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def is_valid(hashed_password, password):
    """Use bcrypt to validate the password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)


if __name__ == "__main__":
    password = "MyAmazingPassw0rd"
    encrypted_password = hash_password(password)
    print(encrypted_password.decode('utf-8'))
    print(is_valid(encrypted_password, password))
