"""
import unittest
from flask_jwt_extended import create_access_token
from unittest.mock import patch, MagicMock
from app.managers.login_manager import LoginManager
from app.utils import json_success, json_invalid_request, json_unauthorized
from app.models import User, Student, University, Company


class TestLoginManager(unittest.TestCase):

    def setUp(self):
        self.login_manager = LoginManager()
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
            'universityId': 1
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



    @patch.object(LoginManager, 'get_user_by_email', return_value=Student(**self.user_data_student))
    @patch.object(LoginManager, 'verify_password', return_value=True)
    @patch.object(LoginManager, 'create_access_token', return_value='access_token')
    def test_login_success_with_patch_object(self, mock_create_access_token, mock_verify_password, mock_get_user_by_email):
        user_data = {'email': 'test@example.com', 'password': 'password123'}
        
        response = self.login_manager.login(user_data)

        self.assertEqual(response, json_success("Login successful", user=mock_get_user_by_email.return_value, access_token='access_token'))
        mock_get_user_by_email.assert_called_once_with('test@example.com')
        mock_verify_password.assert_called_once_with('password123', 'hashed_password')
        mock_create_access_token.assert_called_once_with(identity={'id': 1})


    def test_login_missing_email(self):
        user_data = {'password': 'password123'}
        response = self.login_manager.login(user_data)
        self.assertEqual(response, json_invalid_request("Email and password are required."))


    def test_login_missing_password(self):
        user_data = {'email': 'test@example.com'}
        response = self.login_manager.login(user_data)
        self.assertEqual(response, json_invalid_request("Email and password are required."))


    @patch('app.managers.login_manager.LoginManager.get_user_by_email')
    def test_login_invalid_email(self, mock_get_user_by_email):
        user_data = {'email': 'test@example.com', 'password': 'password123'}
        mock_get_user_by_email.return_value = None

        response = self.login_manager.login(user_data)
        self.assertEqual(response, json_unauthorized("Invalid email or password."))
        mock_get_user_by_email.assert_called_once_with('test@example.com')


    @patch('...app.managers.login_manager.LoginManager.get_user_by_email')
    @patch('...app.managers.login_manager.verify_password')
    def test_login_invalid_password(self, mock_verify_password, mock_get_user_by_email):
        user_data = {'email': 'test@example.com', 'password': 'password123'}
        mock_user = MagicMock()
        mock_user.get_password.return_value = 'hashed_password'

        mock_get_user_by_email.return_value = mock_user
        mock_verify_password.return_value = False

        response = self.login_manager.login(user_data)
        self.assertEqual(response, json_unauthorized("Invalid email or password."))
        mock_get_user_by_email.assert_called_once_with('test@example.com')
        mock_verify_password.assert_called_once_with('password123', 'hashed_password')


    def test_logout_success(self):
        response = self.login_manager.logout()
        self.assertEqual(response, json_success("Logout successful", logout=True))


if __name__ == '__main__':
    unittest.main()
"""