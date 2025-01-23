from flask import jsonify, Flask, request
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, login_user
import sqlite3
from app.utils.auth import hash_password, verify_password, generate_token
from app.models.student import Student
from app.models.university import University
from app.models.company import Company
from app.models.user import User
from app.utils.error_handler import handle_database_error, handle_general_error

def create_main_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    CORS(app, resources={r"/*": {"origins": "*"}})
    login_manager = LoginManager()
    login_manager.init_app(app)

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
            # Get JSON data from the request
            data = request.get_json()

            # Extract required fields
            values = {
                'email': data.get('university_email'),
                'password': hash_password(data.get('university_password')),
                'name': data.get('name'),
                'address': data.get('location'),
                'websiteURL': data.get('websiteURL'),
                'description': data.get('description'),
                'logoPath': data.get('logoPath', '')  # Optional field
            }

            # Validate required fields
            if not all([values['email'], values['password'], values['name'], values['address'], values['websiteURL'], values['description']]):
                return jsonify({
                    "type": "invalid_request",
                    "message": "All fields (email, password, name, address, websiteURL, description) are required."
                }), 400
            
            university = University.add(**values)

            # Generate a JWT token for the registered student
            token = generate_token(university.get_id())

            # Return success response
            return jsonify({
                'message': 'Registration successful',
                'token': token,
                'user': university.to_dict()
            }), 201

        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)


    @app.route('/api/register/student', methods=['POST', 'OPTIONS'])
    @cross_origin()
    def student_register():
        try:
            # Get JSON data from the request
            data = request.get_json()

            # Extract fields from the JSON
            values = {
                'email'         : data.get('email'),
                'password'      : hash_password(data.get('password')),
                'firstName'     : data.get('firstName'),
                'lastName'      : data.get('lastName'),
                'phoneNumber'   : data.get('phoneNumber'),
                'profilePicturePath': data.get('profilePicturePath', ''),  # Optional
                'location'      : data.get('location'),
                'degreeProgram' : data.get('degreeProgram'),
                'gpa'           : data.get('GPA', None),  # Optional
                'graduationYear': data.get('graduationYear', None),  # Optional
                'CVpath'        : data.get('CVpath'),
                'skills'        : data.get('skills'),
                'languageSpoken': data.get('languageSpoken'),
                'universityId'  : data.get('university')
            }

            student = Student.add(**values)

            # Generate a JWT token for the registered student
            token = generate_token(student.get_id)

            # Return success response
            return jsonify({
                'message': 'Registration successful',
                'token': token,
                'user': student.to_dict()
            }), 201

        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)   


    @app.route('/api/register/company', methods=['POST', 'OPTIONS'])
    @cross_origin()
    def company_register():
        try:
            # Get JSON data from the request
            data = request.get_json()

            # Extract fields from the JSON
            values = {
                'email'         : data.get('email'),
                'password'      : hash_password(data.get('password')),
                'companyName'   : data.get('companyName'),
                'logoPath'      : data.get('logoPath', ''),  # Optional
                'description'   : data.get('description'),
                'location'      : data.get('location'),
            }

            company = Company.add(**values)

            # Generate a JWT token for the registered company
            token = generate_token(company.get_id)

            # Return success response
            return jsonify({
                'message': 'Registration successful',
                'token': token,
                'user': company.to_dict()
            }), 201

        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)   


    @app.route('/api/userlogin', methods = ['POST', 'OPTIONS'])
    @cross_origin()
    def user_login():
        try:
            # Get JSON data from the request
            data = request.get_json()

            # Extract fields from the JSON
            email = data.get('email')
            password = data.get('password')

            # Validate required fields
            if not email or not password:
                return jsonify({
                "type": "invalid_request",
                "message": "Email and password are required."
                }), 400

            # Verify user credentials
            user = load_user(email)

            #if user and user.check_password(password):
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

        except sqlite3.Error as e:
            return handle_database_error(e)
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