from flask import jsonify
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
)
from app.utils.auth import verify_password
from app.models.user import User
from app.models.student import Student
from app.models.university import University
from app.models.company import Company

from flask import jsonify
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
)
from app.utils.auth import verify_password

class LoginManager:

    def login(self, email: str, password: str, load_user):
        """
        Login a user with the given email and password using JWT.
        :param email: Email of the user
        :param password: Password of the user
        :param load_user: Function to load the user by email
        :return: JSON response with user object and tokens if login is successful,
                 or an error message if login fails
        """
        try:
            if not email or not password:
                return jsonify({
                    "type": "invalid_request",
                    "message": "Email and password are required."
                }), 400

            # Load user
            user = load_user(email)
            if not user or not verify_password(password, user.get_password()):
                return jsonify({
                    "type": "invalid_credentials",
                    "message": "Invalid email or password."
                }), 401

            # Create tokens
            access_token = create_access_token(identity={"id": user.get_id(), "email": user.get_email()})
            refresh_token = create_refresh_token(identity={"id": user.get_id(), "email": user.get_email()})

            # Set cookies and return response
            response = jsonify({
                "message": "Login successful",
                "user": user.to_dict(),
            })
            set_access_cookies(response, access_token)
            set_refresh_cookies(response, refresh_token)

            return response, 200
        except Exception as e:
            return jsonify({"type": "server_error", "message": str(e)}), 500

    def logout(self):
        """
        Logout the current user by unsetting JWT cookies.
        :return: JSON response with success message if logout is successful,
                 or an error message if logout fails
        """
        try:
            response = jsonify({'logout': True})
            unset_jwt_cookies(response)
            return response, 200
        except Exception as e:
            return jsonify({"type": "server_error", "message": str(e)}), 500
