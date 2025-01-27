from flask import jsonify, Flask, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, get_jwt_identity, jwt_required, get_current_user

from datetime import timedelta

from .utils import handle_error
from .models import User, Student, University, Company
from .managers import LoginManager, RegistrationManager, InternshipManager


def create_main_app():
    app = Flask(__name__)

    # App Configuration
    app.config['SECRET_KEY'] = 'secret'
    app.config["JWT_SECRET_KEY"] = "nTXl6GKclQxRFz57pxXx"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=15)
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
            return jsonify({"user": get_current_user().to_dict()}), 200
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
            return jsonify(universities), 200
        except Exception as e:
            return handle_error(e)


    @app.route('/api/register/university', methods=['POST', 'OPTIONS'])
    def university_register():
        if request.method == 'OPTIONS':
            return jsonify({'status': 'OK'}), 200  
        if request.content_type != 'application/json':
            return jsonify({
                "type": "unsupported_media_type",
                "message": "Content-Type must be application/json"
            }), 415
        try:
            data = request.get_json()

            registrationManager = RegistrationManager()
            return registrationManager.register_university(data)
        
        except Exception as e:
            return handle_error(e)


    @app.route('/api/register/student', methods=['POST', 'OPTIONS'])
    def student_register():
        if request.method == 'OPTIONS':
            return jsonify({'status': 'OK'}), 200  
        if request.content_type != 'application/json':
            return jsonify({
                "type": "unsupported_media_type",
                "message": "Content-Type must be application/json"
            }), 415
        try:
            data = request.get_json()

            registrationManager = RegistrationManager()
            return registrationManager.register_student(data)

        except Exception as e:
            return handle_error(e)   


    @app.route('/api/register/company', methods=['POST', 'OPTIONS'])
    def company_register():
        if request.method == 'OPTIONS':
            return jsonify({'status': 'OK'}), 200  
        if request.content_type != 'application/json':
            return jsonify({
                "type": "unsupported_media_type",
                "message": "Content-Type must be application/json"
            }), 415
        try:
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
            data = request.get_json()
            
            internship_manager = InternshipManager()
            return internship_manager.post_internship_position(data)

        except Exception as e:
            return handle_error(e)
        
    
    @app.route('/api/internship/get_by_id', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def get_internship_position_by_id():
        try:
            data = request.get_json()
            internship_id = data.get('internshipPositionId')

            internship_manager = InternshipManager()
            return internship_manager.get_internship_position_by_id(internship_id)

        except Exception as e:
            return handle_error(e)


    @app.route('/api/internship/get_by_company', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def get_internship_positions_by_company():
        if request.method == 'OPTIONS':
            return jsonify({'status': 'OK'}), 200  
        if request.content_type != 'application/json':
            return jsonify({
                "type": "unsupported_media_type",
                "message": "Content-Type must be application/json"
            }), 415
        try:
            data = request.get_json() 
            company_id = data.get('id')

            internship_manager = InternshipManager()
            return internship_manager.get_internship_positions_by_company(company_id)

        except Exception as e:
            return handle_error(e)
        
    
    @app.route('/api/internship/close', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def close_internship_position():
        try:
            data = request.get_json()
            internship_id = data.get('internshipPositionId')

            internship_manager = InternshipManager()
            return internship_manager.close_internship_position(internship_id)

        except Exception as e:
            return handle_error(e)
    
    """
    @app.route('/api/application/create', methods=['POST', 'OPTIONS'])
    @login_required
    def create_application():
        try:
            data = request.get_json()
            
            application_manager = ApplicationManager()
            return application_manager.create_application(data)
        except Exception as e:
            return handle_error(e)
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
        except Exception as e:
            return handle_error(e)
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

        except Exception as e:
            return handle_error(e)
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

        except Exception as e:
            return handle_error(e)
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

        except Exception as e:
            return handle_error(e)
    """    
    return app
