import unittest
import os
from sqlite3 import connect, Row
from app.db.dbModels.internship_db import InternshipDB
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
        self.con.commit()
        self.con.close()

        self.db = InternshipDB()
        self.db.con = connect(os.getenv("TEST_DATABASE"))
        self.db.con.row_factory = Row
    
    def tearDown(self):
        self.db.con.close()
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
        self.db.update_status(internship_id, "Completed")
        internship = self.db.get_by_id(internship_id)
        self.assertEqual(internship["status"], "Completed")


    def test_update_status_invalid(self):
        self.assertFalse(self.db.update_status(999, "Completed"))


if __name__ == '__main__':
    unittest.main()