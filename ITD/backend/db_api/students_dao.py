### ---------------------- ###
 #      PER ORA INUTILE     #
### ---------------------- ###

import sqlite3
from flask import jsonify, Flask, request


# SQLite database setup
DATABASE = 'SC.db'

SECRET_KEY = "123456" 

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
                'exp': datetime.now(datetime.UTC) + datetime.timedelta(hours=24)  # Token valid for 24 hours
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

