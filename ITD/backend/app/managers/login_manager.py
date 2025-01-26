from flask import jsonify
from flask_jwt_extended import create_access_token

from ..utils import verify_password
from ..models import User, Student, University, Company

class LoginManager:

    def login(self, user_data):
        """
        Login a user with the given email and password using JWT.
        :param user_data: Dictionary containing 'email' and 'password' of the user
        :return: JSON response with user object and access token if login is successful,
             or an error message if login fails
        """
        try:
            email = user_data.get('email')
            password = user_data.get('password')

            if not email or not password:
                return jsonify({
                    "type": "invalid_request",
                    "message": "Email and password are required."
                }), 400

            user = self.get_user_by_email(email)
            if not user or not verify_password(password, user.get_password()):
                return jsonify({
                    "type": "invalid_credentials",
                    "message": "Invalid email or password."
                }), 401

            access_token = create_access_token(identity={ "id": user.get_id() })

            return jsonify({
                "message": "Login successful",
                "user": user.to_dict(),
                "access_token": access_token,
            }), 200
        except Exception as e:
            raise e


    def logout(self):
        """
        Logout the current user.
        :return: JSON response with success message if logout is successful,
             or an error message if logout fails
        """
        try:
            response = jsonify({'logout': True})
            
            return response, 200
        except Exception as e:
            return jsonify({"type": "server_error", "message": str(e)}), 500

        
    @staticmethod
    def get_user_by_email(email):
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