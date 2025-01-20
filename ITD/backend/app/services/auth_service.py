from app.models.user import User
import re

    
def is_string_valid(question):
    """
    Check if the provided input is a valid string.

    :param question: The input to validate.
    :return: True if the input is a string, otherwise False.
    """
    return isinstance(question, str)


def is_int_valid(question):
    """
    Check if the provided input is a valid integer number.

    :param question: The input to validate.
    :return: True if the input is an integer, otherwise False.
    """
    return isinstance(question, int)


def is_float_valid(question):
    """
    Check if the provided input is a valid float number.

    :param question: The input to validate.
    :return: True if the input is a float, otherwise False.
    """
    return isinstance(question, float)


def is_phoneNumber_valid(phoneNumber):
    """
    Check if the provided input is a valid phone number.

    :param phoneNumber: The phone number to validate.
    :return: True if the phone number is valid, False otherwise.
    """
    phone_regex = r'^\+?[1-9]\d{1,14}$'  # E.164 format     <- IS CORRECT?
    return bool(re.match(phone_regex, phoneNumber))


def is_email_valid(email: str):
    """
    Check if the provided input is a valid email address.

    :param email: The email address to validate.
    :return: True if the email is valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_regex, email))


def is_email_unique(email: str):
    """
    Check if the provided email is unique.

    :param email: The email address to check.
    :return: True if the email is unique, otherwise False.
    :raises Exception: If an error occurs during the database query execution.
    """
    try:
        return User.is_email_unique(email)
    except Exception as e:
        raise e
    