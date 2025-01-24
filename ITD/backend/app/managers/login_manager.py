from flask import jsonify
from flask_login import login_user, logout_user
from app.utils.auth import verify_password, generate_token
from app.models.user import User
from app.models.student import Student
from app.models.university import University
from app.models.company import Company

class LoginManager:

    def login(self, email: str, password: str, load_user):
        """
        Login a user with the given email and password.
        
        :param email: Email of the user
        :param password: Password of the user
        :param load_user: Function to load the user by email
        :return: JSON response with user object and token if login is successful, 
                 or an error message if login fails
        """
        try:
            # Validate required fields
            if not email or not password:
                return jsonify({
                "type": "invalid_request",
                "message": "Email and password are required."
                }), 400

            # Verify user credentials
            user = load_user(email)

            if user and verify_password(password, user.get_password()):
                # Generate a JWT token for the authenticated user
                token = generate_token(user.get_id())

                login_user(user, True)
                # Return success response
                return jsonify({
                    'message': 'Login successful',
                    'token': token,
                    'user': user.to_dict()
                }), 200
            else:
                return jsonify({
                    "type": "invalid_credentials",
                    "message": "Invalid email or password."
                }), 401

        except Exception as e:
            return e

    def logout(self):
        """
        Logout the current user.
        
        :return: JSON response with success message if logout is successful, 
                 or an error message if logout fails
        """
        try:
            logout_user()
            return jsonify({
                'message': 'Logout successful'
            }), 200
        except Exception as e:
            return e
        
