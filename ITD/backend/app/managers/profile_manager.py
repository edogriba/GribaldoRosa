from ..models import Student, University, Company
from flask_jwt_extended import get_current_user
from typing import Union
from werkzeug.utils import secure_filename
from ..utils import json_created, json_invalid_request, json_internal_server_error, update_file_user, json_unauthorized
from ..services import *


class ProfileManager:
    def update_student(self, user_data, profilePicture, CV):
        """
        Update the student with the given user data.

        :param user_data: Dictionary containing student data
        :return: JSON response with success message if update is successful, 
                 or an error message if update fails
        """
        try:
            values = {
                'phoneNumber'   : user_data.get('phoneNumber'),
                'profilePicturePath': None if not profilePicture else secure_filename(profilePicture.filename),     # Optional
                'location'      : user_data.get('location'),
                'degreeProgram' : user_data.get('degreeProgram'),
                'gpa'           : None if not user_data.get('GPA') else float(user_data.get('GPA')),                              # Optional
                'graduationYear': None if not user_data.get('graduationYear') else int(user_data.get('graduationYear')),          # Optional
                'CVpath'        : None if not CV else secure_filename(CV.filename),           
                'skills'        : user_data.get('skills'),
                'languageSpoken': user_data.get('languageSpoken'),
                'universityId'  : int(user_data.get('universityId'))
            }

            if get_current_user().get_type() != "student":
                return json_unauthorized("Unauthorized access")
            
            values.update({'id': get_current_user().get_id()})
            
            validation_result = validate_student_data(values)
            if validation_result is not True:
                return validation_result
                        
            student = Student.update(values['id'], values['phoneNumber'], values['profilePicturePath'], values['location'], 
                                     values['degreeProgram'], values['gpa'], values['graduationYear'], values['CVpath'], 
                                     values['skills'], values['languageSpoken'], values['universityId'])

            if not student:
                return json_internal_server_error("Update failed")

            if profilePicture:
                update_file_user(values['id'], get_current_user().get_profilePicture(), profilePicture)

            if CV:
                update_file_user(values['id'], get_current_user().get_cv(), CV)

            return json_created( "Update successful", user = student.to_dict() )
        
        except Exception as e:
            raise e


    def update_university(self, user_data, logo):
        """
        Update the university with the given user data.

        :param user_data: Dictionary containing university data
        :return: JSON response with success message if update is successful, 
                 or an error message if update fails
        """
        try:
            values = {
                'websiteURL'    : user_data.get('websiteURL'),
                'description'   : user_data.get('description'),
                'logoPath'      : None if not logo else secure_filename(logo.filename)           # Optional
            }

            if get_current_user().get_type() != "university":
                return json_invalid_request("Unauthorized access")
            
            values.update({'id': get_current_user().get_id()})
            
            validation_result = validate_university_data(values)
            if validation_result is not True:
                return validation_result
            
            university = University.update(**values)

            if not university:
                return json_internal_server_error("Update failed")
            
            if logo:
                update_file_user(values['id'], get_current_user().get_logoPath(), logo)

            return json_created( "Update successful", user = university.to_dict() )

        except Exception as e:
            raise e
        
    
    def update_company(self, user_data, logo):
        """
        Update the company with the given user data.

        :param user_data: Dictionary containing company data
        :return: JSON response with success message if update is successful, 
                 or an error message if update fails
        """
        try:
            values = {
                'description'   : user_data.get('description'),
                'location'      : user_data.get('location'),
                'logoPath'      : None if not logo else secure_filename(logo.filename)           # Optional
            }

            if get_current_user().get_type() != "company":
                return json_invalid_request("Unauthorized access")
            
            values.update({'id': get_current_user().get_id()})
            
            validation_result = validate_company_data(values)
            if validation_result is not True:
                return validation_result
            
            company = Company.update(**values)

            if not company:
                return json_internal_server_error("Update failed")
            
            if logo:
                update_file_user(values['id'], get_current_user().get_logoPath(), logo)

            return json_created( "Update successful", user = company.to_dict() )

        except Exception as e:
            raise e
    

def validate_student_data(user_data) -> Union[tuple, bool]:
    """
    Validate the student data.

    :param user_data: Dictionary containing student data
    :return: True if the student data is valid, otherwise JSON response with error message
    """
    try:
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

        if not is_optional_path_valid(user_data["CVpath"]):
            return json_invalid_request("Invalid CV path")

        if not is_skills_valid(user_data["skills"]):
            return json_invalid_request("Invalid skills")

        if not is_languageSpoken_valid(user_data["languageSpoken"]):
            return json_invalid_request("Invalid language spoken")

        if not is_id_valid(user_data["universityId"]):
            return json_invalid_request("Invalid university")

        return True
    except Exception as e:
        return json_invalid_request("Invalid data")
    
    
def validate_university_data(user_data) -> Union[tuple, bool]:
    """
    Validate the university data.

    :param user_data: Dictionary containing university data
    :return: True if the university data is valid, otherwise JSON response with error message
    """
    try:        
        if not is_url_valid(user_data["websiteURL"]):
            return json_invalid_request("Invalid website URL")
        
        if not is_description_valid(user_data["description"]):
            return json_invalid_request("Invalid description")
        
        if not is_optional_path_valid(user_data["logoPath"]):
            return json_invalid_request("Invalid logo path")

        return True
    except Exception as e:
        return json_invalid_request("Invalid data")


def validate_company_data(user_data) -> Union[tuple, bool]:
    """
    Validate the company data.

    :param user_data: Dictionary containing company data
    :return: True if the company data is valid, otherwise JSON response with error message
    """
    try:       
        if not is_location_valid(user_data["location"]):
            return json_invalid_request("Invalid location")
        
        if not is_description_valid(user_data["description"]):
            return json_invalid_request("Invalid description")
        
        if not is_optional_path_valid(user_data["logoPath"]):
            return json_invalid_request("Invalid logo path")
        
        return True
    except Exception as e:
        return json_invalid_request("Invalid data")
