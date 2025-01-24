from flask import jsonify, Flask, request
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, login_required
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
    def university_list():     
        try:
            universities = University.get_list_dict()

            return jsonify(universities), 200
        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)


    @app.route('/api/register/university', methods=['POST', 'OPTIONS'])
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
    def user_login():
        try:
            data = request.get_json()

            login_manager = CustomLoginManager()
            return login_manager.login(data.get('email'), data.get('password'), load_user=load_user)
            
        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)


    @app.route('/api/userlogout', methods=['POST', 'OPTIONS'])
    @login_required
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