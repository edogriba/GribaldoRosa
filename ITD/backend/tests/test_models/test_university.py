import unittest
from unittest.mock import patch
from app.models import University
from app.db.dbModels import UniversityDB


class TestUniversity(unittest.TestCase):

    def setUp(self):
        self.university = University(
            id=1,
            email="test@university.com",
            password="password",
            name="Test University",
            address="123 University St",
            websiteURL="http://www.testuniversity.com",
            description="A test university",
            logoPath=None
        )

        self.university1 = University(
            id=2,
            email="test2@university.com",
            password="password2",
            name="Test University 2",
            address="456 University Ave",
            websiteURL="http://www.testuniversity2.com",
            description="Another test university",
            logoPath="/path/to/logo2.png"
        )
        

    def test_get_id(self):
        self.assertEqual(self.university.get_id(), 1)
        self.assertEqual(self.university1.get_id(), 2)


    def test_get_email(self):
        self.assertEqual(self.university.get_email(), "test@university.com")
        self.assertEqual(self.university1.get_email(), "test2@university.com")


    def test_get_password(self):
        self.assertEqual(self.university.get_password(), "password")
        self.assertEqual(self.university1.get_password(), "password2")


    def test_get_type(self):
        self.assertEqual(self.university.get_type(), "university")
        self.assertEqual(self.university1.get_type(), "university")


    def test_get_name(self):
        self.assertEqual(self.university.get_name(), "Test University")
        self.assertEqual(self.university1.get_name(), "Test University 2")


    def test_get_address(self):
        self.assertEqual(self.university.get_address(), "123 University St")
        self.assertEqual(self.university1.get_address(), "456 University Ave")


    def test_get_websiteURL(self):
        self.assertEqual(self.university.get_websiteURL(), "http://www.testuniversity.com")
        self.assertEqual(self.university1.get_websiteURL(), "http://www.testuniversity2.com")


    def test_get_description(self):
        self.assertEqual(self.university.get_description(), "A test university")
        self.assertEqual(self.university1.get_description(), "Another test university")


    def test_get_logoPath(self):
        self.assertIsNone(self.university.get_logoPath())
        self.assertEqual(self.university1.get_logoPath(), "/path/to/logo2.png")


    def test_to_dict(self):
        expected_dict = {
            'id': 1,
            'email': "test@university.com",
            'type': "university",
            'name': "Test University",
            'address': "123 University St",
            'websiteURL': "http://www.testuniversity.com",
            'description': "A test university",
            'logoPath': None
        }

        expected_dict1 = {
            'id': 2,
            'email': "test2@university.com",
            'type': "university",
            'name': "Test University 2",
            'address': "456 University Ave",
            'websiteURL': "http://www.testuniversity2.com",
            'description': "Another test university",
            'logoPath': "/path/to/logo2.png"
        }

        self.assertEqual(self.university.to_dict(), expected_dict)
        self.assertEqual(self.university1.to_dict(), expected_dict1)


    @patch.object(UniversityDB, 'insert', return_value=1)
    @patch.object(UniversityDB, 'close')
    def test_add_with_logo(self, mock_close, mock_insert):
        university = University.add(
            email="test2@university.com",
            password="password2",
            name="Test University 2",
            address="456 University Ave",
            websiteURL="http://www.testuniversity2.com",
            description="Another test university",
            logoPath="/path/to/logo2.png"
        )
        self.assertIsInstance(university, University)
        self.assertEqual(university.id, 1)
        mock_insert.assert_called_once()
        mock_close.assert_called_once()


    @patch.object(UniversityDB, 'insert', return_value=2)
    @patch.object(UniversityDB, 'close')
    def test_add_no_logo(self, mock_close, mock_insert):
        university = University.add(
            email="test@university.com",
            password="password",
            name="Test University",
            address="123 University St",
            websiteURL="http://www.testuniversity.com",
            description="A test university",
            logoPath=None
        )
        self.assertIsInstance(university, University)
        self.assertEqual(university.id, 2)
        mock_insert.assert_called_once()
        mock_close.assert_called_once()

    
    @patch.object(UniversityDB, 'insert', return_value=None)
    @patch.object(UniversityDB, 'close')
    def test_add_returns_none(self, mock_close, mock_insert):
        university = University.add(
            email="test@university.com",
            password="password",
            name="Test University",
            address="123 University St",
            websiteURL="http://www.testuniversity.com",
            description="A test university",
            logoPath=None
        )
        self.assertIsNone(university)
        mock_insert.assert_called_once()
        mock_close.assert_called_once()

        
    @patch.object(UniversityDB, 'insert', side_effect=Exception("Database insert error"))
    @patch.object(UniversityDB, 'close')
    def test_add_raises_exception(self, mock_close, mock_insert):
        with self.assertRaises(Exception) as context:
            University.add(
                email="test@university.com",
                password="password",
                name="Test University",
                address="123 University St",
                websiteURL="http://www.testuniversity.com",
                description="A test university",
                logoPath=None
            )
        self.assertTrue("Database insert error" in str(context.exception))
        mock_insert.assert_called_once()
        mock_close.assert_called_once()


    @patch.object(UniversityDB, 'get_list_dict', return_value=[{'id': 1, 'name': 'Test University'}])
    @patch.object(UniversityDB, 'close')
    def test_get_list_dict(self, mock_close, mock_get_list_dict):
        universities = University.get_list_dict()
        self.assertEqual(universities, [{'id': 1, 'name': 'Test University'}])
        mock_get_list_dict.assert_called_once()
        mock_close.assert_called_once()

    
    @patch.object(UniversityDB, 'get_list_dict', side_effect=Exception("Database query error"))
    @patch.object(UniversityDB, 'close')
    def test_get_list_dict_raises_exception(self, mock_close, mock_get_list_dict):
        with self.assertRaises(Exception) as context:
            University.get_list_dict()
        self.assertTrue("Database query error" in str(context.exception))
        mock_get_list_dict.assert_called_once()
        mock_close.assert_called_once()


    @patch.object(UniversityDB, 'get_list_dict', return_value=None)
    @patch.object(UniversityDB, 'close')
    def test_get_list_dict_returns_none(self, mock_close, mock_get_list_dict):
        universities = University.get_list_dict()
        self.assertIsNone(universities)
        mock_get_list_dict.assert_called_once()
        mock_close.assert_called_once()


    @patch.object(UniversityDB, 'get_by_id', return_value={
        'id': 1,
        'email': "test@university.com",
        'password': "password",
        'name': "Test University",
        'address': "123 University St",
        'websiteURL': "http://www.testuniversity.com",
        'description': "A test university",
        'logoPath': None
    })
    @patch.object(UniversityDB, 'close')
    def test_get_by_id(self, mock_close, mock_get_by_id):
        university = University.get_by_id(1)
        self.assertIsInstance(university, University)
        self.assertEqual(university.id, 1)
        mock_get_by_id.assert_called_once_with(1)
        mock_close.assert_called_once()


    @patch.object(UniversityDB, 'get_by_id', side_effect=Exception("Database query error"))
    @patch.object(UniversityDB, 'close')
    def test_get_by_id_raises_exception(self, mock_close, mock_get_by_id):
        with self.assertRaises(Exception) as context:
            University.get_by_id(1)
        self.assertTrue("Database query error" in str(context.exception))
        mock_get_by_id.assert_called_once_with(1)
        mock_close.assert_called_once()


    @patch.object(UniversityDB, 'get_by_id', return_value=None)
    @patch.object(UniversityDB, 'close')
    def test_get_by_id_returns_none(self, mock_close, mock_get_by_id):
        university = University.get_by_id(1)
        self.assertIsNone(university)
        mock_get_by_id.assert_called_once_with(1)
        mock_close.assert_called_once()


    @patch.object(UniversityDB, 'get_by_email', return_value={
        'id': 1,
        'email': "test@university.com",
        'password': "password",
        'name': "Test University",
        'address': "123 University St",
        'websiteURL': "http://www.testuniversity.com",
        'description': "A test university",
        'logoPath': None
    })
    @patch.object(UniversityDB, 'close')
    def test_get_by_email(self, mock_close, mock_get_by_email):
        university = University.get_by_email("test@university.com")
        self.assertIsInstance(university, University)
        self.assertEqual(university.id, 1)
        mock_get_by_email.assert_called_once_with("test@university.com")
        mock_close.assert_called_once()

    
    @patch.object(UniversityDB, 'get_by_email', side_effect=Exception("Database query error"))
    @patch.object(UniversityDB, 'close')
    def test_get_by_email_raises_exception(self, mock_close, mock_get_by_email):
        with self.assertRaises(Exception) as context:
            University.get_by_email("test@university.com")
        self.assertTrue("Database query error" in str(context.exception))
        mock_get_by_email.assert_called_once_with("test@university.com")
        mock_close.assert_called_once()


    @patch.object(UniversityDB, 'get_by_email', return_value=None)
    @patch.object(UniversityDB, 'close')
    def test_get_by_email_returns_none(self, mock_close, mock_get_by_email):
        university = University.get_by_email("test@university.com")
        self.assertIsNone(university)
        mock_get_by_email.assert_called_once_with("test@university.com")
        mock_close.assert_called_once()


if __name__ == '__main__':
    unittest.main()