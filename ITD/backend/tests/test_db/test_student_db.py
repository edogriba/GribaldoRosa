import unittest
import os
from sqlite3 import connect, Row
from app.db.dbModels.student_db import StudentDB
from app.db.dbModels.user_db import UserDB
from dotenv import load_dotenv

class TestStudentDB(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.con = connect(os.getenv("TEST_DATABASE"))
        self.con.execute(""" DROP TABLE IF EXISTS User """)
        self.con.execute(""" CREATE TABLE User (
                                UserId INTEGER PRIMARY KEY AUTOINCREMENT,
                                Email TEXT NOT NULL,
                                Password TEXT NOT NULL,
                                Type TEXT NOT NULL
                            ); """)
        self.con.execute(""" DROP TABLE IF EXISTS Student """)
        self.con.execute(""" CREATE TABLE IF NOT EXISTS Student (
                                        UserId INTEGER PRIMARY KEY,
                                        FirstName TEXT NOT NULL,
                                        LastName TEXT NOT NULL,
                                        PhoneNumber TEXT NOT NULL,
                                        ProfilePicturePath TEXT,
                                        Location TEXT NOT NULL,
                                        DegreeProgram TEXT NOT NULL,
                                        Gpa REAL,
                                        GraduationYear INTEGER,
                                        CVpath TEXT NOT NULL,
                                        Skills TEXT NOT NULL,
                                        LanguageSpoken TEXT NOT NULL,
                                        UniversityId INTEGER NOT NULL,
                                        FOREIGN KEY (UserId) REFERENCES User(UserId)
                                ); """)
        self.con.commit()

        self.user_db = UserDB()
        self.user_db.con = self.con
        self.user_db.con.row_factory = Row
        self.db = StudentDB()
        self.db.con = self.con
        self.db.con.row_factory = Row

    def tearDown(self):
        self.con.close()
        os.remove(os.getenv("TEST_DATABASE"))


    def test_insert_student(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath="path/to/profile.jpg", location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        self.assertIsNotNone(user_id)
        student = self.db.get_by_id(user_id)
        self.assertIsNotNone(student)
        self.assertEqual(student['email'], "test@example.com")
        self.assertEqual(student['firstName'], "John")
        self.assertEqual(student['lastName'], "Doe")
        self.assertEqual(student['profilePicture'], "path/to/profile.jpg")


    def test_insert_student_1(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        student = self.db.get_by_id(user_id)
        self.assertIsNotNone(student)
        self.assertEqual(student['email'], "test@example.com")
        self.assertEqual(student['firstName'], "John")
        self.assertEqual(student['lastName'], "Doe")


    def test_insert_student_2(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=None, graduationYear=None, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        student = self.db.get_by_id(user_id)
        self.assertIsNotNone(student)
        self.assertEqual(student['email'], "test@example.com")
        self.assertEqual(student['firstName'], "John")
        self.assertEqual(student['lastName'], "Doe")


    def test_get_student_by_id(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath="path/to/profile.jpg", location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        student = self.db.get_by_id(user_id)
        self.assertIsNotNone(student)
        self.assertEqual(student['email'], "test@example.com")
        self.assertEqual(student['firstName'], "John")
        self.assertEqual(student['lastName'], "Doe")
        self.assertEqual(student['profilePicture'], "path/to/profile.jpg")

        student1 = self.db.get_by_id(user_id + 1)
        self.assertIsNone(student1)
    

    def test_get_student_by_email(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        student = self.db.get_by_email("test@example.com")
        self.assertIsNotNone(student)
        self.assertEqual(student['id'], user_id)


    def test_get_student_by_email_1(self):
        self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        student = self.db.get_by_email("test1@example.com")
        self.assertIsNone(student)


    def test_update_student(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath="path/to/profile.jpg", location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        self.db.update(
            id=user_id, phoneNumber="0987654321", profilePicture="new/path/to/profile.jpg", location="New City",
            degreeProgram="Data Science", GPA=3.8, graduationYear=2024, CV="new/path/to/cv",
            skills="Python, SQL, Java", languageSpoken="English, Spanish", universityId=2
        )
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['phoneNumber'], "0987654321")
        self.assertEqual(student['profilePicture'], "new/path/to/profile.jpg")
        self.assertEqual(student['location'], "New City")
        self.assertEqual(student['degreeProgram'], "Data Science")
        self.assertEqual(student['GPA'], 3.8)
        self.assertEqual(student['graduationYear'], 2024)
        self.assertEqual(student['CV'], "new/path/to/cv")
        self.assertEqual(student['skills'], "Python, SQL, Java")
        self.assertEqual(student['languageSpoken'], "English, Spanish")
        self.assertEqual(student['universityId'], 2)


    def test_update_student_invalid_id(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath="path/to/profile.jpg", location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        with self.assertRaises(Exception) as context:
            self.db.update(
            id=user_id + 1, phoneNumber="0987654321", profilePicture="new/path/to/profile.jpg", location="New City",
            degreeProgram="Data Science", GPA=3.8, graduationYear=2024, CV="new/path/to/cv",
            skills="Python, SQL, Java", languageSpoken="English, Spanish", universityId=2
            )
        self.assertTrue('Student not found' in str(context.exception))
        student = self.db.get_by_id(user_id + 1)
        self.assertIsNone(student)


    def test_update_student_partial_values(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath="path/to/profile.jpg", location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        self.db.update(
            id=user_id, phoneNumber="0987654321", profilePicture=None, location="New City",
            degreeProgram="Data Science", GPA=None, graduationYear=None, CV="new/path/to/cv",
            skills="Python, SQL, Java", languageSpoken="English, Spanish", universityId=2
        )
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['phoneNumber'], "0987654321")
        self.assertEqual(student['profilePicture'], "path/to/profile.jpg")
        self.assertEqual(student['location'], "New City")
        self.assertEqual(student['degreeProgram'], "Data Science")
        self.assertIsNone(student['GPA'])
        self.assertIsNone(student['graduationYear'])
        self.assertEqual(student['CV'], "new/path/to/cv")
        self.assertEqual(student['skills'], "Python, SQL, Java")
        self.assertEqual(student['languageSpoken'], "English, Spanish")
        self.assertEqual(student['universityId'], 2)


if __name__ == '__main__':
    unittest.main()