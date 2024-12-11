from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

# SQLite database setup
DATABASE = 'SC.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Allows access by column name
    return conn


class Student(Resource):
    def get(self, student_id):
        conn = get_db()
        student = conn.execute("SELECT * FROM students WHERE id=?", (student_id,)).fetchone()
        if student:
            return jsonify({'id': student['id'], 'name': student['name'], 'gpa': student['gpa']})
        return {'message': 'Item not found'}, 404

    def delete(self, student_id):
        conn = get_db()
        conn.execute("DELETE FROM students WHERE id=?", (student_id,))
        conn.commit()
        return {'message': 'Student deleted'}, 200

class StudentList(Resource):
    def get(self):
        conn = get_db()
        students = conn.execute("SELECT * FROM students").fetchall()
        return jsonify([{'id': student['id'], 'name': student['name'], 'gpa': student['gpa']} for student in students])

    def post(self):
        data = request.get_json()
        name = data.get('name')
        gpa = data.get('gpa')
        conn = get_db()
        cursor = conn.execute("INSERT INTO students (name, price) VALUES (?, ?)", (name, gpa))
        conn.commit()
        return {'id': cursor.lastrowid, 'name': name, 'price': gpa}, 201

api.add_resource(StudentList, '/students')
api.add_resource(Student, '/students/<int:student_id>')

if __name__ == '__main__':
    app.run(debug=True)
