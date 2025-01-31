import unittest
from unittest.mock import patch
from app.models import Company
from app.db.dbModels import CompanyDB


class TestCompany(unittest.TestCase):

    def setUp(self):
        self.company = Company(
            id=1,
            email="test@example.com",
            password="password123",
            companyName="Test Company",
            logoPath=None,
            description="A test company",
            location="Test Location"
        )

        self.company1 = Company(
            id=2,
            email="test2@example.com",
            password="password456",
            companyName="Test Company 2",
            logoPath="/path/to/logo2.png",
            description="Another test company",
            location="Another Test Location"
        )
    

    def test_get_id(self):
        self.assertEqual(self.company.get_id(), 1)
        self.assertEqual(self.company1.get_id(), 2)

    
    def test_get_email(self):
        self.assertEqual(self.company.get_email(), "test@example.com")
        self.assertEqual(self.company1.get_email(), "test2@example.com")


    def test_get_password(self):
        self.assertEqual(self.company.get_password(), "password123")
        self.assertEqual(self.company1.get_password(), "password456")


    def test_get_type(self):
        self.assertEqual(self.company.get_type(), "company")
        self.assertEqual(self.company1.get_type(), "company")


    def test_get_companyName(self):
        self.assertEqual(self.company.get_companyName(), "Test Company")
        self.assertEqual(self.company1.get_companyName(), "Test Company 2")


    def test_get_logoPath(self):
        self.assertIsNone(self.company.get_logoPath())
        self.assertEqual(self.company1.get_logoPath(), "/path/to/logo2.png")


    def test_get_description(self):
        self.assertEqual(self.company.get_description(), "A test company")
        self.assertEqual(self.company1.get_description(), "Another test company")


    def test_get_location(self):
        self.assertEqual(self.company.get_location(), "Test Location")
        self.assertEqual(self.company1.get_location(), "Another Test Location")

    
    def test_to_dict(self):
        company_dict = self.company.to_dict()
        expected_dict = {
            'id': 1,
            'email': 'test@example.com',
            'type': 'company',
            'companyName': 'Test Company',
            'logoPath': None,
            'description': 'A test company',
            'location': 'Test Location'
        }
        self.assertEqual(company_dict, expected_dict)

        company_dict1 = self.company1.to_dict()
        expected_dict1 = {
            'id': 2,
            'email': 'test2@example.com',
            'type': 'company',
            'companyName': 'Test Company 2',
            'logoPath': '/path/to/logo2.png',
            'description': 'Another test company',
            'location': 'Another Test Location'
        }
        self.assertEqual(company_dict1, expected_dict1)


    @patch.object(CompanyDB, 'insert', return_value=3)
    @patch.object(CompanyDB, 'close')
    def test_add_company_with_logo(self, mock_close, mock_insert):
        company = Company.add("test3@example.com", "password789", "Test Company 3", "/path/to/logo3.png", "A third test company", "Third Test Location")
        self.assertIsInstance(company, Company)
        self.assertEqual(company.id, 3)
        self.assertEqual(company.email, "test3@example.com")
        self.assertEqual(company.companyName, "Test Company 3")
        self.assertEqual(company.logoPath, "/path/to/logo3.png")
        mock_insert.assert_called_once()
        mock_close.assert_called_once()

    
    @patch.object(CompanyDB, 'insert', return_value=4)
    @patch.object(CompanyDB, 'close')
    def test_add_company_without_logo(self, mock_close, mock_insert):
        company = Company.add("test4@example.com", "password012", "Test Company 4", None, "A fourth test company", "Fourth Test Location")
        self.assertIsInstance(company, Company)
        self.assertEqual(company.id, 4)
        self.assertEqual(company.email, "test4@example.com")
        self.assertEqual(company.companyName, "Test Company 4")
        self.assertIsNone(company.logoPath)
        mock_insert.assert_called_once()
        mock_close.assert_called_once()


    @patch.object(CompanyDB, 'insert', side_effect=Exception("Database error"))
    @patch.object(CompanyDB, 'close')
    def test_add_company_with_exception(self, mock_close, mock_insert):
        with self.assertRaises(Exception) as context:
            Company.add("test5@example.com", "password345", "Test Company 5", None, "A fifth test company", "Fifth Test Location")
        self.assertTrue('Database error' in str(context.exception))
        mock_insert.assert_called_once()
        mock_close.assert_called_once()


    @patch.object(CompanyDB, 'insert', return_value=None)
    @patch.object(CompanyDB, 'close')
    def test_add_company_with_none_return(self, mock_close, mock_insert):
        company = Company.add("test6@example.com", "password678", "Test Company 6", None, "A sixth test company", "Sixth Test Location")
        self.assertIsNone(company)
        mock_insert.assert_called_once()
        mock_close.assert_called_once()


    @patch.object(CompanyDB, 'get_by_id', return_value={
        'id': 1, 'email': 'test@example.com', 'password': 'password123', 'companyName': 'Test Company', 'logoPath': None, 'description': 'A test company', 'location': 'Test Location'
    })
    @patch.object(CompanyDB, 'close')
    def test_get_by_id(self, mock_close, mock_get_by_id):
        company = Company.get_by_id(1)
        self.assertIsInstance(company, Company)
        self.assertEqual(company.id, 1)
        self.assertEqual(company.email, 'test@example.com')
        self.assertEqual(company.companyName, 'Test Company')
        mock_get_by_id.assert_called_once_with(1)
        mock_close.assert_called_once()

    
    @patch.object(CompanyDB, 'get_by_id', return_value=None)
    @patch.object(CompanyDB, 'close')
    def test_get_by_id_not_found(self, mock_close, mock_get_by_id):
        company = Company.get_by_id(999)
        self.assertIsNone(company)
        mock_get_by_id.assert_called_once_with(999)
        mock_close.assert_called_once()

    
    @patch.object(CompanyDB, 'get_by_id', side_effect=Exception("Database error"))
    @patch.object(CompanyDB, 'close')
    def test_get_by_id_with_exception(self, mock_close, mock_get_by_id):
        with self.assertRaises(Exception) as context:
            Company.get_by_id(1)
        self.assertTrue('Database error' in str(context.exception))
        mock_get_by_id.assert_called_once_with(1)
        mock_close.assert_called_once()


    @patch.object(CompanyDB, 'get_by_email', return_value={
        'id': 1, 'email': 'test@example.com', 'password': 'password123', 'companyName': 'Test Company', 'logoPath': None, 'description': 'A test company', 'location': 'Test Location'
    })
    @patch.object(CompanyDB, 'close')
    def test_get_by_email(self, mock_close, mock_get_by_email):
        company = Company.get_by_email('test@example.com')
        self.assertIsInstance(company, Company)
        self.assertEqual(company.id, 1)
        self.assertEqual(company.email, 'test@example.com')
        self.assertEqual(company.companyName, 'Test Company')
        mock_get_by_email.assert_called_once_with('test@example.com')
        mock_close.assert_called_once()

    
    @patch.object(CompanyDB, 'get_by_email', return_value=None)
    @patch.object(CompanyDB, 'close')
    def test_get_by_email_not_found(self, mock_close, mock_get_by_email):
        company = Company.get_by_email('nonexistent@example.com')
        self.assertIsNone(company)
        mock_get_by_email.assert_called_once_with('nonexistent@example.com')
        mock_close.assert_called_once()

    
    @patch.object(CompanyDB, 'get_by_email', side_effect=Exception("Database error"))
    @patch.object(CompanyDB, 'close')
    def test_get_by_email_with_exception(self, mock_close, mock_get_by_email):
        with self.assertRaises(Exception) as context:
            Company.get_by_email('test@example.com')
        self.assertTrue('Database error' in str(context.exception))
        mock_get_by_email.assert_called_once_with('test@example.com')
        mock_close.assert_called_once()


    @patch.object(CompanyDB, 'update')
    @patch.object(CompanyDB, 'get_by_id', return_value={
        'id': 1, 'email': 'test@example.com', 'password': 'password123', 'companyName': 'Test Company', 'logoPath': None, 'description': 'Updated description', 'location': 'Updated Location'
    })
    @patch.object(CompanyDB, 'close')
    def test_update_company(self, mock_close, mock_get_by_id, mock_update):
        company = Company.update(1, None, 'Updated description', 'Updated Location')
        self.assertIsInstance(company, Company)
        self.assertEqual(company.id, 1)
        self.assertEqual(company.description, 'Updated description')
        self.assertEqual(company.location, 'Updated Location')
        mock_update.assert_called_once_with(1, None, 'Updated description', 'Updated Location')
        mock_get_by_id.assert_called_once_with(1)
        mock_close.assert_called_once()

    
    @patch.object(CompanyDB, 'update')
    @patch.object(CompanyDB, 'get_by_id', return_value=None)
    @patch.object(CompanyDB, 'close')
    def test_update_company_not_found(self, mock_close, mock_get_by_id, mock_update):
        company = Company.update(999, None, 'Updated description', 'Updated Location')
        self.assertIsNone(company)
        mock_update.assert_called_once_with(999, None, 'Updated description', 'Updated Location')
        mock_get_by_id.assert_called_once_with(999)
        mock_close.assert_called_once()

    
    @patch.object(CompanyDB, 'update', side_effect=Exception("Database error"))
    @patch.object(CompanyDB, 'close')
    def test_update_company_with_exception(self, mock_close, mock_update):
        with self.assertRaises(Exception) as context:
            Company.update(1, None, 'Updated description', 'Updated Location')
        self.assertTrue('Database error' in str(context.exception))
        mock_update.assert_called_once_with(1, None, 'Updated description', 'Updated Location')
        mock_close.assert_called_once()

        
if __name__ == '__main__':
    unittest.main()