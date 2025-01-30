import bcrypt
from typing import Union

def hash_password(password) -> Union[str, Exception]:
    """
    Hashes a plaintext password using bcrypt.

    @param {str} password - The plaintext password to be hashed.

    This function securely hashes the provided password by using bcrypt's
    `hashpw` function with a generated salt. It ensures that sensitive
    information such as passwords are stored in a secure, non-reversible format.
    The resulting hash is returned as a UTF-8 decoded string.
    """
    try:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    except Exception as e:
        raise e


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plaintext password against a hashed password using bcrypt.

    @param {str} plain_password - The plaintext password to verify.
    @param {str} hashed_password - The hashed password to compare against.

    This function securely verifies the provided plaintext password by using
    bcrypt's `checkpw` function to compare it with the stored hashed password.
    It returns True if the passwords match, and False otherwise.
    """
    try:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    except Exception as e:
        return False
