import unittest
import os
from sqlite3 import connect, Row
from app.db.dbModels.user_db import UserDB
from app.db.dbModels.company_db import CompanyDB
from dotenv import load_dotenv

class TestCompanyDB(unittest.TestCase):
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

        self.user_db = UserDB()
        self.user_db.con = self.con
        self.user_db.con.row_factory = Row
        self.db = CompanyDB()
        self.db.con = self.con
        self.db.con.row_factory = Row

    def tearDown(self):
        self.con.close()
        os.remove(os.getenv("TEST_DATABASE"))

    def test_insert_company(self):
        email = "test@example.com"
        password = "password123"
        companyName = "Test Company"
        logoPath = "/path/to/logo.png"
        description = "A test company"
        location = "Test Location"

        user_id = self.db.insert(email, password, companyName, logoPath, description, location)

        cur = self.con.cursor()
        cur.execute("SELECT * FROM Company WHERE UserId = ?", (user_id,))
        company = cur.fetchone()

        self.assertIsNotNone(company)
        self.assertEqual(company["CompanyName"], companyName)
        self.assertEqual(company["LogoPath"], logoPath)
        self.assertEqual(company["Description"], description)
        self.assertEqual(company["Location"], location)


    def test_insert_company_invalid(self):
        email = "invalid@example.com"
        password = "password123"
        companyName = "Invalid Company"
        logoPath = "/path/to/logo.png"
        description = "An invalid company"
        location = "Invalid Location"

        with self.assertRaises(Exception):
            self.db.insert(None, password, companyName, logoPath, description, location)

        with self.assertRaises(Exception):
            self.db.insert(email, None, companyName, logoPath, description, location)

        with self.assertRaises(Exception):
            self.db.insert(email, password, None, logoPath, description, location)

        with self.assertRaises(Exception):
            self.db.insert(email, password, companyName, logoPath, None, location)

        with self.assertRaises(Exception):
            self.db.insert(email, password, companyName, logoPath, description, None)
        
        id = self.db.insert(email, password, companyName, None, description, location)
        company = self.db.get_by_id(id)
        self.assertIsNotNone(company)
        self.assertEqual(company["id"], id)
        self.assertEqual(company["email"], email)
        self.assertEqual(company["password"], password) 
        self.assertEqual(company["companyName"], companyName)
        self.assertIsNone(company["logoPath"])
        self.assertEqual(company["description"], description)
        self.assertEqual(company["location"], location)


    def test_insert_duplicate_company(self):
        email = "duplicate@example.com"
        password = "password123"
        companyName = "Duplicate Company"
        logoPath = "/path/to/logo.png"
        description = "A duplicate company"
        location = "Duplicate Location"

        self.db.insert(email, password, companyName, logoPath, description, location)
        with self.assertRaises(Exception):
            self.db.insert(email, password, companyName, logoPath, description, location)


    def test_get_by_id(self):
        email = "test@example.com"
        password = "password123"
        companyName = "Test Company"
        logoPath = "/path/to/logo.png"
        description = "A test company"
        location = "Test Location"

        user_id = self.db.insert(email, password, companyName, logoPath, description, location)
        company = self.db.get_by_id(user_id)

        self.assertIsNotNone(company)
        self.assertEqual(company["id"], user_id)
        self.assertEqual(company["email"], email)
        self.assertEqual(company["password"], password)
        self.assertEqual(company["companyName"], companyName)
        self.assertEqual(company["logoPath"], logoPath)
        self.assertEqual(company["description"], description)
        self.assertEqual(company["location"], location)


    def test_get_by_id_not_found(self):
        company = self.db.get_by_id(9999)
        self.assertIsNone(company)

    
    def test_get_by_email(self):
        email = "test@example.com"
        password = "password123"
        companyName = "Test Company"
        logoPath = "/path/to/logo.png"
        description = "A test company"
        location = "Test Location"

        user_id = self.db.insert(email, password, companyName, logoPath, description, location)
        company = self.db.get_by_email(email)

        self.assertIsNotNone(company)
        self.assertEqual(company["id"], user_id)
        self.assertEqual(company["email"], email)
        self.assertEqual(company["password"], password)
        self.assertEqual(company["companyName"], companyName)
        self.assertEqual(company["logoPath"], logoPath)
        self.assertEqual(company["description"], description)
        self.assertEqual(company["location"], location)


    def test_get_by_email_not_found(self):
        company = self.db.get_by_email("nonexistent@example.com")
        self.assertIsNone(company)


    def test_update_company(self):
        email = "update@example.com"
        password = "password123"
        companyName = "Update Company"
        logoPath = "/path/to/logo.png"
        description = "A company to be updated"
        location = "Initial Location"

        user_id = self.db.insert(email, password, companyName, logoPath, description, location)

        new_logoPath = "/new/path/to/logo.png"
        new_description = "An updated company"
        new_location = "Updated Location"

        self.db.update(user_id, new_logoPath, new_description, new_location)
        company = self.db.get_by_id(user_id)

        self.assertIsNotNone(company)
        self.assertEqual(company["logoPath"], new_logoPath)
        self.assertEqual(company["description"], new_description)
        self.assertEqual(company["location"], new_location)


    def test_update_company_not_found(self):
        with self.assertRaises(Exception) as context:
            self.db.update(9999, "/new/path/to/logo.png", "Non-existent company", "Non-existent location")
        self.assertEqual(str(context.exception), "Company not found")


    def test_update_company_invalid(self):
        email = "invalid_update@example.com"
        password = "password123"
        companyName = "Invalid Update Company"
        logoPath = "/path/to/logo.png"
        description = "A company to be updated"
        location = "Initial Location"

        user_id = self.db.insert(email, password, companyName, logoPath, description, location)

        with self.assertRaises(Exception):
            self.db.update(user_id, None, None, None)

        with self.assertRaises(Exception):
            self.db.update(user_id, "/new/path/to/logo.png", None, "Updated Location")

        with self.assertRaises(Exception):
            self.db.update(user_id, "/new/path/to/logo.png", "An updated company", None)


    def test_update_company_partial(self):
        email = "partial_update@example.com"
        password = "password123"
        companyName = "Partial Update Company"
        logoPath = "/path/to/logo.png"
        description = "A company to be updated"
        location = "Initial Location"

        user_id = self.db.insert(email, password, companyName, logoPath, description, location)

        new_description = "An updated company"

        self.db.update(user_id, None, new_description, location)
        company = self.db.get_by_id(user_id)

        self.assertIsNotNone(company)
        self.assertEqual(company["logoPath"], "/path/to/logo.png")
        self.assertEqual(company["description"], new_description)
        self.assertEqual(company["location"], location)


    def test_get_companies_names(self):
        email1 = "company1@example.com"
        password1 = "password123"
        companyName1 = "Company One"
        logoPath1 = "/path/to/logo1.png"
        description1 = "First company"
        location1 = "Location One"

        email2 = "company2@example.com"
        password2 = "password123"
        companyName2 = "Company Two"
        logoPath2 = "/path/to/logo2.png"
        description2 = "Second company"
        location2 = "Location Two"

        self.db.insert(email1, password1, companyName1, logoPath1, description1, location1)
        self.db.insert(email2, password2, companyName2, logoPath2, description2, location2)

        company_names = self.db.get_companies_names()

        self.assertIn(companyName1, company_names)
        self.assertIn(companyName2, company_names)
        self.assertEqual(len(company_names), 2)


    def test_get_companies_names_empty(self):
        company_names = self.db.get_companies_names()
        self.assertEqual(company_names, [])


if __name__ == '__main__':
    unittest.main()