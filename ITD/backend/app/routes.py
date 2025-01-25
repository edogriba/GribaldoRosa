from flask import jsonify, Flask, request
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, login_required, current_user
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
#from app.managers.application_manager import ApplicationManager

def create_main_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret'
    CORS(app, resources={r"/*": {"origins": "*"}})


    login_manager = LoginManager()
    login_manager.init_app(app)


    app.config["JWT_SECRET_KEY"] = "nTXl6GKclQxRFz57pxXx"  
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=15)  # Short-lived access token
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=7)     # Long-lived refresh token

    jwt = JWTManager(app)

    @app.route('/api/universitylist', methods=['GET', 'OPTIONS'])
    @cross_origin()
    def university_list():     
        try:
            universities = University.get_list_dict()

            return jsonify(universities), 200
        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)


    @app.route('/api/register/university', methods=['POST', 'OPTIONS'])
    @cross_origin()
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
    @cross_origin()
    def student_register():
        try:
            data = request.get_json()

            registrationManager = RegistrationManager()
            return registrationManager.register_student(data)

        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)   


    @app.route('/api/register/company', methods=['POST', 'OPTIONS'])
    @cross_origin()
    def company_register():
        try:
            data = request.get_json()

            registrationManager = RegistrationManager()
            return registrationManager.register_company(data)

        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)   


    @app.route('/api/userlogin', methods = ['POST', 'OPTIONS'])
    @cross_origin()
    def user_login():
        try:
            data = request.get_json()

            login_manager = CustomLoginManager()
            #return login_manager.login(data.get('email'), data.get('password'), load_user=load_user)
            user_dict = login_manager.login(data.get('email'), data.get('password'), load_user=load_user)
            print("response: \n" + 
                    "message : Login successful \n" +
                    "user : " + str(user_dict)
                )
            return jsonify({
                    'message': 'Login successful',
                    'user': user_dict
                }), 200
            
        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)


    @app.route('/api/userlogout', methods=['POST', 'OPTIONS'])
    @login_required
    @cross_origin()
    def user_logout():
        try:
            login_manager = CustomLoginManager()
            return login_manager.logout()
        except Exception as e:
            return handle_general_error(e)


    @app.route('/api/token/refresh', methods=['POST', 'OPTIONS'])
    @jwt_required(refresh=True)
    def refresh_token():
        try: 
            identity = get_jwt_identity()

            if not identity:
                return jsonify({
                    "type": "invalid_token",
                    'message': 'Unauthorized'
                    }), 401
            
            new_access_token = create_access_token(identity=identity)

            response = jsonify({
                'message': 'Token refreshed successfully',
                'access_token': new_access_token
            })

            set_access_cookies(response, new_access_token)

            return response, 200
        
        except Exception as e:
            return handle_general_error(e)


    @app.route('/api/internship/post', methods=['POST', 'OPTIONS'])
    @login_required
    @cross_origin()
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
    @login_required
    @cross_origin()
    def get_internship_by_id(internshipId):
        try:
            internship_manager = InternshipManager()
            return internship_manager.get_internship_by_id(internshipId)

        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)


    @app.route('/api/internship/get_by_company/<int:companyId>', methods=['GET', 'OPTIONS'])
    @login_required
    @cross_origin()
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

    @login_manager.user_loader
    def load_user(user_email):
        type = User.get_type_by_email(user_email)
        if type == "student":
            return Student.get_by_email(user_email)
        elif type == "company":
            return Company.get_by_email(user_email)
        elif type == "university":
            return University.get_by_email(user_email)
        else:
            return None
    
    
    return app