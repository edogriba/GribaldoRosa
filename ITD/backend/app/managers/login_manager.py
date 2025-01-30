from flask_jwt_extended import create_access_token

from ..utils import verify_password, json_success, json_invalid_request, json_unauthorized
from ..models import User, Student, University, Company
from typing import Union

class LoginManager:

    def login(self, email: str, password: str):
        """
        Login a user with the given email and password using JWT.
        :param user_data: Dictionary containing 'email' and 'password' of the user
        :return: JSON response with user object and access token if login is successful,
             or an error message if login fails
        """
        try:
            if not email or not password:
                return json_invalid_request("Email and password are required.")

            user = self.get_user_by_email(email)
            if not user or not verify_password(password, user.get_password()):
                return json_unauthorized("Invalid email or password.")

            access_token = create_access_token(identity={ "id": user.get_id() })

            return json_success("Login successful", user = user.to_dict(), access_token = access_token)

        except Exception as e:
            raise e


    def logout(self):
        """
        Logout the current user.
        :return: JSON response with success message if logout is successful,
             or an error message if logout fails
        """
        try:
            return json_success("Logout successful", logout = True)
        
        except Exception as e:
            raise e

        
    @staticmethod
    def get_user_by_email(email: str) -> Union['Student', 'University', 'Company', None, Exception]:
        """
        Load a user by email by first determining their type using `get_type_by_email`
        and then fetching their details from the corresponding model.

        :param email: Email of the user.
        :return: Instance of the user (User, Student, University, or Company) or None.
        """
        try:
            user_type = User.get_type_by_email(email)
            
            if user_type == "student":
                return Student.get_by_email(email)
            elif user_type == "university":
                return University.get_by_email(email)
            elif user_type == "company":
                return Company.get_by_email(email)
            
            return None 
        except Exception as e:
            raise e