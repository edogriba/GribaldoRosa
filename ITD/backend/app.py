from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import sqlite3
from flask_cors import CORS
import bcrypt
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "123456" 

app = Flask(__name__)
api = Api(app)
CORS(app)

# SQLite database setup
DATABASE = 'SC.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Allows access by column name
    return conn


class StudentList(Resource):
    def get(self):
        conn = get_db()
        students = conn.execute("SELECT * FROM students").fetchall()
        return jsonify([{'id': student['id'], 'firstName': student['name'], 'GPA': student['gpa']} for student in students])

    def post(self):
        data = request.get_json()
        name = data.get('name')
        gpa = data.get('gpa')
        conn = get_db()
        cursor = conn.execute("INSERT INTO students (name, price) VALUES (?, ?)", (name, gpa))
        conn.commit()
        return {'id': cursor.lastrowid, 'name': name, 'price': gpa}, 201

class StudentRegistration(Resource):

    def post(self):
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

        # Get the database connection
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
                'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=24)  # Token valid for 24 hours
            }, SECRET_KEY, algorithm="HS256")

            # Return success response
            return {
                'message': 'Registration successful',
                'token': token,
                'user': {
                    'id': cursor.lastrowid,
                    'email': email,
                    'firstName': first_name,
                    'lastName': last_name
                }
            }, 201

        except sqlite3.IntegrityError:
            # Handle unique constraint violations (e.g., duplicate email)
            return {'message': 'Email already exists'}, 400
        except Exception as e:
            # Handle other exceptions
            return {'message': f'An error occurred: {str(e)}'}, 500



class UniversityRegistration(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('university_email')
        password = data.get('university_password')
        name = data.get('name')
        location = data.get('location') 
        description = data.get('description')
        logoPath = data.get('logoPath', '')  # Optional logo field
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        conn = get_db()
        try:
            cursor = conn.execute("""
                    INSERT INTO universities (email, password, name, location, description)
                    VALUES (?, ?, ?, ?, ?)
                """, (email, hashed_password, name, location, description))
            conn.commit()

            token = jwt.encode({
                    'user_id': cursor.lastrowid,
                    'exp': datetime.datetime.now(datetime.UTC) + timedelta(hours=24)  # Token valid for 24 hours
                }, SECRET_KEY, algorithm="HS256")

            
            return {
                    'message': 'Registration successful',
                    'token': token,
                    'user': {
                        'id': cursor.lastrowid,
                        'email': email,
                        'name': name
                    }
                }, 201
        except sqlite3.IntegrityError:
            return {'message': 'Email already exists'}, 400

class UniversityList(Resource):
    def get(self):
        conn = get_db()
        university_list = conn.execute("SELECT id, name FROM universities").fetchall()
        return jsonify([{'id': u['id'], 'name': u['name']} for u in university_list])

api.add_resource(StudentList, '/studentlist')
api.add_resource(UniversityRegistration, '/register/university')
api.add_resource(StudentRegistration, '/register/student')
api.add_resource(UniversityList, '/universitylist')


if __name__ == '__main__':
    app.run(debug=True)
