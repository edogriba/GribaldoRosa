import unittest
import os
from sqlite3 import connect, Row
from app.db.dbModels.user_db import UserDB
from dotenv import load_dotenv

class TestUserDB(unittest.TestCase):
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
        self.con.commit()
        self.con.close()

        self.db = UserDB()
        self.db.con = connect(os.getenv("TEST_DATABASE"))
        self.db.con.row_factory = Row
    
    def tearDown(self):
        self.db.con.close()
        os.remove(os.getenv("TEST_DATABASE"))
    
    def test_insert(self):
        userId = self.db.insert('test@example.com', 'password123', 'student')
        self.assertIsNotNone(userId)


    def test_duplicate_insert(self):
        try:
            self.db.insert('test@example.com', 'password123', 'student')
            self.db.insert('test@example.com', 'password123', 'student')
        except Exception as e:
            self.assertEqual(str(e), 'UNIQUE constraint failed: User.Email')
    

    def test_is_email_unique(self):
        self.db.insert('unique@example.com', 'password123', 'student')
        self.assertFalse(self.db.is_email_unique('unique@example.com'))
        self.assertTrue(self.db.is_email_unique('another@example.com'))
    

    def test_get_type_by_email(self):
        self.db.insert('type@example.com', 'password123', 'student')
        userType = self.db.get_type_by_email('type@example.com')
        self.assertEqual(userType, 'student')
        self.assertIsNone(self.db.get_type_by_email('nonexistent@example.com'))
    

    def test_get_type_by_id(self):
        userId = self.db.insert('id@example.com', 'password123', 'student')
        userType = self.db.get_type_by_id(userId)
        self.assertEqual(userType, 'student')
        self.assertIsNone(self.db.get_type_by_id(999))


if __name__ == '__main__':
    unittest.main()