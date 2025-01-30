"""
import unittest
from unittest.mock import patch, MagicMock
from app.managers.registration_manager import RegistrationManager


class TestRegistrationManager(unittest.TestCase):

    def setUp(self):
        self.manager = RegistrationManager()
        self.user_data_student = {
            'email': 'student@example.com',
            'password': 'Password123!',
            'firstName': 'John',
            'lastName': 'Doe',
            'phoneNumber': '1234567890',
            'profilePicturePath': None,
            'location': 'Somewhere',
            'degreeProgram': 'Computer Science',
            'GPA': 3.5,
            'graduationYear': 2023,
            'CVpath': '/path/to/cv',
            'skills': ['Python', 'Java'],
            'languageSpoken': ['English'],
            'university': 1
        }
        self.user_data_university = {
            'university_email': 'university@example.com',
            'university_password': 'Password123!',
            'name': 'Example University',
            'location': 'Somewhere',
            'websiteURL': 'http://example.com',
            'description': 'A great university',
            'logoPath': '/path/to/logo'
        }
        self.user_data_company = {
            'email': 'company@example.com',
            'password': 'Password123!',
            'companyName': 'Example Company',
            'logoPath': '/path/to/logo',
            'description': 'A great company',
            'location': 'Somewhere'
        }


    @patch('app.managers.registration_manager.validate_student_data', return_value=True)
    @patch('app.managers.registration_manager.Student.add')
    @patch('app.managers.registration_manager.hash_password', return_value='hashed_password')
    @patch('app.managers.registration_manager.create_access_token', return_value='access_token')
    def test_register_student_success(self, mock_create_access_token, mock_hash_password, mock_student_add, mock_validate_student_data):
        mock_student = MagicMock()
        mock_student.get_id.return_value = 1
        mock_student.to_dict.return_value = self.user_data_student
        mock_student_add.return_value = mock_student

        response = self.manager.register_student(self.user_data_student)

        self.assertEqual(response['message'], 'Registration successful')
        self.assertEqual(response['user'], self.user_data_student)
        self.assertEqual(response['access_token'], 'access_token')


    @patch('app.managers.registration_manager.validate_university_data', return_value=True)
    @patch('app.managers.registration_manager.University.add')
    @patch('app.managers.registration_manager.hash_password', return_value='hashed_password')
    @patch('app.managers.registration_manager.create_access_token', return_value='access_token')
    def test_register_university_success(self, mock_create_access_token, mock_hash_password, mock_university_add, mock_validate_university_data):
        mock_university = MagicMock()
        mock_university.get_id.return_value = 1
        mock_university.to_dict.return_value = self.user_data_university
        mock_university_add.return_value = mock_university

        response = self.manager.register_university(self.user_data_university)

        self.assertEqual(response['message'], 'Registration successful')
        self.assertEqual(response['user'], self.user_data_university)
        self.assertEqual(response['access_token'], 'access_token')


    @patch('app.managers.registration_manager.validate_company_data', return_value=True)
    @patch('app.managers.registration_manager.Company.add')
    @patch('app.managers.registration_manager.hash_password', return_value='hashed_password')
    @patch('app.managers.registration_manager.create_access_token', return_value='access_token')
    def test_register_company_success(self, mock_create_access_token, mock_hash_password, mock_company_add, mock_validate_company_data):
        mock_company = MagicMock()
        mock_company.get_id.return_value = 1
        mock_company.to_dict.return_value = self.user_data_company
        mock_company_add.return_value = mock_company

        response = self.manager.register_company(self.user_data_company)

        self.assertEqual(response['message'], 'Registration successful')
        self.assertEqual(response['user'], self.user_data_company)
        self.assertEqual(response['access_token'], 'access_token')


if __name__ == '__main__':
    unittest.main()
"""