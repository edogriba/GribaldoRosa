from flask import jsonify, Flask, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, get_jwt_identity, jwt_required, get_current_user

from datetime import timedelta

from .utils import handle_error, validate_request, json_success
from .models import User, Student, University, Company
from .managers import LoginManager, RegistrationManager, InternshipManager, ApplicationManager


def create_main_app():
    app = Flask(__name__)

    # App Configuration
    app.config['SECRET_KEY'] = 'secret'
    app.config["JWT_SECRET_KEY"] = "nTXl6GKclQxRFz57pxXx"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=10)
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


    ###########################
    # Authentication Routes   #
    ###########################

    @app.route('/api/userlogin', methods=['POST'])
    def user_login():
        try:
            data = request.get_json()

            login_manager = LoginManager()
            return login_manager.login(data)     
        except Exception as e:
            return handle_error(e)


    @app.route('/api/userlogout', methods=['POST'])
    @jwt_required()
    def user_logout():
        try:
            login_manager = LoginManager()
            return login_manager.logout()
        except Exception as e:
            return handle_error(e)


    @app.route("/api/protected", methods=["GET"])
    @jwt_required()
    def protected():
        try:     
            return json_success(message="Access granted", user = get_current_user().to_dict())
        except Exception as e:
            return handle_error(e)
    
    
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]

        user_type = User.get_type_by_id(identity["id"])  
            
        if user_type == "student":
            return Student.get_by_id(int(identity["id"]))
        elif user_type == "university":
            return  University.get_by_id(int(identity["id"]))
        elif user_type == "company":
            return  Company.get_by_id(int(identity["id"]))
        else:
            return None
    
    ###########################
    #   Registration Routes   #
    ###########################
    @app.route('/api/universitylist', methods=['GET', 'OPTIONS'])
    def university_list():     
        try:
            universities = University.get_list_dict()
            return json_success(message="Universities retrieved", universities=universities)
        except Exception as e:
            return handle_error(e)


    @app.route('/api/register/university', methods=['POST', 'OPTIONS'])
    def university_register():
        try:
            validation_error = validate_request()
            if validation_error:
                return validation_error
            
            data = request.get_json()

            registrationManager = RegistrationManager()
            return registrationManager.register_university(data)
        
        except Exception as e:
            return handle_error(e)


    @app.route('/api/register/student', methods=['POST', 'OPTIONS'])
    def student_register():
        try:
            validation_error = validate_request()
            if validation_error:
                return validation_error
            
            data = request.get_json()

            registrationManager = RegistrationManager()
            return registrationManager.register_student(data)

        except Exception as e:
            return handle_error(e)   


    @app.route('/api/register/company', methods=['POST', 'OPTIONS'])
    def company_register():
        try:
            validation_error = validate_request()
            if validation_error:
                return validation_error
            
            data = request.get_json()

            registrationManager = RegistrationManager()
            return registrationManager.register_company(data)

        except Exception as e:
            return handle_error(e)   


    #########################
    #   Internship Routes   #
    ######################### 

    @app.route('/api/internship/post', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def post_internship_position():
        try:
            validation_error = validate_request()
            if validation_error:
                return validation_error
            
            data = request.get_json()
            print(data)
            data['duration'] = int(data['duration'])
            data['compensation'] = int(data['compensation'])
            print(data)
            internship_manager = InternshipManager()
            return internship_manager.post_internship_position(data)

        except Exception as e:
            return handle_error(e)
        
    
    @app.route('/api/internship/get_by_id', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def get_internship_position_by_id():
        try:
            validation_error = validate_request()
            if validation_error:
                return validation_error
            
            data = request.get_json()

            internship_manager = InternshipManager()
            return internship_manager.get_internship_position_by_id(data.get('internshipPositionId'))

        except Exception as e:
            return handle_error(e)


    @app.route('/api/internship/get_by_company', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def get_internship_positions_by_company():
        try:
            validation_error = validate_request()
            if validation_error:
                return validation_error
            
            data = request.get_json() 

            internship_manager = InternshipManager()
            return internship_manager.get_internship_positions_by_company(data.get('id'))

        except Exception as e:
            return handle_error(e)
        
    
    @app.route('/api/internship/close', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def close_internship_position():
        try:
            validation_error = validate_request()
            if validation_error:
                return validation_error
            
            data = request.get_json()

            internship_manager = InternshipManager()
            return internship_manager.close_internship_position(data.get('internshipPositionId'))

        except Exception as e:
            return handle_error(e)
        
    @app.route('/api/internship/get_by_student', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def get_internship_positions_by_student():
        try:
            validation_error = validate_request()
            if validation_error:
                return validation_error
            
            data = request.get_json()
            
            internship_manager = InternshipManager()
            return internship_manager.get_internship_positions_by_student(data.get('studentId'))

        except Exception as e:
            return handle_error(e)
    
    
    ##########################
    #   Application Routes   #
    ##########################
     
    @app.route('/api/application/create', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def create_application():
        try:
            validation_error = validate_request()
            if validation_error:
                return validation_error
            
            data = request.get_json()
            
            application_manager = ApplicationManager()
            return application_manager.create_application(data.get('internshipPositionId'))
        except Exception as e:
            return handle_error(e)
        
    @app.route('/api/application/accept', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def accept_application():    
        try:
            validation_error = validate_request()
            if validation_error:
                return validation_error
            
            data = request.get_json()
            
            application_manager = ApplicationManager()
            return application_manager.accept_application(**data)
        except Exception as e:
            return handle_error(e)
    

    @app.route('/api/application/reject', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def reject_application():
        try:
            validation_error = validate_request()
            if validation_error:
                return validation_error
            
            data = request.get_json()
            
            application_manager = ApplicationManager()
            return application_manager.reject_application(**data)
        except Exception as e:
            return handle_error(e)
    

    @app.route('/api/application/confirm', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def confirm_application():
        try:
            validation_error = validate_request()
            if validation_error:
                return validation_error
            
            data = request.get_json()
            
            application_manager = ApplicationManager()
            return application_manager.confirm_application(**data)
        except Exception as e:
            return handle_error(e)


    @app.route('/api/application/refuse', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def refuse_application():
        try:
            validation_error = validate_request()
            if validation_error:
                return validation_error
            
            data = request.get_json()

            application_manager = ApplicationManager()
            return application_manager.refuse_application(**data)

        except Exception as e:
            return handle_error(e)
        
    
    
    @app.route('/api/application/get_by_id', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def get_application_by_id():
        try:
            validation_error = validate_request()
            if validation_error:
                return validation_error
            
            data = request.get_json()
            application_manager = ApplicationManager()
            return application_manager.get_application_by_id(data.get('applicationId'))
        except Exception as e:
            return handle_error(e)
        

    @app.route('/api/application/get_by_student', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def get_applications_by_student():
        try:
            validation_error = validate_request()
            if validation_error:
                return validation_error
            
            data = request.get_json()
            print("Ecco cos vedo", data)
            application_manager = ApplicationManager()
            return application_manager.get_applications_by_student(data.get('studentId'))
        except Exception as e:
            return handle_error(e)
        

    @app.route('/api/application/get_by_internship_position', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def get_applications_by_internship_position():
        try:
            validation_error = validate_request()
            if validation_error:
                return validation_error
            
            data = request.get_json()
            print(data)
            
            application_manager = ApplicationManager()
            return application_manager.get_applications_by_internship_position(data.get('internshipPositionId'))
        except Exception as e:
            return handle_error(e)
     
    return app

    
