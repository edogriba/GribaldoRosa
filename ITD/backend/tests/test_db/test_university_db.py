import unittest
import os
from sqlite3 import connect, Row
from app.db.dbModels.user_db import UserDB
from app.db.dbModels.university_db import UniversityDB
from dotenv import load_dotenv

class TestUniversityDB(unittest.TestCase):
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
        self.con.execute(""" DROP TABLE IF EXISTS University """)
        self.con.execute(""" CREATE TABLE IF NOT EXISTS University (
                                UserId INTEGER PRIMARY KEY,
                                Name TEXT NOT NULL,
                                Address TEXT NOT NULL,
                                WebsiteURL TEXT NOT NULL,
                                Description TEXT NOT NULL,
                                LogoPath TEXT,
                                FOREIGN KEY (UserId) REFERENCES User(UserId)
                        ); """)
        self.con.commit()

        self.user_db = UserDB()
        self.user_db.con = self.con
        self.user_db.con.row_factory = Row
        self.db = UniversityDB()
        self.db.con = self.con
        self.db.con.row_factory = Row

    def tearDown(self):
        self.con.close()
        os.remove(os.getenv("TEST_DATABASE"))

    def test_insert_university(self):
        university_id = self.db.insert(
            email="university@example.com", password="password", name="Test University", address="123 University St",
            websiteURL="http://www.testuniversity.com", description="A test university",
            logoPath="path/to/logo.jpg"
        )
        self.assertIsNotNone(university_id)
        
        university = self.db.get_by_id(university_id)
        self.assertIsNotNone(university)
        self.assertEqual(university['id'], university_id)
        self.assertEqual(university['email'], "university@example.com")
        self.assertEqual(university['password'], "password")
        self.assertEqual(university['name'], "Test University")
        self.assertEqual(university['address'], "123 University St")
        self.assertEqual(university['websiteURL'], "http://www.testuniversity.com")
        self.assertEqual(university['description'], "A test university")
        self.assertEqual(university['logoPath'], "path/to/logo.jpg")


    def test_insert_university_no_logo(self):
        university_id = self.db.insert(
            email="university@example.com", password="password", name="Test University", address="123 University St",
            websiteURL="http://www.testuniversity.com", description="A test university",
            logoPath=None
        )
        self.assertIsNotNone(university_id)
        
        university = self.db.get_by_id(university_id)
        self.assertIsNotNone(university)
        self.assertEqual(university['id'], university_id)
        self.assertEqual(university['email'], "university@example.com")
        self.assertEqual(university['password'], "password")
        self.assertEqual(university['name'], "Test University")
        self.assertEqual(university['address'], "123 University St")
        self.assertEqual(university['websiteURL'], "http://www.testuniversity.com")
        self.assertEqual(university['description'], "A test university")
        self.assertIsNone(university['logoPath'])


    def test_insert_invalid_university(self):
        with self.assertRaises(Exception):
            self.db.insert(
                email=None, password="password", name="Test University", address="123 University St",
                websiteURL="http://www.testuniversity.com", description="A test university",
                logoPath="path/to/logo.jpg"
            )

        with self.assertRaises(Exception):
            self.db.insert(
                email="university@example.com", password=None, name="Test University", address="123 University St",
                websiteURL="http://www.testuniversity.com", description="A test university",
                logoPath="path/to/logo.jpg"
            )

        with self.assertRaises(Exception):
            self.db.insert(
                email="university@example.com", password="password", name=None, address="123 University St",
                websiteURL="http://www.testuniversity.com", description="A test university",
                logoPath="path/to/logo.jpg"
            )

        with self.assertRaises(Exception):
            self.db.insert(
                email="university@example.com", password="password", name="Test University", address=None,
                websiteURL="http://www.testuniversity.com", description="A test university",
                logoPath="path/to/logo.jpg"
            )

        with self.assertRaises(Exception):
            self.db.insert(
                email="university@example.com", password="password", name="Test University", address="123 University St",
                websiteURL=None, description="A test university",
                logoPath="path/to/logo.jpg"
            )

        with self.assertRaises(Exception):
            self.db.insert(
                email="university@example.com", password="password", name="Test University", address="123 University St",
                websiteURL="http://www.testuniversity.com", description=None,
                logoPath="path/to/logo.jpg"
            )


    def test_duplicate_insert_university(self):
        university_id_1 = self.db.insert(
            email="university@example.com", password="password", name="Test University", address="123 University St",
            websiteURL="http://www.testuniversity.com", description="A test university",
            logoPath="path/to/logo.jpg"
        )
        self.assertIsNotNone(university_id_1)

        
        with self.assertRaises(Exception):
            self.db.insert(
                email="university@example.com", password="password", name="Test University", address="123 University St",
                websiteURL="http://www.testuniversity.com", description="A test university",
                logoPath="path/to/logo.jpg"
            )


    def test_get_by_id(self):
        university_id = self.db.insert(
            email="university@example.com", password="password", name="Test University", address="123 University St",
            websiteURL="http://www.testuniversity.com", description="A test university",
            logoPath="path/to/logo.jpg"
        )
        self.assertIsNotNone(university_id)
        
        university = self.db.get_by_id(university_id)
        self.assertIsNotNone(university)
        self.assertEqual(university['id'], university_id)
        self.assertEqual(university['email'], "university@example.com")
        self.assertEqual(university['password'], "password")
        self.assertEqual(university['name'], "Test University")
        self.assertEqual(university['address'], "123 University St")
        self.assertEqual(university['websiteURL'], "http://www.testuniversity.com")
        self.assertEqual(university['description'], "A test university")
        self.assertEqual(university['logoPath'], "path/to/logo.jpg")


    def test_get_by_id_not_found(self):
        university = self.db.get_by_id(9999)
        self.assertIsNone(university)


    def test_get_by_email(self):
        university_id = self.db.insert(
            email="university@example.com", password="password", name="Test University", address="123 University St",
            websiteURL="http://www.testuniversity.com", description="A test university",
            logoPath="path/to/logo.jpg"
        )
        self.assertIsNotNone(university_id)
        
        university = self.db.get_by_email("university@example.com")
        self.assertIsNotNone(university)
        self.assertEqual(university['id'], university_id)
        self.assertEqual(university['email'], "university@example.com")
        self.assertEqual(university['password'], "password")
        self.assertEqual(university['name'], "Test University")
        self.assertEqual(university['address'], "123 University St")
        self.assertEqual(university['websiteURL'], "http://www.testuniversity.com")
        self.assertEqual(university['description'], "A test university")
        self.assertEqual(university['logoPath'], "path/to/logo.jpg")


    def test_get_by_email_not_found(self):
        university = self.db.get_by_email("nonexistent@example.com")
        self.assertIsNone(university)
    

    def test_get_list_dict(self):
        university_id_1 = self.db.insert(
            email="university1@example.com", password="password1", name="Test University 1", address="123 University St",
            websiteURL="http://www.testuniversity1.com", description="A test university 1",
            logoPath="path/to/logo1.jpg"
        )
        university_id_2 = self.db.insert(
            email="university2@example.com", password="password2", name="Test University 2", address="456 University Ave",
            websiteURL="http://www.testuniversity2.com", description="A test university 2",
            logoPath="path/to/logo2.jpg"
        )
        
        universities = self.db.get_list_dict()
        self.assertEqual(len(universities), 2)
        
        university_1 = universities[0]
        self.assertEqual(university_1['id'], university_id_1)
        self.assertEqual(university_1['name'], "Test University 1")
        
        university_2 = universities[1]
        self.assertEqual(university_2['id'], university_id_2)
        self.assertEqual(university_2['name'], "Test University 2")


    def test_get_list_dict_empty(self):
        universities = self.db.get_list_dict()
        self.assertEqual(len(universities), 0)

    
    def test_update_university(self):
        university_id = self.db.insert(
            email="university@example.com", password="password", name="Test University", address="123 University St",
            websiteURL="http://www.testuniversity.com", description="A test university",
            logoPath="path/to/logo.jpg"
        )
        self.assertIsNotNone(university_id)
        
        self.db.update(
            id=university_id, address="456 University Ave", websiteURL="http://www.updateduniversity.com",
            description="An updated test university", logoPath="path/to/updated_logo.jpg"
        )
        
        university = self.db.get_by_id(university_id)
        self.assertIsNotNone(university)
        self.assertEqual(university['id'], university_id)
        self.assertEqual(university['address'], "456 University Ave")
        self.assertEqual(university['websiteURL'], "http://www.updateduniversity.com")
        self.assertEqual(university['description'], "An updated test university")
        self.assertEqual(university['logoPath'], "path/to/updated_logo.jpg")


    def test_update_university_no_logo(self):
        university_id = self.db.insert(
            email="university@example.com", password="password", name="Test University", address="123 University St",
            websiteURL="http://www.testuniversity.com", description="A test university",
            logoPath="path/to/logo.jpg"
        )
        self.assertIsNotNone(university_id)
        
        self.db.update(
            id=university_id, address="456 University Ave", websiteURL="http://www.updateduniversity.com",
            description="An updated test university", logoPath=None
        )
        
        university = self.db.get_by_id(university_id)
        self.assertIsNotNone(university)
        self.assertEqual(university['id'], university_id)
        self.assertEqual(university['address'], "456 University Ave")
        self.assertEqual(university['websiteURL'], "http://www.updateduniversity.com")
        self.assertEqual(university['description'], "An updated test university")
        self.assertIsNone(university['logoPath'])


    def test_update_university_not_found(self):
        with self.assertRaises(Exception):
            self.db.update(
                id=9999, address="456 University Ave", websiteURL="http://www.updateduniversity.com",
                description="An updated test university", logoPath="path/to/updated_logo.jpg"
            )
        
if __name__ == '__main__':
    unittest.main()