import unittest
import os
from sqlite3 import connect, Row
from app.db.dbModels.assessment_db import AssessmentDB
from dotenv import load_dotenv

class TestAssessmentDB(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.con = connect(os.getenv("TEST_DATABASE"))
        self.con.execute(""" DROP TABLE IF EXISTS Assessment""")
        self.con.execute(""" CREATE TABLE IF NOT EXISTS Assessment(
                                AssessmentId INTEGER PRIMARY KEY AUTOINCREMENT,
                                ApplicationId INTEGER NOT NULL,
                                Date TEXT NOT NULL,
                                Link TEXT NOT NULL
                            ); """)
        self.con.commit()
        self.con.close()

        self.db = AssessmentDB()
        self.db.con = connect(os.getenv("TEST_DATABASE"))
        self.db.con.row_factory = Row
    
    def tearDown(self):
        self.db.con.close()
        os.remove(os.getenv("TEST_DATABASE"))


    def test_insert_assessment(self):
        assessment_id = self.db.insert(1, "2023-10-01", "http://example.com")
        self.assertIsInstance(assessment_id, int)


    def test_invalid_insert(self):
        with self.assertRaises(Exception):
            self.db.insert(None, "2023-10-01", "http://example.com")
        with self.assertRaises(Exception):
            self.db.insert(1, None, "http://example.com")
        with self.assertRaises(Exception):
            self.db.insert(1, "2023-10-01", None)


    def test_insert_assessment_multiple(self):
        assessment_id = self.db.insert(1, "2023-10-01", "http://example.com")
        self.assertIsInstance(assessment_id, int)
        assessment_id = self.db.insert(1, "2023-10-02", "http://example.com/2")
        self.assertIsInstance(assessment_id, int)

    
    def test_get_last_assessment_by_application_id_invalid_id(self):
        assessment= self.db.get_last_assessment_by_application_id(None)
        self.assertIsNone(assessment)


    def test_get_last_assessment_by_application_id(self):
        self.db.insert(1, "2023-10-01", "http://example.com")
        self.db.insert(1, "2023-10-02", "http://example.com/2")
        last_assessment = self.db.get_last_assessment_by_application_id(1)
        self.assertEqual(last_assessment["date"], "2023-10-02")
        self.assertEqual(last_assessment["link"], "http://example.com/2")


    def test_get_last_assessment_by_application_id_no_results(self):
        last_assessment= self.db.get_last_assessment_by_application_id(1)
        self.assertIsNone(last_assessment)


    def test_get_last_assessment_by_application_id_multiple(self):
        self.db.insert(1, "2023-10-01", "http://example.com")
        self.db.insert(1, "2023-10-02", "http://example.com/2")
        self.db.insert(1, "2023-10-03", "http://example.com/3")
        last_assessment= self.db.get_last_assessment_by_application_id(1)
        self.assertEqual(last_assessment["date"], "2023-10-03")
        self.assertEqual(last_assessment["link"], "http://example.com/3")

    
    def test_get_last_assessment_by_application_id_multiple_applications(self):
        self.db.insert(1, "2023-10-01", "http://example.com")
        self.db.insert(1, "2023-10-02", "http://example.com/2")
        self.db.insert(2, "2023-10-03", "http://example.com/3")
        last_assessment= self.db.get_last_assessment_by_application_id(1)
        self.assertEqual(last_assessment["date"], "2023-10-02")
        self.assertEqual(last_assessment["link"], "http://example.com/2")

    
    def test_get_last_assessment_by_application_id_multiple_applications_no_results(self):
        self.db.insert(1, "2023-10-01", "http://example.com")
        self.db.insert(1, "2023-10-02", "http://example.com/2")
        self.db.insert(2, "2023-10-03", "http://example.com/3")
        last_assessment= self.db.get_last_assessment_by_application_id(3)
        self.assertIsNone(last_assessment)


    def test_get_last_assessment_by_application_id_invalid_type(self):
        assessment = self.db.get_last_assessment_by_application_id("invalid_id")
        self.assertIsNone(assessment)


    if __name__ == "__main__":
        unittest.main()