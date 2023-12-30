"""
Programmer: Ali Rahbar
Date: December 30, 2023
Description: This file is incharge of encrypting certain data before writing it to the database
"""
from cryptography.fernet import Fernet

# Use the get_key function to get the key
key = b'fYeiB-VeHvaLr5PaEGrAclEISzNC29cMCz_1rK_dTE8='  # ToDo: Read From Environmental Variable
cipher_suite = Fernet(key)


def encrypt_string(message):
    """Programmer: Ali Rahbar
    Date: December 30, 2023

    Encrypts the Strings given to the function
    """

    encrypted_message = cipher_suite.encrypt(message.encode())

    return encrypted_message


def decrypt_string(encrypted_message):
    """Programmer: Ali Rahbar
    Date: December 30, 2023

    Returns the Decrypted Strings given to the function
    >>> decrypt_string(b'gAAAAABlj7gUZrKQPA5Qoo-akmigUt-r3qsUr7vTYKZrWMqPbQqI5BdS8HstVi1wQ66O1bJAoiZWzs6FoXozW7OyKNzdznEypA==')
    'Hello'
    >>> decrypt_string(b'gAAAAABlj7hkAf9veZA84jYtj2QRz9KFkY4RPUh4oOfxjJaDiJJ917qiWk-N_xEYvUPDKq9azvs6O8kaKPMCiutoDXjow8LOQg==')
    'Hello'
    """

    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()

    return decrypted_message
