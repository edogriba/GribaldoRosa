import unittest
import os
from sqlite3 import connect, Row
from app.db.dbModels.internshipPosition_db import InternshipPositionDB
from dotenv import load_dotenv

class TestInternshipPositionDB(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.con = connect(os.getenv("TEST_DATABASE"))
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
        self.con.commit()
        self.con.close()

        self.db = InternshipPositionDB()
        self.db.con = connect(os.getenv("TEST_DATABASE"))
        self.db.con.row_factory = Row
    
    def tearDown(self):
        self.db.con.close()
        os.remove(os.getenv("TEST_DATABASE"))


    def test_insert(self):
        internship_id = self.db.insert(1, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        self.assertIsNotNone(internship_id)
        self.assertEqual(internship_id, 1)
        internship_id = self.db.insert(1, "Program A", 6, "Location A", "Role A", "Skill A", None, "Benefit A", "English", "Description A", "Open")
        self.assertEqual(internship_id, 2)
        internship_id = self.db.insert(1, "Program A", 6, "Location A", "Role A", "Skill A", 1000, None, "English", "Description A", "Open")
        self.assertEqual(internship_id, 3)
        internship_id = self.db.insert(1, "Program A", 6, "Location A", "Role A", "Skill A", None, None, "English", "Description A", "Open")
        self.assertEqual(internship_id, 4)

    
    def test_insert_invalid(self):
        with self.assertRaises(Exception):
            self.db.insert(None, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        with self.assertRaises(Exception):
            self.db.insert(1, None, 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        with self.assertRaises(Exception):
            self.db.insert(1, "Program A", None, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        with self.assertRaises(Exception):
            self.db.insert(1, "Program A", 6, None, "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        with self.assertRaises(Exception):
            self.db.insert(1, "Program A", 6, "Location A", None, "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        with self.assertRaises(Exception):
            self.db.insert(1, "Program A", 6, "Location A", "Role A", None, 1000, "Benefit A", "English", "Description A", "Open")
        with self.assertRaises(Exception):
            self.db.insert(1, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", None, "Description A", "Open")
        with self.assertRaises(Exception):
            self.db.insert(1, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", None, "Open")
        with self.assertRaises(Exception):
            self.db.insert(1, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", None)


    def test_get_by_id(self):
        internship_id = self.db.insert(1, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        internship = self.db.get_by_id(internship_id)
        self.assertIsNotNone(internship)
        self.assertEqual(internship["internshipPositionId"], internship_id)
        self.assertEqual(internship["companyId"], 1)
        self.assertEqual(internship["programName"], "Program A")
        self.assertEqual(internship["duration"], 6)
        self.assertEqual(internship["location"], "Location A")
        self.assertEqual(internship["roleTitle"], "Role A")
        self.assertEqual(internship["skillsRequired"], "Skill A")
        self.assertEqual(internship["compensation"], 1000)
        self.assertEqual(internship["benefits"], "Benefit A")
        self.assertEqual(internship["languagesRequired"], "English")
        self.assertEqual(internship["description"], "Description A")
        self.assertEqual(internship["status"], "Open")


    def test_get_by_id_invalid(self):
        internship = self.db.get_by_id(999)
        self.assertIsNone(internship)


    def test_get_by_companyId(self):
        self.db.insert(1, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        internships = self.db.get_by_companyId(1)
        self.assertEqual(len(internships), 1)
        self.assertEqual(internships[0]["programName"], "Program A")


    def test_get_by_companyId_invalid(self):
        internships = self.db.get_by_companyId(999)
        self.assertEqual(len(internships), 0)


    def test_get_by_program_name(self):
        self.db.insert(1, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        self.db.insert(1, "Program B", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        self.db.insert(1, "Program B", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        internships = self.db.get_by_program_name("Program A")
        self.assertEqual(len(internships), 1)
        self.assertEqual(internships[0]["programName"], "Program A")
        internships = self.db.get_by_program_name("Program B")
        self.assertEqual(len(internships), 2)
        self.assertEqual(internships[0]["programName"], "Program B")
        self.assertEqual(internships[1]["programName"], "Program B")

    
    def test_get_by_program_name_invalid(self):
        internships = self.db.get_by_program_name("Nonexistent Program")
        self.assertEqual(len(internships), 0)


    def test_get_list(self):
        self.db.insert(1, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        self.db.insert(2, "Program B", 12, "Location B", "Role B", "Skill B", 2000, "Benefit B", "Spanish", "Description B", "Closed")
        internships = self.db.get_list()
        self.assertEqual(len(internships), 2)


    def test_update_status(self):
        internship_id = self.db.insert(1, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        self.db.update_status(internship_id, "Closed")
        internship = self.db.get_by_id(internship_id)
        self.assertEqual(internship["status"], "Closed")

    
    def test_update_status_invalid(self):
        self.assertFalse(self.db.update_status(999, "Closed"))


if __name__ == '__main__':
    unittest.main()