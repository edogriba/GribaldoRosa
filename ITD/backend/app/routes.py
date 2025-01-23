from flask import jsonify, Flask, request
from flask_cors import CORS
from flask_login import LoginManager
import sqlite3
from app.utils.auth import hash_password, generate_token
from app.models.student import Student
from app.models.university import University
from app.utils.error_handler import handle_database_error, handle_general_error

def create_main_app():

    app = Flask(__name__)
    CORS(app)

    @app.route('/api/universitylist', methods=['GET'])
    def university_list():     
        try:
            universities = University.get_list_dict()

            return jsonify(universities), 200
        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)


    @app.route('/api/register/university', methods=['POST'])
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
                'user': {
                    'id': university.get_id(),
                    'email': university.get_email(),
                    'firstName': university.get_name(),
                }
            }), 201

        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)


    @app.route('/api/register/student', methods=['POST'])
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
                'user': {
                    'id': student.get_id,
                    'email': student.get_email,
                    'firstName': student.get_firstName,
                    'lastName': student.get_lastName
                }
            }), 201

        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)   


    @app.route('/api/userlogin', methods = ['POST'])
    def user_login():
        try:
            # Get JSON data from the request
            data = request.get_json()

            # Extract fields from the JSON
            values = {
                'email'         : data.get('email'),
                'password'      : hash_password(data.get('password')),
            }

            student = Student.add(**values)

            # Generate a JWT token for the registered student
            token = generate_token(student.get_id)

            # Return success response
            return jsonify({
                'message': 'Registration successful',
                'token': token,
                'user': {
                    'id': student.get_id,
                    'email': student.get_email,
                    'firstName': student.get_firstName,
                    'lastName': student.get_lastName
                }
            }), 201

        except sqlite3.Error as e:
            return handle_database_error(e)
        except Exception as e:
            return handle_general_error(e)    

    return app