from flask import jsonify, Flask, request
from flask_cors import CORS
import sqlite3
#import pdb
import jwt
import bcrypt
from datetime import datetime, timedelta


SECRET_KEY = "123456"


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
                 

    @app.route('/register/university', methods=['POST'])
    def university_register():

        data = request.get_json()

        # Extract required fields
        email = data.get('university_email')
        password = data.get('university_password')
        name = data.get('name')
        location = data.get('location')
        description = data.get('description')
        logoPath = data.get('logoPath', '')  # Optional field

        # Validate required fields
        if not all([email, password, name, location, description]):
            return jsonify({
                "type": "invalid_request",
                "message": "All fields (email, password, name, location, description) are required."
            }), 400

        # Hash the password
        hashed_password = hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

        conn = get_db()
        try:
            # Insert data into the database
            cursor = conn.execute("""
                INSERT INTO universities (email, password, name, location, description, logoPath)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (email, hashed_password, name, location, description, logoPath))
            conn.commit()

            # Generate a JWT token
            token = encode({
                'user_id': cursor.lastrowid,
                'exp': datetime.now(datetime.UTC) + timedelta(hours=24)  # Token valid for 24 hours
            }, SECRET_KEY, algorithm="HS256")

            # Success response
            return jsonify({
                'message': 'Registration successful',
                'token': token,
                'user': {
                    'id': cursor.lastrowid,
                    'email': email,
                    'name': name
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
        finally:
            conn.close()


    @app.route('/register/student', methods=['POST'])
    def student_register():
        # Get JSON data from the request
        data = request.get_json()

        # Extract fields from the JSON
        email = data.get('email')
        password = data.get('password')
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        phone_number = data.get('phoneNumber')
        profile_picture_path = data.get('profilePicturePath', '')  # Optional
        location = data.get('location')
        degree_program = data.get('degreeProgram')
        gpa = data.get('GPA', None)  # Optional
        graduation_year = data.get('graduationYear', None)  # Optional
        cv_path = data.get('CVpath')
        skills = data.get('skills')
        languages_spoken = data.get('languageSpoken')
        university_id = data.get('university')

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        conn = get_db()
        try:
            # Insert student data into the database
            cursor = conn.execute("""
                INSERT INTO Students (
                    email, password, firstName, lastName, phoneNumber, profilePicturePath, 
                    location, degreeProgram, GPA, graduationYear, CVpath, skills, 
                    languageSpoken, university
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                email, hashed_password, first_name, last_name, phone_number, profile_picture_path,
                location, degree_program, gpa, graduation_year, cv_path, skills,
                languages_spoken, university_id
            ))
            conn.commit()

            # Generate a JWT token for the registered student
            token = jwt.encode({
                'user_id': cursor.lastrowid,
                'exp': datetime.now(datetime.UTC) + timedelta(hours=24)  # Token valid for 24 hours
            }, SECRET_KEY, algorithm="HS256")

            # Return success response
            return jsonify({
                'message': 'Registration successful',
                'token': token,
                'user': {
                    'id': cursor.lastrowid,
                    'email': email,
                    'firstName': first_name,
                    'lastName': last_name
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
        finally:
            conn.close()

    return app