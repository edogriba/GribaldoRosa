import bcrypt
import jwt
from datetime import datetime, timedelta

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
            {'user_id': user_id, 'exp': datetime.now(datetime.UTC) + timedelta(hours=24)},
            SECRET_KEY, algorithm="HS256"
        )
        return token
    except jwt.PyJWTError as e:
        # Catch specific JWT encoding errors and propagate
        raise Exception(f"Error generating JWT token: {str(e)}")
    except Exception as e:
        # Catch any other exceptions and propagate
        raise Exception(f"Unexpected error occurred: {str(e)}")