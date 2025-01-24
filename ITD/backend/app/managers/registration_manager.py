from flask import jsonify

from app.models.user import User
from app.models.student import Student
from app.models.university import University
from app.models.company import Company
from app.services.auth_service import *
from app.utils.auth import hash_password

class RegistrationManager:

    def register_student(self, user_data):
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
                'profilePicturePath': user_data.get('profilePicturePath', ''),  # Optional
                'location'      : user_data.get('location'),
                'degreeProgram' : user_data.get('degreeProgram'),
                'gpa'           : user_data.get('GPA', None),                   # Optional
                'graduationYear': user_data.get('graduationYear', None),        # Optional
                'CVpath'        : user_data.get('CVpath'),
                'skills'        : user_data.get('skills'),
                'languageSpoken': user_data.get('languageSpoken'),
                'universityId'  : user_data.get('university')
            }

            res = self.validate_student_data(values)
            if not res:
                return jsonify({
                    "type": "invalid_request",
                    "message": "Invalid data"
                }), 400
            
            values.update({'password': hash_password(values['password'])})

            student = Student.add(**values)

            # Return success response
            return jsonify({
                'message': 'Registration successful',
                'user': student.to_dict()
            }), 201
        
        except Exception as e:
            return e


    def register_university(self, user_data):
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
                'logoPath'      : user_data.get('logoPath', '')  # Optional field
            }
            
            if not self.validate_university_data(values):
                return jsonify({
                    "type": "invalid_request",
                    "message": "Invalid data"
                }), 400
            
            values.update({'password': hash_password(values['password'])})
            
            university = University.add(**values)

            # Return success response
            return jsonify({
                'message': 'Registration successful',
                'user': university.to_dict()
            }), 201
        except Exception as e:
            return e


    def register_company(self, user_data):
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
                'logoPath'      : user_data.get('logoPath', ''),  # Optional
                'description'   : user_data.get('description'),
                'location'      : user_data.get('location'),
            }

            if not self.validate_company_data(values):
                return jsonify({
                    "type": "invalid_request",
                    "message": "Invalid data"
                }), 400
            
            values.update({'password': hash_password(values['password'])})

            company = Company.add(**values)

            # Return success response
            return jsonify({
                'message': 'Registration successful',
                'user': company.to_dict()
            }), 201
        except Exception as e:
            return e


    def validate_student_data(self, user_data):
        """
        Validate the student data.

        :param user_data: Dictionary containing student data
        :return: True if the student data is valid, otherwise False
        """
        try:
            if not is_email_valid(user_data["email"]):
                print("Invalid email")
                return False
            if not is_email_unique(user_data["email"]):
                print("Email not unique")
                return False
            if not is_password_valid(user_data["password"]):
                print("Invalid password")
                return False
            if not is_name_valid(user_data["firstName"]):
                print("Invalid first name")
                return False
            if not is_name_valid(user_data["lastName"]):
                print("Invalid last name")
                return False
            if not is_phoneNumber_valid(user_data["phoneNumber"]):
                print("Invalid phone number")
                return False
            if not is_optional_path_valid(user_data["profilePicturePath"]):
                print("Invalid profile picture path")
                return False
            if not is_location_valid(user_data["location"]):
                print("Invalid location")
                return False
            if not is_degreeProgram_valid(user_data["degreeProgram"]):
                print("Invalid degree program")
                return False
            if not is_gpa_valid(user_data["gpa"]):
                print("Invalid GPA")
                return False
            if not is_graduationYear_valid(user_data["graduationYear"]):
                print("Invalid graduation year")
                return False
            if not is_path_valid(user_data["CVpath"]):
                print("Invalid CV path")
                return False
            if not is_skills_valid(user_data["skills"]):
                print("Invalid skills")
                return False
            if not is_languageSpoken_valid(user_data["languageSpoken"]):
                print("Invalid language spoken")
                return False
            if not is_id_valid(user_data["universityId"]):
                print("Invalid university ID")
                return False
            return True
        except Exception as e:
            print(f"Exception in validate_student_data: {e}")
            return False
        

    def validate_university_data(self, user_data):
        """
        Validate the university data.

        :param user_data: Dictionary containing university data
        :return: True if the university data is valid, otherwise False
        """
        try:
            if not is_email_valid(user_data["email"]):
                print("Invalid email")
                return False
            if not is_email_unique(user_data["email"]):
                print("Email not unique")
                return False
            if not is_password_valid(user_data["password"]):
                print("Invalid password")
                return False
            if not is_name_valid(user_data["name"]):
                print("Invalid name")
                return False
            if not is_location_valid(user_data["address"]):
                print("Invalid address")
                return False
            if not is_url_valid(user_data["websiteURL"]):
                print("Invalid website URL")
                return False
            if not is_description_valid(user_data["description"]):
                print("Invalid description")
                return False
            if not is_optional_path_valid(user_data["logoPath"]):
                print("Invalid logo path")
                return False
            return True
        except Exception as e:
            print(f"Exception in validate_student_data: {e}")
            return e


    def validate_company_data(self, user_data):
        """
        Validate the company data.

        :param user_data: Dictionary containing company data
        :return: True if the company data is valid, otherwise False
        """
        try:
            if not is_email_valid(user_data["email"]):
                print("Invalid email")
                return False
            if not is_email_unique(user_data["email"]):
                print("Email not unique")
                return False
            if not is_password_valid(user_data["password"]):
                print("Invalid password")
                return False
            if not is_name_valid(user_data["companyName"]):
                print("Invalid company name")
                return False
            if not is_location_valid(user_data["location"]):
                print("Invalid location")
                return False
            if not is_description_valid(user_data["description"]):
                print("Invalid description")
                return False
            if not is_optional_path_valid(user_data["logoPath"]):
                print("Invalid logo path")
                return False
            return True
        except Exception as e:
            print(f"Exception in validate_company_data: {e}")
            return False
        