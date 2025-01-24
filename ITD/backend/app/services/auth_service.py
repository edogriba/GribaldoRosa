import re
from app.models.user import User 

    
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
    if isinstance(question, int):
        return True
    if isinstance(question, str):
        return all(char.isdigit() for char in question)
    return False


def is_float_valid(question):
    """
    Check if the provided input is a valid float number.

    :param question: The input to validate.
    :return: True if the input is a float, otherwise False.
    """
    return isinstance(question, float) or isinstance(question, int)


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
    

################################
#    CREDENTIALS VALIDATION    #
################################
def is_email_valid(email: str):
    """
    Check if the provided input is a valid email address.

    :param email: The email address to validate.
    :return: True if the email is valid and not empty, False otherwise.
    """
    try:
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return email and bool(re.match(email_regex, email))
    except Exception as e:
        return False


def is_phoneNumber_valid(phoneNumber):
    """
    Check if the provided input is a valid phone number.

    :param phoneNumber: The phone number to validate.
    :return: True if the phone number is valid and not empty, False otherwise.
    """
    try:
        phone_regex = r'^\+?[1-9]\d{1,14}$'  # E.164 format
        return phoneNumber and bool(re.match(phone_regex, phoneNumber))
    except Exception as e:
        return False


def is_password_valid(password: str):
    """
    A valid password must meet the following criteria:
    - At least 8 characters long
    - Contains at least one digit
    - Contains at least one alphabetic character
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter

    :param password: The password to validate.
    :return: True if the password is valid and not empty, False otherwise.
    """
    try:
        return password and (len(password) >= 8 and 
                any(char.isdigit() for char in password) and 
                any(char.isalpha() for char in password) and 
                any(char.isupper() for char in password) and 
                any(char.islower() for char in password))
    except Exception as e:
        return False


def is_url_valid(url: str):
    """
    Check if the provided input is a valid URL.

    :param url: The URL to validate.
    :return: True if the URL is valid and not empty, False otherwise.
    """
    try:
        url_regex = r'^https?://(?:www\.)?[\w.-]+(?:\.[a-zA-Z]{2,})+$'
        return url and bool(re.match(url_regex, url))
    except Exception as e:
        return False


def is_location_valid(location: str):
    """
    Check if the provided input is a valid location.

    :param location: The location to validate.
    :return: True if the location is valid and not empty, False otherwise.
    """
    try:
        location_regex = r'^[a-zA-Z0-9\s,.-]+$'
        max_length = 255
        return location and bool(re.match(location_regex, location)) and len(location) <= max_length
    except Exception as e:
        return False


def is_description_valid(description: str):
    """
    Check if the provided input is a valid description.

    :param description: The description to validate.
    :return: True if the description is valid and not empty, False otherwise.
    """
    try:
        max_length = 1024
        return description and is_string_valid(description) and len(description) <= max_length
    except Exception as e:
        return False


def is_name_valid(name: str):
    """
    Check if the provided input is a valid name.

    :param name: The name to validate.
    :return: True if the name is valid and not empty, False otherwise.
    """
    try:
        name_regex = r'^[a-zA-Z\s]+$'
        max_length = 100  
        return name and bool(re.match(name_regex, name)) and len(name) <= max_length
    except Exception as e:
        return False


def is_degreeProgram_valid(degreeProgram: str):
    """
    Check if the provided input is a valid degree program.

    :param degreeProgram: The degree program to validate.
    :return: True if the degree program is valid and not empty, False otherwise.
    """
    try:
        regex = r'^[a-zA-Z\s]+$'
        max_length = 255  
        return degreeProgram and bool(re.match(regex, degreeProgram)) and len(degreeProgram) <= max_length
    except Exception as e:
        return False


def is_gpa_valid(gpa: float):
    """
    Check if the provided input is a valid GPA.

    :param gpa: The GPA to validate. It can be None or a float between 0.0 and 4.0.
    :return: True if the GPA is valid or None, False otherwise.
    """
    try:
        return not gpa or is_float_valid(gpa) and 0.0 <= gpa <= 4.0
    except Exception as e:
        return False


def is_graduationYear_valid(graduationYear: int):
    """
    Check if the provided input is a valid graduation year.

    :param graduationYear: The graduation year to validate.
    :return: True if the graduation year is valid or None, False otherwise.
    """
    try:
        return not graduationYear or is_int_valid(graduationYear) and 1900 <= graduationYear <= 2025
    except Exception as e:
        return False
    

def is_path_valid(path: str):
    """
    Check if the provided input is a valid path.

    :param path: The path to validate.
    :return: True if the path is valid and not empty, False otherwise.
    """
    try:
        max_length = 1024
        return path and is_string_valid(path) and len(path) <= max_length
    except Exception as e:
        return False


def is_optional_path_valid(path: str):
    """
    Check if the provided input is a valid optional path.

    :param path: The path to validate.
    :return: True if the path is valid or empty, False otherwise.
    """
    try:
        max_length = 1024
        return not path or is_string_valid(path) and len(path) <= max_length
    except Exception as e:
        return False


def is_skills_valid(skills: str):
    """
    Check if the provided input is a valid skills list.

    :param skills: The skills list to validate.
    :return: True if the skills list is valid and not empty, False otherwise.
    """
    try:
        skills_regex = r'^[a-zA-Z\s,.-]+$'
        max_length = 1024
        return skills and bool(re.match(skills_regex, skills)) and len(skills) <= max_length
    except Exception as e:
        return False


def is_userType_valid(userType: str):
    """
    Check if the provided input is a valid user type.

    :param userType: The user type to validate.
    :return: True if the user type is valid and not empty, False otherwise.
    """
    try:
        return userType and userType in ['student', 'university', 'company']
    except Exception as e:
        return False


def is_languageSpoken_valid(languageSpoken: str):
    """
    Check if the provided input is a valid language spoken.

    :param languageSpoken: The language spoken to validate.
    :return: True if the language spoken is valid and not empty, False otherwise.
    """
    try:
        languages_regex = r'^[a-zA-Z\s,.-]+$'
        max_length = 1024
        return languageSpoken and bool(re.match(languages_regex, languageSpoken)) and len(languageSpoken) <= max_length
    except Exception as e:
        return False


def is_id_valid(id: int):
    """
    Check if the provided input is a valid ID.

    :param id: The ID to validate.
    :return: True if the ID is valid and not empty, False otherwise.
    """
    try:
        return id and is_int_valid(id)
    except Exception as e:
        return False
