from flask import jsonify, Flask, request
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required,
    set_access_cookies,
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
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=15)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=7)
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
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        return response

    login_manager = CustomLoginManager()

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
            
            # Use the LoginManager to handle login
            return login_manager.login(email, password, load_user)
        except Exception as e:
            return handle_general_error(e)


    # Logout Route
    @app.route('/api/userlogout', methods=['POST'])
    @jwt_required()
    def user_logout():
        try:
            # Use the LoginManager to handle logout
            return login_manager.logout()
        except Exception as e:
            return handle_general_error(e)

    # Refresh Token Route
    @app.route('/api/token/refresh', methods=['POST'])
    @jwt_required(refresh=True)
    def refresh_token():
        try:
            identity = get_jwt_identity()
            user = User.get_by_email(identity)  # Fetch user details using identity
            new_access_token = create_access_token(identity=user.email)
            return jsonify({"message": "Token refreshed"}), 200
        except Exception as e:
            return handle_general_error(e)

    # Example: Protected Route
    @app.route("/api/protected", methods=["GET"])
    @jwt_required()
    def protected():
        current_user = get_jwt_identity()
        print("Current User:", current_user)
        return jsonify({"user": current_user}), 200

    return app
