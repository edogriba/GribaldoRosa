from flask_jwt_extended import create_access_token, get_current_user
from typing import Union

from ..models import Student, University, Company
from ..utils import hash_password, json_created, json_invalid_request, json_internal_server_error, save_file, get_upload_folder_user, update_file_user
from werkzeug.utils import secure_filename
from ..services.auth_service import *

class RegistrationManager:

    def register_student(self, user_data, profilePicture, CV):
        """
        Register a new student with the given user data.

        :param user_data: Dictionary containing student data
        :return: JSON response with success message if registration is successful, 
                 or an error message if registration fails
        """
        try:
            values = {
                'email'         : user_data.get('email'),
                'password'      : user_data.get('password'),
                'firstName'     : user_data.get('firstName'),
                'lastName'      : user_data.get('lastName'),
                'phoneNumber'   : user_data.get('phoneNumber'),
                'profilePicturePath': None,    # Optional
                'location'      : user_data.get('location'),
                'degreeProgram' : user_data.get('degreeProgram'),
                'gpa'           : user_data.get('GPA', None),                       # Optional
                'graduationYear': user_data.get('graduationYear', None),            # Optional
                'CVpath'        : None,
                'skills'        : user_data.get('skills'),
                'languageSpoken': user_data.get('languageSpoken'),
                'universityId'  : int(user_data.get('university'))
            }
            values.update({'gpa': float(values['gpa'])}) if values['gpa'] else None
            values.update({'graduationYear': int(values['graduationYear'])}) if values['graduationYear'] else None
            values.update({'profilePicturePath': secure_filename(profilePicture.filename)}) if profilePicture else None
            values.update({'CVpath': secure_filename(CV.filename)}) if CV else None

            validation_result = validate_student_data(values, True)
            if validation_result is not True:
                return validation_result
            
            values.update({'password': hash_password(values['password'])})

            student = Student.add(**values)

            save_file(profilePicture, get_upload_folder_user(student.get_id())) if profilePicture else None
            save_file(CV, get_upload_folder_user(student.get_id())) if CV else None

            access_token = create_access_token(identity={ "id": student.get_id() })

            return json_created( "Registration successful", user = student.to_dict(), access_token = access_token )
        
        except Exception as e:
            return e


    def register_university(self, user_data, logo):
        """
        Register a new university with the given user data.

        :param user_data: Dictionary containing university data
        :return: JSON response with success message if registration is successful, 
                 or an error message if registration fails
        """
        try:
            values = {
                'email'         : user_data.get('university_email'),
                'password'      : user_data.get('university_password'),
                'name'          : user_data.get('name'),
                'address'       : user_data.get('location'),
                'websiteURL'    : user_data.get('websiteURL'),
                'description'   : user_data.get('description'),
                'logoPath'      : None  # Optional field
            }

            values.update({'logoPath': secure_filename(logo.filename)}) if logo else None
            
            validation_result = validate_university_data(values, True)
            if validation_result is not True:
                return validation_result
            
            values.update({'password': hash_password(values['password'])})
            
            university = University.add(**values)

            save_file(logo, get_upload_folder_user(university.get_id())) if logo else None

            access_token = create_access_token(identity={ "id": university.get_id() })

            return json_created( "Registration successful", user = university.to_dict(), access_token = access_token )

        except Exception as e:
            return e


    def register_company(self, user_data, logo):
        """
        Register a new company with the given user data.

        :param user_data: Dictionary containing company data
        :return: JSON response with success message if registration is successful, 
                 or an error message if registration fails
        """
        try:
            values = {
                'email'         : user_data.get('email'),
                'password'      : user_data.get('password'),
                'companyName'   : user_data.get('companyName'),
                'logoPath'      : None,  # Optional field
                'description'   : user_data.get('description'),
                'location'      : user_data.get('location'),
            }

            values.update({'logoPath': secure_filename(logo.filename)}) if logo else None
            print(values['logoPath'])
            validation_result = validate_company_data(values, True)
            if validation_result is not True:
                return validation_result
            
            values.update({'password': hash_password(values['password'])})

            company = Company.add(**values)

            save_file(logo, get_upload_folder_user(company.get_id())) if logo else None

            access_token = create_access_token(identity={ "id": company.get_id() })

            return json_created( "Registration successful", user = company.to_dict(), access_token = access_token )

        except Exception as e:
            return e


    def update_student(self, user_data, profilePicture, CV):
        """
        Update the student with the given user data.

        :param user_data: Dictionary containing student data
        :return: JSON response with success message if update is successful, 
                 or an error message if update fails
        """
        try:
            values = {
                'id'            : int(user_data.get('id')),
                'phoneNumber'   : user_data.get('phoneNumber'),
                'profilePicturePath': user_data.get('profilePicturePath', None),            # Optional
                'location'      : user_data.get('location'),
                'degreeProgram' : user_data.get('degreeProgram'),
                'gpa'           : float(user_data.get('GPA', None)),                               # Optional
                'graduationYear': int(user_data.get('graduationYear', None)),                    # Optional
                'CVpath'        : user_data.get('CVpath'),
                'skills'        : user_data.get('skills'),
                'languageSpoken': user_data.get('languageSpoken'),
                'universityId'  : int(user_data.get('university'))
            }

            if values['id'] != get_current_user().get_id() or get_current_user().get_type() != "student":
                return json_invalid_request("Unauthorized access")
            
            validation_result = validate_student_data(values, False)
            if validation_result is not True:
                return validation_result
            
            if profilePicture:
                update_file_user(values['id'], values['profilePicturePath'], profilePicture)
                values.update({'profilePicturePath': secure_filename(profilePicture.filename)})

            if CV:
                update_file_user(values['id'], values['CVpath'], CV)
                values.update({'CVpath': secure_filename(CV.filename)})
                        
            student = Student.update(**values)

            if not student:
                return json_internal_server_error("Update failed")

            return json_created( "Update successful", user = student.to_dict() )
        
        except Exception as e:
            return e


    def update_university(self, user_data, logo):
        """
        Update the university with the given user data.

        :param user_data: Dictionary containing university data
        :return: JSON response with success message if update is successful, 
                 or an error message if update fails
        """
        try:
            values = {
                'id'            : int(user_data.get('id')),
                'address'       : user_data.get('location'),
                'websiteURL'    : user_data.get('websiteURL'),
                'description'   : user_data.get('description'),
                'logoPath'      : user_data.get('logoPath', None)             # Optional field
            }

            if values['id'] != get_current_user().get_id() or get_current_user().get_type() != "university":
                return json_invalid_request("Unauthorized access")
            
            validation_result = validate_university_data(values, False)
            if validation_result is not True:
                return validation_result
            
            if logo:
                update_file_user(values['id'], values['logoPath'], logo)
                values.update({'logoPath': secure_filename(logo.filename)})
            
            university = University.update(**values)

            if not university:
                return json_internal_server_error("Update failed")

            return json_created( "Update successful", user = university.to_dict() )

        except Exception as e:
            return e
        
    
    def update_company(self, user_data, logo):
        """
        Update the company with the given user data.

        :param user_data: Dictionary containing company data
        :return: JSON response with success message if update is successful, 
                 or an error message if update fails
        """
        try:
            values = {
                'id'            : int(user_data.get('id')),
                'logoPath'      : user_data.get('logoPath', None),  # Optional field
                'description'   : user_data.get('description'),
                'location'      : user_data.get('location'),
            }

            if values['id'] != get_current_user().get_id() or get_current_user().get_type() != "company":
                return json_invalid_request("Unauthorized access")
            
            validation_result = validate_company_data(values, False)
            if validation_result is not True:
                return validation_result
            
            if logo:
                update_file_user(values['id'], values['logoPath'], logo)
                values.update({'logoPath': secure_filename(logo.filename)})
            
            company = Company.update(**values)

            if not company:
                return json_internal_server_error("Update failed")

            return json_created( "Update successful", user = company.to_dict() )

        except Exception as e:
            return e
    

def validate_student_data(user_data, flag) -> Union[tuple, bool]:
    """
    Validate the student data.

    :param user_data: Dictionary containing student data
    :return: True if the student data is valid, otherwise JSON response with error message
    """
    try:
        if flag and not is_email_valid(user_data["email"]):
            return json_invalid_request("Invalid email")
        
        if flag and not is_email_unique(user_data["email"]):
            return json_invalid_request("Email not unique")

        if flag and not is_password_valid(user_data["password"]):
            return json_invalid_request("Invalid password")

        if flag and not is_name_valid(user_data["firstName"]):
            return json_invalid_request("Invalid first name")

        if flag and not is_name_valid(user_data["lastName"]):
            return json_invalid_request("Invalid last name")

        if not is_phoneNumber_valid(user_data["phoneNumber"]):
            return json_invalid_request("Invalid phone number")

        if not is_optional_path_valid(user_data["profilePicturePath"]):
            return json_invalid_request("Invalid profile picture path")

        if not is_location_valid(user_data["location"]):
            return json_invalid_request("Invalid location")

        if not is_degreeProgram_valid(user_data["degreeProgram"]):
            return json_invalid_request("Invalid degree program")

        if not is_gpa_valid(user_data["gpa"]):
            return json_invalid_request("Invalid GPA")

        if not is_graduationYear_valid(user_data["graduationYear"]):
            return json_invalid_request("Invalid graduation year")

        if not is_path_valid(user_data["CVpath"]):
            return json_invalid_request("Invalid CV path")

        if not is_skills_valid(user_data["skills"]):
            return json_invalid_request("Invalid skills")

        if not is_languageSpoken_valid(user_data["languageSpoken"]):
            return json_invalid_request("Invalid language spoken")

        if not is_id_valid(user_data["universityId"]):
            return json_invalid_request("Invalid university")

        return True
    except Exception as e:
        print(f"Error: {e}")
        return json_invalid_request("Invalid data")
    
    
def validate_university_data(user_data, flag) -> Union[tuple, bool]:
    """
    Validate the university data.

    :param user_data: Dictionary containing university data
    :return: True if the university data is valid, otherwise JSON response with error message
    """
    try:
        if flag and not is_email_valid(user_data["email"]):
            return json_invalid_request("Invalid email")
        
        if flag and not is_email_unique(user_data["email"]):
            return json_invalid_request("Email not unique")
        
        if flag and not is_password_valid(user_data["password"]):
            return json_invalid_request("Invalid password")
        
        if flag and not is_name_valid(user_data["name"]):
            return json_invalid_request("Invalid name")
        
        if not is_location_valid(user_data["address"]):
            return json_invalid_request("Invalid address")
        
        if not is_url_valid(user_data["websiteURL"]):
            return json_invalid_request("Invalid website URL")
        
        if not is_description_valid(user_data["description"]):
            return json_invalid_request("Invalid description")
        
        if not is_optional_path_valid(user_data["logoPath"]):
            return json_invalid_request("Invalid logo path")
        
        return True
    except Exception as e:
        print(f"Exception in validate_university_data: {e}")
        return json_invalid_request("Invalid data")


def validate_company_data(user_data, flag) -> Union[tuple, bool]:
    """
    Validate the company data.

    :param user_data: Dictionary containing company data
    :return: True if the company data is valid, otherwise JSON response with error message
    """
    try:
        if flag and not is_email_valid(user_data["email"]):
            return json_invalid_request("Invalid email")
        
        if flag and not is_email_unique(user_data["email"]):
            return json_invalid_request("Email not unique")
        
        if flag and not is_password_valid(user_data["password"]):
            return json_invalid_request("Invalid password")
        
        if flag and not is_name_valid(user_data["companyName"]):
            return json_invalid_request("Invalid company name")
        
        if not is_location_valid(user_data["location"]):
            return json_invalid_request("Invalid location")
        
        if not is_description_valid(user_data["description"]):
            return json_invalid_request("Invalid description")
        
        if not is_optional_path_valid(user_data["logoPath"]):
            return json_invalid_request("Invalid logo path")
        
        return True
    except Exception as e:
        print(f"Exception in validate_company_data: {e}")
        return json_invalid_request("Invalid data")
