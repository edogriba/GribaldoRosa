from flask import jsonify, make_response, redirect, url_for
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
                "access_token": access_token,
                "refresh_token": refresh_token
            })
            '''
            response = make_response(redirect(url_for('protected')))
            print(response)
            '''
            #set_access_cookies(response, access_token)
            set_refresh_cookies(response, refresh_token)
            '''
            # Extract all Set-Cookie headers
            set_cookie_headers = response.headers.getlist("Set-Cookie")  # Retrieve all Set-Cookie headers as a list

            # Initialize variables for CSRF tokens
            csrf_access_token = None
            csrf_refresh_token = None

            # Parse the Set-Cookie headers to find both CSRF tokens
            for cookie in set_cookie_headers:
                if "csrf_access_token=" in cookie:
                    csrf_access_token = cookie
                elif "csrf_refresh_token=" in cookie:
                    csrf_refresh_token = cookie

            # Debugging: Print the extracted cookies
            print("CSRF Access Token Set-Cookie:", csrf_access_token)
            print("CSRF Refresh Token Set-Cookie:", csrf_refresh_token)

            # Re-set the CSRF access token with HttpOnly
            if csrf_access_token:
                csrf_access_value = csrf_access_token.split("csrf_access_token=")[-1].split(";")[0]
                response.set_cookie(
                    "csrf_access_token",
                    value=csrf_access_value,
                    httponly=True,  # Ensure HttpOnly
                    secure=False,   # Set to True in production
                    samesite="Lax", # Adjust based on your CORS needs
                )

            # Re-set the CSRF refresh token with HttpOnly
            if csrf_refresh_token:
                csrf_refresh_value = csrf_refresh_token.split("csrf_refresh_token=")[-1].split(";")[0]
                response.set_cookie(
                    "csrf_refresh_token",
                    value=csrf_refresh_value,
                    httponly=True,  # Ensure HttpOnly
                    secure=False,   # Set to True in production
                    samesite="Lax", # Adjust based on your CORS needs
                )'''
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
