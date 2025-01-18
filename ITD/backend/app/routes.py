from flask import jsonify, Flask, request
from flask_cors import CORS
import sqlite3
from app.utils.auth import hash_password, generate_token
from app.models.student import Student
from app.models.university import University

def create_main_app():

    app = Flask(__name__)
    CORS(app)

    # SQLite database setup
    DATABASE = 'app/SC.db'

    def get_db():
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row  # Allows access by column name
        return conn

    @app.route('/universitylist', methods=['GET'])
    def university_list():
        try:
            conn = get_db()
            university_list = conn.execute("SELECT id, name FROM Universities").fetchall()

            # Transform the query result into a list of dictionaries
            result = [{'id': row['id'], 'name': row['name']} for row in university_list]

            return jsonify(result), 200
        except Exception as e:
            return jsonify({
                "type": "database_error",
                "message": str(e)
            }), 500
        finally:
            conn.close()


    @app.route('/studentlist', methods=['GET'])
    def student_list():
        try:
            conn = get_db()
            students = conn.execute("SELECT id, name, gpa FROM students").fetchall()

            # Transform the query result into a list of dictionaries
            result = [{'id': student['id'], 'firstName': student['name'], 'GPA': student['gpa']} for student in students]

            return jsonify(result), 200
        except Exception as e:
            return jsonify({
                "type": "database_error",
                "message": str(e)
            }), 500
        finally:
            conn.close()


    @app.route('/register/university', methods=['POST'])
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

        except sqlite3.IntegrityError:
            # Handle duplicate email errors
            return jsonify({
                "type": "conflict",
                "message": "Email already exists."
            }), 400
        except Exception as e:
            # Handle other server-side errors
            return jsonify({
                "type": "server_error",
                "message": str(e)
            }), 500


    @app.route('/register/student', methods=['POST'])
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

        except sqlite3.IntegrityError:
            # Handle unique constraint violations (e.g., duplicate email)
            return jsonify({
                "type": "conflict",
                "message": "Email already exists."
            }), 400
        except Exception as e:
            # Handle other exceptions
            return jsonify({
                "type": "server_error",
                "message": str(e)
            }), 500      

    return app