import unittest
import os
from app.models.user import User
from app.db.dbModels.user_db import UserDB

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User(id=1, email="test@example.com", password="password123", type="student")
        self.db = UserDB()

    def tearDown(self):
        self.db.con.close()
        os.remove(os.getenv("TEST_DATABASE"))


    def test_get_id(self):
        self.assertEqual(self.user.get_id(), 1)


    def test_get_email(self):
        self.assertEqual(self.user.get_email(), "test@example.com")


    def test_get_type(self):
        self.assertEqual(self.user.get_type(), "student")


    def test_get_password(self):
        self.assertEqual(self.user.get_password(), "password123")


    def test_to_dict(self):
        expected_dict = {
            'id': 1,
            'email': "test@example.com",
            'type': "student"
        }
        self.assertEqual(self.user.to_dict(), expected_dict)


    def test_check_password(self):
        self.assertTrue(self.user.check_password("password123"))
        self.assertFalse(self.user.check_password("wrongpassword"))
        self.assertFalse(self.user.check_password(""))
        self.assertFalse(self.user.check_password(None))    
        self.assertFalse(self.user.check_password(123))


    def test_is_email_unique(self):
        UserDB.is_email_unique = lambda self, email: email != "test@example.com"
        self.assertTrue(User.is_email_unique("unique@example.com"))
        self.assertFalse(User.is_email_unique("test@example.com"))


    def test_is_email_unique_raises_exception(self):
        def mock_is_email_unique(self, email):
            raise Exception("Database error")
        
        UserDB.is_email_unique = mock_is_email_unique
        with self.assertRaises(Exception) as context:
            User.is_email_unique("test@example.com")
        self.assertEqual(str(context.exception), "Database error")


    def test_get_type_by_email(self):
        UserDB.get_type_by_email = lambda self, email: "student" if email == "test@example.com" else None
        self.assertEqual(User.get_type_by_email("test@example.com"), "student")
        self.assertIsNone(User.get_type_by_email("unknown@example.com"))


    def test_get_type_by_email_raises_exception(self):
        def mock_get_type_by_email(self, email):
            raise Exception("Database error")
        
        UserDB.get_type_by_email = mock_get_type_by_email
        with self.assertRaises(Exception) as context:
            User.get_type_by_email("test@example.com")
        self.assertEqual(str(context.exception), "Database error")


    def test_get_type_by_id(self):
        UserDB.get_type_by_id = lambda self, id: "student" if id == 1 else None
        self.assertEqual(User.get_type_by_id(1), "student")
        self.assertIsNone(User.get_type_by_id(2))

    
    def test_get_type_by_id_raises_exception(self):
        def mock_get_type_by_id(self, id):
            raise Exception("Database error")
        
        UserDB.get_type_by_id = mock_get_type_by_id
        with self.assertRaises(Exception) as context:
            User.get_type_by_id(1)
        self.assertEqual(str(context.exception), "Database error")


if __name__ == '__main__':
    unittest.main()