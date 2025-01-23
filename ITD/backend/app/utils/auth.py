import bcrypt
import jwt
from jwt.exceptions import PyJWTError
from datetime import datetime, timedelta, timezone

SECRET_KEY = "123456"


def hash_password(password):
    """
    Hashes a plaintext password using bcrypt.

    @param {str} password - The plaintext password to be hashed.

    This function securely hashes the provided password by using bcrypt's
    `hashpw` function with a generated salt. It ensures that sensitive
    information such as passwords are stored in a secure, non-reversible format.
    The resulting hash is returned as a UTF-8 decoded string.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def verify_password(plain_password, hashed_password):
    """
    Verifies a plaintext password against a hashed password using bcrypt.

    @param {str} plain_password - The plaintext password to verify.
    @param {str} hashed_password - The hashed password to compare against.

    This function securely verifies the provided plaintext password by using
    bcrypt's `checkpw` function to compare it with the stored hashed password.
    It returns True if the passwords match, and False otherwise.
    """
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


def generate_token(user_id):
    """
    Generates a JWT (JSON Web Token) for the given user ID.

    @param {int} user_id - The unique identifier of the user.

    This function creates a secure JWT with the user's ID and an expiration
    time of 24 hours. The token is signed using the `SECRET_KEY` and the HS256
    algorithm, ensuring that it can be used for authentication and authorization
    purposes. The generated token is returned as a string.
    """
    try:
        token = jwt.encode(
            {
                'user_id': int(user_id), 
                'exp': datetime.now(timezone.utc) + timedelta(hours=24)
            },
            SECRET_KEY, 
            algorithm="HS256"
        )
        return token
    except PyJWTError as e:
        # Catch specific JWT encoding errors and propagate
        print(f"Error generating JWT token: {str(e)}")              ### Debugging
        raise e
    except Exception as e:
        # Catch any other exceptions and propagate
        print(f"Unexpected error occurred: {str(e)}")               ### Debugging
        raise e

    