import unittest
import os
from sqlite3 import connect, Row
from app.db.dbModels.complaint_db import ComplaintDB
from dotenv import load_dotenv

class TestAssessmentDB(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.con = connect(os.getenv("TEST_DATABASE"))
        self.con.execute(""" DROP TABLE IF EXISTS Complaint """)
        self.con.execute(""" CREATE TABLE IF NOT EXISTS Complaint (
                                ComplaintId INTEGER PRIMARY KEY AUTOINCREMENT,
                                InternshipId INTEGER NOT NULL,
                                SourceId INTEGER NOT NULL,
                                Date TEXT NOT NULL,
                                Content TEXT NOT NULL
                            ); """)
        self.con.commit()
        self.con.close()

        self.db = ComplaintDB()
        self.db.con = connect(os.getenv("TEST_DATABASE"))
        self.db.con.row_factory = Row
    
    def tearDown(self):
        self.db.con.close()
        os.remove(os.getenv("TEST_DATABASE"))


    def test_insert_valid_data(self):
        result = self.db.insert(1, 1, "2023-10-01", "Test complaint content")
        self.assertIsInstance(result, int)


    def test_insert_invalid_data(self):
        with self.assertRaises(Exception):
            self.db.insert(None, 1, "2023-10-01", "Test complaint content")


    def test_insert_and_retrieve(self):
        complaint_id = self.db.insert(1, 1, "2023-10-01", "Test complaint content")
        complaints = self.db.get_by_internship_id(1)
        self.assertEqual(len(complaints), 1)
        self.assertEqual(complaints[0]["complaintId"], complaint_id)
        self.assertEqual(complaints[0]["internshipId"], 1)
        self.assertEqual(complaints[0]["sourceId"], 1)
        self.assertEqual(complaints[0]["date"], "2023-10-01")
        self.assertEqual(complaints[0]["content"], "Test complaint content")


    def test_get_by_internship_id_no_complaints(self):
        complaints = self.db.get_by_internship_id(999)
        self.assertEqual(complaints, [])


    def test_get_by_internship_id_multiple_complaints(self):
        self.db.insert(1, 1, "2023-10-01", "Test complaint content 1")
        self.db.insert(1, 2, "2023-10-02", "Test complaint content 2")
        complaints = self.db.get_by_internship_id(1)
        self.assertEqual(len(complaints), 2)
        self.assertEqual(complaints[0]["internshipId"], 1)
        self.assertEqual(complaints[1]["internshipId"], 1)


    def test_get_by_internship_id_invalid_id(self):
        complaints = self.db.get_by_internship_id("invalid_id")
        self.assertEqual(complaints, [])


    def test_get_by_internship_id_no_internship_id(self):
        complaints = self.db.get_by_internship_id(None)
        self.assertEqual(complaints, [])
