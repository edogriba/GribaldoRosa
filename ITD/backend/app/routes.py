from flask import jsonify, Flask, request
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager,
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

    ##########################################################################
    # Authentication Routes                                                  #
    ##########################################################################

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
    
    
    ##########################################################################
    # Registration Routes                                                  #
    #########################
    @app.route('/api/universitylist', methods=['GET', 'OPTIONS'])
    def university_list():     
        try:
            print("University List")
            universities = University.get_list_dict()
            print(universities)
            return jsonify(universities), 200
        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)


    @app.route('/api/register/university', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def university_register():
        try:
            data = request.get_json()

            registrationManager = RegistrationManager()
            return registrationManager.register_university(data)

        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)


    @app.route('/api/register/student', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def student_register():
        if request.method == 'OPTIONS':
            return jsonify({'status': 'OK'}), 200  # Handle preflight request
        if request.content_type != 'application/json':
            return jsonify({
                "type": "unsupported_media_type",
                "message": "Content-Type must be application/json"
            }), 415
        try:
            data = request.get_json()

            registrationManager = RegistrationManager()
            return registrationManager.register_student(data)

        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)   


    @app.route('/api/register/company', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def company_register():
        try:
            data = request.get_json()

            registrationManager = RegistrationManager()
            return registrationManager.register_company(data)

        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)   


    ###############################################################
    # Internship Routes
    ###############################################################

    @app.route('/api/internship/post', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def post_internship():
        try:
            data = request.get_json()
            
            internship_manager = InternshipManager()
            return internship_manager.post_internship(data)
        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)
        
    
    @app.route('/api/internship/get_by_id/<int:internshipId>', methods=['GET', 'OPTIONS'])
    @jwt_required()
    def get_internship_by_id(internshipId):
        try:
            internship_manager = InternshipManager()
            return internship_manager.get_internship_by_id(internshipId)
        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)
    @app.route('/api/internship/get_by_company/<int:companyId>', methods=['GET', 'OPTIONS'])
    @jwt_required()
    def get_internships_by_companyId(companyId):
        try:
            internship_manager = InternshipManager()
            return internship_manager.get_internships_by_company(companyId)
        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)
        
    
    """
    @app.route('/api/application/create', methods=['POST', 'OPTIONS'])
    @login_required
    def create_application():
        try:
            data = request.get_json()
            
            application_manager = ApplicationManager()
            return application_manager.create_application(data)
        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)
    @app.route('/api/application/accept', methods=['POST', 'OPTIONS'])
    @login_required
    def accept_application():
        if request.method == 'OPTIONS':
            return jsonify({'status': 'OK'}), 200  # Handle preflight request
        if request.content_type != 'application/json':
            return jsonify({
                "type": "unsupported_media_type",
                "message": "Content-Type must be application/json"
            }), 415
        try:
            data = request.get_json()
            # Assuming ApplicationManager handles application acceptance
            application_manager = ApplicationManager()
            return application_manager.accept_application(data)
        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)
    @app.route('/api/application/refuse', methods=['POST', 'OPTIONS'])
    @login_required
    def refuse_application():
        if request.method == 'OPTIONS':
            return jsonify({'status': 'OK'}), 200  # Handle preflight request
        if request.content_type != 'application/json':
            return jsonify({
                "type": "unsupported_media_type",
                "message": "Content-Type must be application/json"
            }), 415
        try:
            data = request.get_json()
            # Assuming ApplicationManager handles application refusal
            application_manager = ApplicationManager()
            return application_manager.refuse_application(data)
        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)
    @app.route('/api/internship/accept', methods=['POST', 'OPTIONS'])
    @login_required
    def accept_internship():
        if request.method == 'OPTIONS':
            return jsonify({'status': 'OK'}), 200  # Handle preflight request
        if request.content_type != 'application/json':
            return jsonify({
                "type": "unsupported_media_type",
                "message": "Content-Type must be application/json"
            }), 415
        try:
            data = request.get_json()
            # Assuming InternshipManager handles internship acceptance
            internship_manager = InternshipManager()
            return internship_manager.accept_internship(data)
        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)
    @app.route('/api/internship/refuse', methods=['POST', 'OPTIONS'])
    @login_required
    def refuse_internship():
        if request.method == 'OPTIONS':
            return jsonify({'status': 'OK'}), 200  # Handle preflight request
        if request.content_type != 'application/json':
            return jsonify({
                "type": "unsupported_media_type",
                "message": "Content-Type must be application/json"
            }), 415
        try:
            data = request.get_json()
            # Assuming InternshipManager handles internship refusal
            internship_manager = InternshipManager()
            return internship_manager.refuse_internship(data)
        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)
    """    
    return app
