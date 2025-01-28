import unittest
import os
from sqlite3 import connect, Row
from app.db.dbModels.application_db import ApplicationDB
from dotenv import load_dotenv

class TestApplicationDB(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.con = connect(os.getenv("TEST_DATABASE"))
        self.con.execute(""" DROP TABLE IF EXISTS Application """)
        self.con.execute(""" CREATE TABLE IF NOT EXISTS Application (
                                        ApplicationId INTEGER PRIMARY KEY AUTOINCREMENT,
                                        StudentId INTEGER NOT NULL,
                                        InternshipPositionId INTEGER NOT NULL,
                                        Status TEXT NOT NULL
                                    ); """)
        self.con.commit()
        self.con.close()

        self.db = ApplicationDB()
        self.db.con = connect(os.getenv("TEST_DATABASE"))
        self.db.con.row_factory = Row
    
    def tearDown(self):
        self.db.con.close()
        os.remove(os.getenv("TEST_DATABASE"))

    
    def test_insert_application(self):
        self.db.insert(1, 1, "pending")
        application = self.db.get_by_studentId_internshipPositionId(1, 1)
        self.assertIsNotNone(application)
        self.assertEqual(application["studentId"], 1)
        self.assertEqual(application["internshipPositionId"], 1)
        self.assertEqual(application["status"], "pending")


    def test_invalid_insert(self):
        with self.assertRaises(Exception):
            self.db.insert(None, 1, "pending")
        with self.assertRaises(Exception):
            self.db.insert(1, None, "pending")
        with self.assertRaises(Exception):
            self.db.insert(1, 1, None)


    def test_get_by_id(self):
        self.db.insert(1, 1, "pending")
        application = self.db.get_by_id(1)
        self.assertIsNotNone(application)
        self.assertEqual(application["applicationId"], 1)
        self.assertEqual(application["studentId"], 1)
        self.assertEqual(application["internshipPositionId"], 1)
        self.assertEqual(application["status"], "pending")


    def test_get_by_invalid_id(self):
        application = self.db.get_by_id(999)
        self.assertIsNone(application)


    def test_get_by_studentId(self):
        self.db.insert(1, 1, "pending")
        applications = self.db.get_by_studentId(1)
        self.assertEqual(len(applications), 1)
        self.assertEqual(applications[0]["studentId"], 1)
        self.assertEqual(applications[0]["internshipPositionId"], 1)
        self.assertEqual(applications[0]["status"], "pending")

    
    def test_get_by_invalid_studentId(self):
        applications = self.db.get_by_studentId(999)
        self.assertEqual(len(applications), 0)


    def test_get_by_internshipPositionId(self):
        self.db.insert(1, 1, "pending")
        applications = self.db.get_by_internshipPositionId(1)
        self.assertEqual(len(applications), 1)
        self.assertEqual(applications[0]["studentId"], 1)
        self.assertEqual(applications[0]["internshipPositionId"], 1)
        self.assertEqual(applications[0]["status"], "pending")

    
    def test_get_by_invalid_internshipPositionId(self):
        applications = self.db.get_by_internshipPositionId(999)
        self.assertEqual(len(applications), 0)


    def test_update_status(self):
        self.db.insert(1, 1, "pending")
        self.db.update_status(1, "accepted")
        application = self.db.get_by_id(1)
        self.assertEqual(application["status"], "accepted")

        
    def test_update_invalid_id(self):
        application = self.db.get_by_id(999)
        self.assertIsNone(application)
        self.assertFalse(self.db.update_status(999, "accepted"))


if __name__ == '__main__':
    unittest.main()