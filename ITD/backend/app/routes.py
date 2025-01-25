from flask import jsonify, Flask, request
from flask_cors import CORS, cross_origin
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required,
)

from datetime import timedelta
import sqlite3
from app.models.student import Student
from app.models.university import University
from app.models.company import Company
from app.models.user import User
from app.utils.error_handler import handle_database_error, handle_general_error
from app.managers.login_manager import LoginManager as CustomLoginManager
from app.managers.registration_manager import RegistrationManager
from app.managers.internship_manager import InternshipManager

def create_main_app():
    app = Flask(__name__)

    # App Configuration
    app.config['SECRET_KEY'] = 'secret'
    app.config["JWT_SECRET_KEY"] = "nTXl6GKclQxRFz57pxXx"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=1)
    app.config["JWT_TOKEN_LOCATION"] = ["headers"]
    app.config["JWT_COOKIE_SECURE"] = False  # Set to True in production with HTTPS
    app.config["JWT_COOKIE_HTTPONLY"] = True
    app.config["JWT_COOKIE_SAMESITE"] = "Lax"
    app.config["JWT_COOKIE_CSRF_PROTECT"] = True  # CSRF protection enabled
    

    # Enable CORS
    CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost:3000"}})

    # Initialize JWT Manager
    jwt = JWTManager(app)
    
    @app.after_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response


    # Function to load a user by email
    def load_user(email):
        """
        Load a user by email by first determining their type using `get_type_by_email`
        and then fetching their details from the corresponding model.

        :param email: Email of the user.
        :return: Instance of the user (User, Student, University, or Company) or None.
        """
        try:
            user_type = User.get_type_by_email(email)  # Determine the user type by email
            
            if user_type == "student":
                return Student.get_by_email(email)
            elif user_type == "university":
                return University.get_by_email(email)
            elif user_type == "company":
                return Company.get_by_email(email)
            
            return None  # If no type matches
        except Exception as e:
            raise e

    # Login Manager Instance


    # Login Route
    @app.route('/api/userlogin', methods=['POST'])
    def user_login():
        try:
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')
            login_manager = CustomLoginManager()
            return login_manager.login(email, password, load_user)     
        except Exception as e:
            return handle_general_error(e)


    # Logout Route
    @app.route('/api/userlogout', methods=['POST'])
    @jwt_required()
    def user_logout():
        try:
            # Use the LoginManager to handle logout
            login_manager = CustomLoginManager()
            return login_manager.logout()
        except Exception as e:
            return handle_general_error(e)


    # Example: Protected Route
    @app.route("/api/protected", methods=["GET"])
    @jwt_required()
    def protected():
        current_user = get_jwt_identity()
        
        mail = current_user.get('email')
        return jsonify({"user": load_user(mail).to_dict()}), 200

    return app
