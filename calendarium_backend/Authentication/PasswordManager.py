import os
import binascii
import hashlib


def hash_password(input_string: str) -> str:
    """Programmer: Ali Rahbart
    Date: December 21, 2023

    Returns the hash value of the string given to it

    >>> hash_password("1234")
    '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'

    >>> hash_password("Ali")
    '862ef3927a7c8acfd3e79aa547800ef285cd9b13a39f5ec2d47554981cb313c8'
    """
    sha256_hash = hashlib.sha256()

    sha256_hash.update(input_string.encode('utf-8'))
    hashed_string = sha256_hash.hexdigest()

    return str(hashed_string)


def generate_salt(length=16) -> str:
    """Programmer: Ali Rahbar
    Date: December 21, 2023

    Returns a randomly generated salt for the security of the passwords.
    """
    salt = os.urandom(length)

    return binascii.hexlify(salt).decode('utf-8')