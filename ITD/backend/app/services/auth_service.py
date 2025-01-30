import re
from ..models import User 

    
def is_string_valid(question) -> bool:
    """
    Check if the provided input is a valid string.

    :param question: The input to validate.
    :return: True if the input is a string, otherwise False.
    """
    return isinstance(question, str)


def is_int_valid(question) -> bool:
    """
    Check if the provided input is a valid integer number.

    :param question: The input to validate.
    :return: True if the input is an integer, otherwise False.
    """
    if isinstance(question, int):
        return True
    return False


def is_float_valid(question) -> bool:
    """
    Check if the provided input is a valid float number.

    :param question: The input to validate.
    :return: True if the input is a float, otherwise False.
    """
    return isinstance(question, float)


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
def is_email_valid(email: str) -> bool:
    """
    Check if the provided input is a valid email address.

    :param email: The email address to validate.
    :return: True if the email is valid and not empty, False otherwise.
    """
    try:
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(email_regex, email))
    except Exception as e:
        return False


def is_phoneNumber_valid(phoneNumber) -> bool:
    """
    Check if the provided input is a valid phone number.

    :param phoneNumber: The phone number to validate.
    :return: True if the phone number is valid and not empty, False otherwise.
    """
    try:
        phone_regex = r'^\+?[1-9]\d{1,14}$|^\d{3}[-.\s]?\d{3}[-.\s]?\d{4}$'
        if len(phoneNumber) < 10:
            return False
        return bool(re.match(phone_regex, phoneNumber))
    except Exception:
        return False


def is_password_valid(password: str) -> bool:
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
        return (len(password) >= 8 and 
                any(char.isdigit() for char in password) and 
                any(char.isalpha() for char in password) and 
                any(char.isupper() for char in password) and 
                any(char.islower() for char in password))
    except Exception as e:
        return False


def is_url_valid(url: str) -> bool:
    """
    Check if the provided input is a valid URL.

    :param url: The URL to validate.
    :return: True if the URL is valid and not empty, False otherwise.
    """
    try:
        url_regex = r'^https?://(?:www\.)?[\w.-]+(?:\.[a-zA-Z]{2,})?(?:/[\w./-]*)?$'
        return bool(re.match(url_regex, url))
    except Exception as e:
        return False


def is_location_valid(location: str) -> bool:
    """
    Check if the provided input is a valid location.

    :param location: The location to validate.
    :return: True if the location is valid and not empty, False otherwise.
    """
    try:
        location_regex = r'^[a-zA-Z0-9\s,.-]+$'
        max_length = 255
        return bool(re.match(location_regex, location)) and len(location) <= max_length
    except Exception as e:
        return False


def is_description_valid(description: str) -> bool:
    """
    Check if the provided input is a valid description.

    :param description: The description to validate.
    :return: True if the description is valid and not empty, False otherwise.
    """
    try:
        max_length = 2048
        return description and is_string_valid(description) and len(description) <= max_length
    except Exception as e:
        return False


def is_name_valid(name: str) -> bool:
    """
    Check if the provided input is a valid name.

    :param name: The name to validate.
    :return: True if the name is valid and not empty, False otherwise.
    """
    try:
        name_regex = r'^[a-zA-Z\s]+$'
        max_length = 100  
        return bool(re.match(name_regex, name)) and len(name) <= max_length
    except Exception as e:
        return False


def is_degreeProgram_valid(degreeProgram: str) -> bool:
    """
    Check if the provided input is a valid degree program.

    :param degreeProgram: The degree program to validate.
    :return: True if the degree program is valid and not empty, False otherwise.
    """
    try:
        regex = r'^[a-zA-Z\s]+$'
        max_length = 255  
        return bool(re.match(regex, degreeProgram)) and len(degreeProgram) <= max_length
    except Exception as e:
        return False


def is_gpa_valid(gpa) -> bool:
    """
    Check if the provided input is a valid GPA.

    :param gpa: The GPA to validate. It can be None or a float between 0.0 and 4.0.
    :return: True if the GPA is valid or None, False otherwise.
    """
    try:
        if gpa == "":
            return False
        return gpa is None or (is_float_valid(gpa) and 0.0 <= gpa <= 4.0)
    except Exception:
        return False


def is_graduationYear_valid(graduationYear: int) -> bool:
    """
    Check if the provided input is a valid graduation year.

    :param graduationYear: The graduation year to validate.
    :return: True if the graduation year is valid or None, False otherwise.
    """
    try:
        if graduationYear == "":
            return False
        return not graduationYear or is_int_valid(graduationYear) and 1900 <= graduationYear <= 2025
    except Exception as e:
        return False
    

def is_path_valid(path: str) -> bool:
    """
    Check if the provided input is a valid path.

    :param path: The path to validate.
    :return: True if the path is valid and not empty, False otherwise.
    """
    try:
        max_length = 1024
        if not path or not isinstance(path, str) or len(path) > max_length:
            return False
        return path.startswith("/") and not any(char in path for char in [" ", "\\", ":", "*", "?", "\"", "<", ">", "|"])
    except Exception:
        return False


def is_optional_path_valid(path: str) -> bool:
    """
    Check if the provided input is a valid optional path.

    :param path: The path to validate.
    :return: True if the path is valid or empty, False otherwise.
    """
    try:
        max_length = 1024
        if not path:
            return True
        if not isinstance(path, str) or len(path) > max_length:
            return False
        return path.startswith("/") and not any(char in path for char in [" ", "\\", ":", "*", "?", "\"", "<", ">", "|"])
    except Exception:
        return False


def is_skills_valid(skills: str) -> bool:
    """
    Check if the provided input is a valid skills list.

    :param skills: The skills list to validate.
    :return: True if the skills list is valid and not empty, False otherwise.
    """
    try:
        skills_regex = r'^([\w\+\#\.]+)(,\s*[\w\+\#\.]+)*$'
        max_length = 1024
        return bool(skills and re.match(skills_regex, skills) and len(skills) <= max_length)
    except Exception:
        return False


def is_userType_valid(userType: str) -> bool:
    """
    Check if the provided input is a valid user type.

    :param userType: The user type to validate.
    :return: True if the user type is valid and not empty, False otherwise.
    """
    try:
        return userType in ['student', 'university', 'company']
    except Exception:
        return False


def is_languageSpoken_valid(languageSpoken: str) -> bool:
    """
    Check if the provided input is a valid language spoken.

    :param languageSpoken: The language spoken to validate.
    :return: True if the language spoken is valid and not empty, False otherwise.
    """
    try:
        languages_regex = r'^[a-zA-Z\s,.-]+$'
        max_length = 1024
        return bool(re.match(languages_regex, languageSpoken)) and len(languageSpoken) <= max_length
    except Exception:
        return False


def is_id_valid(id: int) -> bool:
    """
    Check if the provided input is a valid ID.

    :param id: The ID to validate.
    :return: True if the ID is valid and not empty, False otherwise.
    """
    try:
        if id < 0:
            return False
        return is_int_valid(id)
    except Exception:
        return False


def is_duration_valid(duration: int) -> bool:
    """
    Check if the provided input is a valid duration.

    :param duration: The duration to validate.
    :return: True if the duration is valid and not empty, False otherwise.
    """
    try:
        return is_int_valid(duration) and 0 < duration <= 12
    except Exception:
        return False
    

def is_compensation_valid(compensation: int) -> bool:
    """
    Check if the provided input is a valid compensation.

    :param compensation: The compensation to validate.
    :return: True if the compensation is valid or empty, False otherwise.
    """
    try:
        if compensation == "":
            return False
        return not compensation or is_int_valid(compensation) and 0 <= compensation
    except Exception:
        return False
    

def is_benefits_valid(benefits: str) -> bool:
    """
    Check if the provided input is a valid benefits list.

    :param benefits: The benefits list to validate.
    :return: True if the benefits list is valid or empty, False otherwise.
    """
    try:
        max_length = 1024
        if benefits == "":
            return False
        if not benefits:
            return True
        return is_string_valid(benefits) and 1 < len(benefits.strip()) <= max_length
    except Exception:
        return False
    