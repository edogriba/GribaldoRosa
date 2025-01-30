import unittest
import os
from sqlite3 import connect, Row
from app.db.dbModels import InternshipDB, InternshipPositionDB, ApplicationDB, StudentDB, UserDB, CompanyDB
from dotenv import load_dotenv

class TestInternshipDB(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.con = connect(os.getenv("TEST_DATABASE"))
        self.con.execute(""" DROP TABLE IF EXISTS Internship """)
        self.con.execute(""" CREATE TABLE IF NOT EXISTS Internship (
                                InternshipId INTEGER PRIMARY KEY AUTOINCREMENT,
                                InternshipPositionId INTEGER NOT NULL,
                                ApplicationId INTEGER NOT NULL,
                                Status TEXT NOT NULL
                            ); """)
        self.con.execute(""" DROP TABLE IF EXISTS InternshipPosition """)
        self.con.execute(""" CREATE TABLE IF NOT EXISTS InternshipPosition (
                                InternshipPositionId INTEGER PRIMARY KEY AUTOINCREMENT,
                                CompanyId INTEGER NOT NULL,
                                ProgramName TEXT NOT NULL,
                                Duration INTEGER NOT NULL,
                                Location TEXT NOT NULL,
                                RoleTitle TEXT NOT NULL,
                                SkillsRequired TEXT NOT NULL,
                                Compensation INTEGER,
                                Benefits TEXT,
                                LanguagesRequired TEXT NOT NULL,
                                Description TEXT NOT NULL,
                                Status TEXT NOT NULL DEFAULT 'Open'
                            ); """)
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
        self.con.execute(""" DROP TABLE IF EXISTS Application """)
        self.con.execute(""" CREATE TABLE IF NOT EXISTS Application (
                                ApplicationId INTEGER PRIMARY KEY AUTOINCREMENT,
                                StudentId INTEGER NOT NULL,
                                InternshipPositionId INTEGER NOT NULL,
                                Status TEXT NOT NULL
                            ); """)
        self.con.execute(""" DROP TABLE IF EXISTS Company """)
        self.con.execute(""" CREATE TABLE IF NOT EXISTS Company (
                                UserId INTEGER PRIMARY KEY,
                                CompanyName TEXT NOT NULL,
                                LogoPath TEXT,
                                Description TEXT NOT NULL,
                                Location TEXT NOT NULL,
                                FOREIGN KEY (UserId) REFERENCES User(UserId)
                        ); """)
        self.con.commit()

        self.db = InternshipDB()
        self.db.con = self.con
        self.db.con.row_factory = Row
        self.position_db = InternshipPositionDB()
        self.position_db.con = self.con
        self.position_db.con.row_factory = Row
        self.application_db = ApplicationDB()
        self.application_db.con = self.con
        self.application_db.con.row_factory = Row
        self.student_db = StudentDB()
        self.student_db.con = self.con
        self.student_db.con.row_factory = Row
        self.user_db = UserDB()
        self.user_db.con = self.con
        self.user_db.con.row_factory = Row
        self.company_db = CompanyDB()
        self.company_db.con = self.con
        self.company_db.con.row_factory = Row

    
    def tearDown(self):
        self.con.close()
        os.remove(os.getenv("TEST_DATABASE"))


    def test_insert_internship(self):
        internship_id = self.db.insert(1, 1, "Ongoing")
        self.assertIsNotNone(internship_id)

    
    def test_invalid_insert(self):
        with self.assertRaises(Exception):
            self.db.insert(None, 1, "Ongoing")
        with self.assertRaises(Exception):
            self.db.insert(1, None, "Ongoing")
        with self.assertRaises(Exception):
            self.db.insert(1, 1, None)


    def test_get_by_id(self):
        internship_id = self.db.insert(1, 1, "Ongoing")
        internship = self.db.get_by_id(internship_id)
        self.assertIsNotNone(internship)
        self.assertEqual(internship["internshipPositionId"], 1)
        self.assertEqual(internship["applicationId"], 1)
        self.assertEqual(internship["status"], "Ongoing")

    
    def test_get_by_invalid_id(self):
        internship = self.db.get_by_id(999)
        self.assertIsNone(internship)


    def test_get_by_application_id(self):
        self.db.insert(1, 1, "Ongoing")
        internship = self.db.get_by_application_id(1)
        self.assertIsNotNone(internship)
        self.assertEqual(internship["internshipPositionId"], 1)
        self.assertEqual(internship["applicationId"], 1)
        self.assertEqual(internship["status"], "Ongoing")


    def test_get_by_application_id_invalid(self):
        internship = self.db.get_by_application_id(999)
        self.assertIsNone(internship)


    def test_get_by_internshipPosition_id(self):
        self.db.insert(1, 1, "Ongoing")
        internships = self.db.get_by_internshipPosition_id(1)
        self.assertEqual(len(internships), 1)
        self.assertEqual(internships[0]["internshipPositionId"], 1)
        self.assertEqual(internships[0]["applicationId"], 1)
        self.assertEqual(internships[0]["status"], "Ongoing")


    def test_get_by_internshipPosition_id_invalid(self):
        internships = self.db.get_by_internshipPosition_id(999)
        self.assertEqual(len(internships), 0)


    def test_get_by_applicationId_internshipPositionId(self):
        self.db.insert(1, 1, "Ongoing")
        internship = self.db.get_by_applicationId_internshipPositionId(1, 1)
        self.assertIsNotNone(internship)
        self.assertEqual(internship["internshipPositionId"], 1)
        self.assertEqual(internship["applicationId"], 1)
        self.assertEqual(internship["status"], "Ongoing")


    def test_get_by_applicationId_internshipPositionId_invalid(self):
        internship = self.db.get_by_applicationId_internshipPositionId(999, 999)
        self.assertIsNone(internship)


    def test_update_status(self):
        internship_id = self.db.insert(1, 1, "Ongoing")
        self.db.update_status(internship_id, "Finished")
        internship = self.db.get_by_id(internship_id)
        self.assertEqual(internship["status"], "Finished")


    def test_update_status_invalid(self):
        self.assertFalse(self.db.update_status(999, "Finished"))

    
    def test_get_by_company_id(self):
        self.position_db.insert(1, "Program A", 6, "Location A", "Role A", "Skills A", 1000, "Benefits A", "Languages A", "Description A", "Open")
        self.db.insert(1, 1, "Ongoing")
        internships = self.db.get_by_company_id(1)
        self.assertEqual(len(internships), 1)
        self.assertEqual(internships[0]["internshipPositionId"], 1)
        self.assertEqual(internships[0]["applicationId"], 1)
        self.assertEqual(internships[0]["status"], "Ongoing")


    def test_get_by_company_id_invalid(self):
        internships = self.db.get_by_company_id(999)
        self.assertEqual(len(internships), 0)


    def test_get_preview_by_company_id(self):
        self.position_db.insert(1, "Program A", 6, "Location A", "Role A", "Skills A", 1000, "Benefits A", "Languages A", "Description A", "Open")
        self.con.execute(""" INSERT INTO Student (UserId, FirstName, LastName, PhoneNumber, ProfilePicturePath, Location, DegreeProgram, Gpa, GraduationYear, CVpath, Skills, LanguageSpoken, UniversityId) VALUES (1, 'John', 'Doe', '1234567890', 'path/to/photo', 'Location A', 'Degree A', 3.5, 2023, 'path/to/cv', 'Skills A', 'English', 1) """)
        self.con.execute(""" INSERT INTO Application (StudentId, InternshipPositionId, Status) VALUES (1, 1, 'Ongoing') """)
        self.db.insert(1, 1, "Ongoing")
        internships = self.db.get_preview_by_company_id(1)
        self.assertEqual(len(internships), 1)
        self.assertEqual(internships[0]["student_name"], "John Doe")
        self.assertEqual(internships[0]["student_photoPath"], "path/to/photo")
        self.assertEqual(internships[0]["internshipId"], 1)
        self.assertEqual(internships[0]["roleTitle"], "Role A")
        self.assertEqual(internships[0]["status"], "Ongoing")


    def test_get_preview_by_company_id_invalid(self):
        internships = self.db.get_preview_by_company_id(999)
        self.assertEqual(len(internships), 0)

    
    def test_get_preview_by_student_id(self):
        self.position_db.insert(1, "Program A", 6, "Location A", "Role A", "Skills A", 1000, "Benefits A", "Languages A", "Description A", "Open")
        self.company_db.insert('test@gmail.com', 'password1', 'Company A', 'path/to/logo', 'Description A', 'Location A')
        self.con.execute(""" INSERT INTO Student (UserId, FirstName, LastName, PhoneNumber, ProfilePicturePath, Location, DegreeProgram, Gpa, GraduationYear, CVpath, Skills, LanguageSpoken, UniversityId) VALUES (1, 'John', 'Doe', '1234567890', 'path/to/photo', 'Location A', 'Degree A', 3.5, 2023, 'path/to/cv', 'Skills A', 'English', 1) """)
        self.con.execute(""" INSERT INTO Application (StudentId, InternshipPositionId, Status) VALUES (1, 1, 'Ongoing') """)
        self.db.insert(1, 1, "Ongoing")
        internships = self.db.get_preview_by_student_id(1)
        self.assertEqual(len(internships), 1)
        self.assertEqual(internships[0]["company_name"], "Company A")
        self.assertEqual(internships[0]["company_photoPath"], "path/to/logo")
        self.assertEqual(internships[0]["internshipId"], 1)
        self.assertEqual(internships[0]["roleTitle"], "Role A")
        self.assertEqual(internships[0]["status"], "Ongoing")


    def test_get_preview_by_student_id_invalid(self):
        internships = self.db.get_preview_by_student_id(999)
        self.assertEqual(len(internships), 0)


    def test_get_preview_by_university_id(self):
        self.position_db.insert(1, "Program A", 6, "Location A", "Role A", "Skills A", 1000, "Benefits A", "Languages A", "Description A", "Open")
        self.company_db.insert('test@gmail.com', 'password1', 'Company A', 'path/to/logo', 'Description A', 'Location A')
        self.con.execute(""" INSERT INTO Student (UserId, FirstName, LastName, PhoneNumber, ProfilePicturePath, Location, DegreeProgram, Gpa, GraduationYear, CVpath, Skills, LanguageSpoken, UniversityId) VALUES (1, 'John', 'Doe', '1234567890', 'path/to/photo', 'Location A', 'Degree A', 3.5, 2023, 'path/to/cv', 'Skills A', 'English', 1) """)
        self.con.execute(""" INSERT INTO Application (StudentId, InternshipPositionId, Status) VALUES (1, 1, 'Ongoing') """)
        self.db.insert(1, 1, "Ongoing")
        internships = self.db.get_preview_by_university_id(1)
        self.assertEqual(len(internships), 1)
        self.assertEqual(internships[0]["student_name"], "John Doe")
        self.assertEqual(internships[0]["company_name"], "Company A")
        self.assertEqual(internships[0]["internshipId"], 1)
        self.assertEqual(internships[0]["roleTitle"], "Role A")
        self.assertEqual(internships[0]["status"], "Ongoing")


    def test_get_preview_by_university_id_invalid(self):
        internships = self.db.get_preview_by_university_id(999)
        self.assertEqual(len(internships), 0)


if __name__ == '__main__':
    unittest.main()