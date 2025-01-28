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


    def test_update_phone_number(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_phone_number_by_id(user_id, "0987654321")
        self.assertTrue(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['phoneNumber'], "0987654321")


    def test_update_phone_number1(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_phone_number_by_id(user_id + 1, "0987654321")
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id + 1)
        self.assertIsNone(student)

    
    def test_update_phone_number2(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_phone_number_by_id(user_id, None)
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['phoneNumber'], "1234567890")


    def test_update_phone_number3(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_phone_number_by_id(user_id, 1234567894)
        self.assertTrue(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['phoneNumber'], "1234567894")


    def test_update_profile_picture_path(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_profile_picture_path_by_id(user_id, "new/path/to/profile.jpg")
        self.assertTrue(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['profilePicture'], "new/path/to/profile.jpg")

    
    def test_update_profile_picture_path1(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_profile_picture_path_by_id(user_id + 1, "new/path/to/profile.jpg")
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['profilePicture'], None)


    def test_update_profile_picture_path2(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_profile_picture_path_by_id(user_id, None)
        self.assertTrue(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['profilePicture'], None)


    def test_update_profile_picture_path3(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_profile_picture_path_by_id(user_id, 34545)
        self.assertTrue(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['profilePicture'], "34545")


    def test_update_location(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_location_by_id(user_id, "New City")
        self.assertTrue(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['location'], "New City")


    def test_update_location_invalid_id(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_location_by_id(user_id + 1, "New City")
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id + 1)
        self.assertIsNone(student)
        student1 = self.db.get_by_id(user_id)
        self.assertIsNotNone(student1)
        self.assertEqual(student1['location'], "City")


    def test_update_location_empty_string(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_location_by_id(user_id, "")
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['location'], "City")


    def test_update_location_none(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_location_by_id(user_id, None)
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['location'], "City")


    def test_update_degree_program(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_degree_program_by_id(user_id, "Data Science")
        self.assertTrue(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['degreeProgram'], "Data Science")


    def test_update_degree_program_invalid_id(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_degree_program_by_id(user_id + 1, "Data Science")
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id + 1)
        self.assertIsNone(student)
        student1 = self.db.get_by_id(user_id)
        self.assertIsNotNone(student1)
        self.assertEqual(student1['degreeProgram'], "Computer Science")


    def test_update_degree_program_empty_string(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_degree_program_by_id(user_id, "")
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['degreeProgram'], "Computer Science")


    def test_update_degree_program_none(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_degree_program_by_id(user_id, None)
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['degreeProgram'], "Computer Science")


    def test_update_gpa(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_gpa_by_id(user_id, 3.8)
        self.assertTrue(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['GPA'], 3.8)

    
    def test_update_gpa_invalid_id(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_gpa_by_id(user_id + 1, 3.8)
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id + 1)
        self.assertIsNone(student)
        student1 = self.db.get_by_id(user_id)
        self.assertIsNotNone(student1)
        self.assertEqual(student1['GPA'], 3.5)


    def test_update_gpa_none(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_gpa_by_id(user_id, None)
        self.assertTrue(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['GPA'], None)


    def test_update_gpa_invalid_value(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_gpa_by_id(user_id, "invalid_gpa")
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['GPA'], 3.5)


    def test_update_graduation_year(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_graduation_year_by_id(user_id, 2024)
        self.assertTrue(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['graduationYear'], 2024)


    def test_update_graduation_year_invalid_id(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_graduation_year_by_id(user_id + 1, 2024)
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id + 1)
        self.assertIsNone(student)
        student1 = self.db.get_by_id(user_id)
        self.assertIsNotNone(student1)
        self.assertEqual(student1['graduationYear'], 2023)


    def test_update_graduation_year_none(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_graduation_year_by_id(user_id, None)
        self.assertTrue(updated)
        student = self.db.get_by_id(user_id)
        self.assertIsNone(student['graduationYear'])


    def test_update_graduation_year_invalid_value(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_graduation_year_by_id(user_id, "invalid_year")
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['graduationYear'], 2023)


    def test_update_cv_path(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_cv_path_by_id(user_id, "new/path/to/cv")
        self.assertTrue(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['CV'], "new/path/to/cv")


    def test_update_cv_path_invalid_id(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_cv_path_by_id(user_id + 1, "new/path/to/cv")
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id + 1)
        self.assertIsNone(student)
        student1 = self.db.get_by_id(user_id)
        self.assertIsNotNone(student1)
        self.assertEqual(student1['CV'], "path/to/cv")


    def test_update_cv_path_empty_string(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_cv_path_by_id(user_id, "")
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['CV'], "path/to/cv")


    def test_update_cv_path_none(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_cv_path_by_id(user_id, None)
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['CV'], "path/to/cv")


    def test_update_skills(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_skills_by_id(user_id, "Python, SQL, Java")
        self.assertTrue(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['skills'], "Python, SQL, Java")

    
    def test_update_skills_invalid_id(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_skills_by_id(user_id + 1, "Python, SQL, Java")
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id + 1)
        self.assertIsNone(student)
        student1 = self.db.get_by_id(user_id)
        self.assertIsNotNone(student1)
        self.assertEqual(student1['skills'], "Python, SQL")


    def test_update_skills_empty_string(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_skills_by_id(user_id, "")
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['skills'], "Python, SQL")


    def test_update_skills_none(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_skills_by_id(user_id, None)
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['skills'], "Python, SQL")

    
    def test_update_language_spoken(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_language_spoken_by_id(user_id, "English, Spanish")
        self.assertTrue(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['languageSpoken'], "English, Spanish")


    def test_update_language_spoken_invalid_id(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_language_spoken_by_id(user_id + 1, "English, Spanish")
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id + 1)
        self.assertIsNone(student)
        student1 = self.db.get_by_id(user_id)
        self.assertIsNotNone(student1)
        self.assertEqual(student1['languageSpoken'], "English")


    def test_update_language_spoken_empty_string(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_language_spoken_by_id(user_id, "")
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['languageSpoken'], "English")


    def test_update_language_spoken_none(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_language_spoken_by_id(user_id, None)
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['languageSpoken'], "English")


    def test_update_university(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_university_by_id(user_id, 2)
        self.assertTrue(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['universityId'], 2)


    def test_update_university_invalid_id(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_university_by_id(user_id + 1, 2)
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id + 1)
        self.assertIsNone(student)
        student1 = self.db.get_by_id(user_id)
        self.assertIsNotNone(student1)
        self.assertEqual(student1['universityId'], 1)


    def test_update_university_none(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_university_by_id(user_id, None)
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['universityId'], 1)


    def test_update_university_invalid_value(self):
        user_id = self.db.insert(
            email="test@example.com", password="password", firstName="John", lastName="Doe",
            phoneNumber="1234567890", profilePicturePath=None, location="City",
            degreeProgram="Computer Science", gpa=3.5, graduationYear=2023, CVpath="path/to/cv",
            skills="Python, SQL", languageSpoken="English", universityId=1
        )
        updated = self.db.update_university_by_id(user_id, "invalid_university")
        self.assertFalse(updated)
        student = self.db.get_by_id(user_id)
        self.assertEqual(student['universityId'], 1)


if __name__ == '__main__':
    unittest.main()