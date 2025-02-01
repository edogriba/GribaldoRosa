import unittest
import os
from sqlite3 import connect, Row
from app.db.dbModels import InternshipPositionDB, UserDB, CompanyDB
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
        self.con.execute(""" DROP TABLE IF EXISTS User """)
        self.con.execute(""" CREATE TABLE User (
                                UserId INTEGER PRIMARY KEY AUTOINCREMENT,
                                Email TEXT NOT NULL,
                                Password TEXT NOT NULL,
                                Type TEXT NOT NULL
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

        self.db = InternshipPositionDB()
        self.db.con = self.con
        self.db.con.row_factory = Row
        self.user_db = UserDB()
        self.user_db.con = self.con
        self.user_db.con.row_factory = Row
        self.company_db = CompanyDB()
        self.company_db.con = self.con
        self.company_db.con.row_factory = Row

    
    def tearDown(self):
        self.con.close()
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


    def test_get_role_titles(self):
        self.db.insert(1, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        self.db.insert(2, "Program B", 12, "Location B", "Role B", "Skill B", 2000, "Benefit B", "Spanish", "Description B", "Closed")
        self.db.insert(3, "Program C", 3, "Location C", "Role A", "Skill C", 1500, "Benefit C", "French", "Description C", "Open")
        role_titles = self.db.get_role_titles()
        self.assertEqual(len(role_titles), 2)
        self.assertIn("Role A", role_titles)
        self.assertIn("Role B", role_titles)


    def test_get_role_titles_empty(self):
        role_titles = self.db.get_role_titles()
        self.assertEqual(len(role_titles), 0)

    
    def test_get_locations(self):
        self.db.insert(1, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        self.db.insert(2, "Program B", 12, "Location B", "Role B", "Skill B", 2000, "Benefit B", "Spanish", "Description B", "Closed")
        self.db.insert(3, "Program C", 3, "Location A", "Role C", "Skill C", 1500, "Benefit C", "French", "Description C", "Open")
        locations = self.db.get_locations()
        self.assertEqual(len(locations), 2)
        self.assertIn("Location A", locations)
        self.assertIn("Location B", locations)


    def test_get_locations_empty(self):
        locations = self.db.get_locations()
        self.assertEqual(len(locations), 0)


    def test_search_by_company_name(self):
        self.companyId = self.company_db.insert("company@example.com", "password", "Company A", "path/to/logo", "Description", "Location")
        self.db.insert(self.companyId, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        self.db.insert(2, "Program B", 12, "Location B", "Role B", "Skill B", 2000, "Benefit B", "Spanish", "Description B", "Closed")
        self.db.insert(3, "Program C", 3, "Location A", "Role C", "Skill C", 1500, "Benefit C", "French", "Description C", "Open")
        
        filters = {"companyName": "Company A"}
        results = self.db.search(filters)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["companyId"], self.companyId)


    def test_search_by_role_title(self):
        self.companyId = self.company_db.insert("company@example.com", "password", "Company A", "path/to/logo", "Description", "Location")
        self.db.insert(self.companyId, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        self.db.insert(2, "Program B", 12, "Location B", "Role B", "Skill B", 2000, "Benefit B", "Spanish", "Description B", "Closed")
        self.db.insert(3, "Program C", 3, "Location A", "Role C", "Skill C", 1500, "Benefit C", "French", "Description C", "Open")
        
        filters = {"roleTitle": "Role A"}
        results = self.db.search(filters)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["roleTitle"], "Role A")


    def test_search_by_location(self):
        self.companyId = self.company_db.insert("company@example.com", "password", "Company A", "path/to/logo", "Description", "Location")
        self.db.insert(self.companyId, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        self.db.insert(2, "Program B", 12, "Location B", "Role B", "Skill B", 2000, "Benefit B", "Spanish", "Description B", "Closed")
        self.db.insert(3, "Program C", 3, "Location A", "Role C", "Skill C", 1500, "Benefit C", "French", "Description C", "Open")
        
        filters = {"location": "Location A"}
        results = self.db.search(filters)
        self.assertEqual(len(results), 1)


    def test_search_by_min_stipend(self):
        self.companyId = self.company_db.insert("company@example.com", "password", "Company A", "path/to/logo", "Description", "Location")
        self.db.insert(self.companyId, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        self.db.insert(self.companyId, "Program B", 12, "Location B", "Role B", "Skill B", 2000, "Benefit B", "Spanish", "Description B", "Closed")
        self.db.insert(self.companyId, "Program C", 3, "Location A", "Role C", "Skill C", 1500, "Benefit C", "French", "Description C", "Open")
        
        filters = {"minStipend": 1500}
        results = self.db.search(filters)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["compensation"], 1500)


    def test_search_by_min_duration(self):
        self.companyId = self.company_db.insert("company@example.com", "password", "Company A", "path/to/logo", "Description", "Location")
        self.db.insert(self.companyId, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        self.db.insert(self.companyId, "Program B", 12, "Location B", "Role B", "Skill B", 2000, "Benefit B", "Spanish", "Description B", "Closed")
        self.db.insert(self.companyId, "Program C", 3, "Location A", "Role C", "Skill C", 1500, "Benefit C", "French", "Description C", "Open")
        
        filters = {"minDuration": 4}
        results = self.db.search(filters)
        self.assertEqual(len(results), 1)


    def test_search_by_max_duration(self):
        self.companyId = self.company_db.insert("company@example.com", "password", "Company A", "path/to/logo", "Description", "Location")
        self.db.insert(self.companyId, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        self.db.insert(self.companyId, "Program B", 12, "Location B", "Role B", "Skill B", 2000, "Benefit B", "Spanish", "Description B", "Closed")
        self.db.insert(self.companyId, "Program C", 3, "Location A", "Role C", "Skill C", 1500, "Benefit C", "French", "Description C", "Open")
        
        filters = {"maxDuration": 6}
        results = self.db.search(filters)
        self.assertEqual(len(results), 2)


    def test_search_by_role_title_and_location(self):
        self.companyId = self.company_db.insert("company@example.com", "password", "Company A", "path/to/logo", "Description", "Location")
        self.db.insert(self.companyId, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        self.db.insert(2, "Program B", 12, "Location B", "Role B", "Skill B", 2000, "Benefit B", "Spanish", "Description B", "Closed")
        self.db.insert(3, "Program C", 3, "Location A", "Role C", "Skill C", 1500, "Benefit C", "French", "Description C", "Open")
        
        filters = {"roleTitle": "Role A", "location": "Location A"}
        results = self.db.search(filters)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["roleTitle"], "Role A")
        self.assertEqual(results[0]["location"], "Location A")


    def test_search_no_results(self):
        self.companyId = self.company_db.insert("company@example.com", "password", "Company A", "path/to/logo", "Description", "Location")
        self.db.insert(self.companyId, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        self.db.insert(2, "Program B", 12, "Location B", "Role B", "Skill B", 2000, "Benefit B", "Spanish", "Description B", "Closed")
        self.db.insert(3, "Program C", 3, "Location A", "Role C", "Skill C", 1500, "Benefit C", "French", "Description C", "Open")
        
        self.db.insert(1, "Program A", 6, "Location A", "Role A", "Skill A", 1000, "Benefit A", "English", "Description A", "Open")
        filters = {"roleTitle": "Nonexistent Role"}
        results = self.db.search(filters)
        self.assertEqual(len(results), 0)

        filters = {"location": "Nonexistent Location"}
        results = self.db.search(filters)
        self.assertEqual(len(results), 0)

        filters = {"minStipend": 5000}
        results = self.db.search(filters)
        self.assertEqual(len(results), 0)

        filters = {"minDuration": 12}
        results = self.db.search(filters)
        self.assertEqual(len(results), 0)

        filters = {"maxDuration": 1}
        results = self.db.search(filters)
        self.assertEqual(len(results), 0)


if __name__ == '__main__':
    unittest.main()