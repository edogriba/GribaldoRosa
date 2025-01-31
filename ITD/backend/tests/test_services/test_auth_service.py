import unittest
from unittest.mock import patch
from app.services.auth_service import *

class TestAuthService(unittest.TestCase):

    def test_is_string_valid(self):
        self.assertTrue(is_string_valid("test"))
        self.assertFalse(is_string_valid(123))


    def test_is_int_valid(self):
        self.assertTrue(is_int_valid(123))
        self.assertTrue(is_int_valid(0))
        self.assertTrue(is_int_valid(-123))
        self.assertFalse(is_int_valid("123"))
        self.assertFalse(is_int_valid("abc"))
        self.assertFalse(is_int_valid(123.45))


    def test_is_float_valid(self):
        self.assertTrue(is_float_valid(123.45))
        self.assertTrue(is_float_valid(0.0))
        self.assertTrue(is_float_valid(-123.45))
        self.assertFalse(is_float_valid(10))
        self.assertFalse(is_float_valid("123"))
        self.assertFalse(is_float_valid("abc"))
        self.assertFalse(is_float_valid("123.45"))


    @patch('app.models.User.is_email_unique')
    def test_is_email_unique(self, mock_is_email_unique):
        mock_is_email_unique.return_value = True
        self.assertTrue(is_email_unique("test@example.com"))
        mock_is_email_unique.return_value = False
        self.assertFalse(is_email_unique("test@example.com"))
        mock_is_email_unique.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            is_email_unique("test@example.com")
        self.assertEqual(str(context.exception), "Database error")


    def test_is_email_valid(self):
        self.assertTrue(is_email_valid("test@example.com"))
        self.assertFalse(is_email_valid("test@.com"))
        self.assertFalse(is_email_valid("test.com"))
        self.assertFalse(is_email_valid("test"))
        self.assertFalse(is_email_valid(""))
        self.assertFalse(is_email_valid(123))
        self.assertFalse(is_email_valid(None))


    def test_is_phoneNumber_valid(self):
        self.assertTrue(is_phoneNumber_valid("+1234567890"))
        self.assertTrue(is_phoneNumber_valid("1234567890"))
        self.assertTrue(is_phoneNumber_valid("123-456-7890"))
        self.assertTrue(is_phoneNumber_valid("123.456.7890"))
        self.assertTrue(is_phoneNumber_valid("123 456 7890"))
        self.assertTrue(is_phoneNumber_valid("123-4567890"))
        self.assertTrue(is_phoneNumber_valid("123.4567890"))
        self.assertTrue(is_phoneNumber_valid("123 4567890"))
        self.assertTrue(is_phoneNumber_valid("123456-7890"))
        self.assertTrue(is_phoneNumber_valid("123456.7890"))
        self.assertTrue(is_phoneNumber_valid("123456 7890"))
        self.assertFalse(is_phoneNumber_valid("12345"))
        self.assertFalse(is_phoneNumber_valid("12345678901234567890"))
        self.assertFalse(is_phoneNumber_valid("1234567890a"))
        self.assertFalse(is_phoneNumber_valid("1234567890!"))
        self.assertFalse(is_phoneNumber_valid("1234567890@"))
        self.assertFalse(is_phoneNumber_valid("1234567890#"))
        self.assertFalse(is_phoneNumber_valid("1234567890$"))
        self.assertFalse(is_phoneNumber_valid("1234567890%"))
        self.assertFalse(is_phoneNumber_valid("1234567890^"))
        self.assertFalse(is_phoneNumber_valid("1234567890&"))
        self.assertFalse(is_phoneNumber_valid("1234567890*"))
        self.assertFalse(is_phoneNumber_valid("1234567890("))
        self.assertFalse(is_phoneNumber_valid("1234567890)"))
        self.assertFalse(is_phoneNumber_valid("1234567890_"))
        self.assertFalse(is_phoneNumber_valid(None))
        self.assertFalse(is_phoneNumber_valid(1234567890))
        self.assertFalse(is_phoneNumber_valid(""))


    def test_is_password_valid(self):
        self.assertTrue(is_password_valid("Passwor23"))
        self.assertTrue(is_password_valid("Password1"))
        self.assertTrue(is_password_valid("Password1234567890"))
        self.assertTrue(is_password_valid("Password!@#$%^&*()1234567890"))
        self.assertFalse(is_password_valid("pass"))
        self.assertFalse(is_password_valid("password"))
        self.assertFalse(is_password_valid("PASSWORD"))
        self.assertFalse(is_password_valid("12345678"))
        self.assertFalse(is_password_valid("password123"))
        self.assertFalse(is_password_valid("password1234567890"))
        self.assertFalse(is_password_valid("password!@#$%^&*()"))
        self.assertFalse(is_password_valid("password!@#$%^&*()1234567890"))
        self.assertFalse(is_password_valid(None))
        self.assertFalse(is_password_valid(1234567890))
        self.assertFalse(is_password_valid(""))


    def test_is_url_valid(self):
        self.assertTrue(is_url_valid("http://example.com"))
        self.assertTrue(is_url_valid("https://example.com"))
        self.assertTrue(is_url_valid("http://www.example.com"))
        self.assertTrue(is_url_valid("https://www.example.com"))
        self.assertTrue(is_url_valid("http://example.com/"))
        self.assertTrue(is_url_valid("https://example.com/"))
        self.assertTrue(is_url_valid("http://www.example.com/"))
        self.assertTrue(is_url_valid("https://www.example.com/"))
        self.assertTrue(is_url_valid("http://example.com/page"))
        self.assertTrue(is_url_valid("https://example.com/page"))
        self.assertTrue(is_url_valid("http://www.example.com/page"))
        self.assertFalse(is_url_valid("example.com"))
        self.assertFalse(is_url_valid("www.example.com"))
        self.assertFalse(is_url_valid("example.com/"))
        self.assertFalse(is_url_valid("www.example.com/"))
        self.assertFalse(is_url_valid("example.com/page"))
        self.assertFalse(is_url_valid("www.example.com/page"))
        self.assertFalse(is_url_valid("example"))
        self.assertFalse(is_url_valid("www"))
        self.assertFalse(is_url_valid("example/page"))
        self.assertFalse(is_url_valid(None))
        self.assertFalse(is_url_valid(1234567890))
        self.assertFalse(is_url_valid(""))


    def test_is_location_valid(self):
        self.assertTrue(is_location_valid("New York, NY"))
        self.assertTrue(is_location_valid("Los Angeles, CA"))
        self.assertTrue(is_location_valid("San Francisco, CA"))
        self.assertTrue(is_location_valid("Chicago, IL"))
        self.assertTrue(is_location_valid("Miami, FL"))
        self.assertTrue(is_location_valid("Austin, TX"))
        self.assertTrue(is_location_valid("Seattle, WA"))
        self.assertTrue(is_location_valid("Boston, MA"))
        self.assertTrue(is_location_valid("Washington"))
        self.assertTrue(is_location_valid("London"))
        self.assertTrue(is_location_valid("Paris"))
        self.assertFalse(is_location_valid(""))
        self.assertFalse(is_location_valid("New York, NY" * 100))
        self.assertFalse(is_location_valid("New York, NY!"))
        self.assertFalse(is_location_valid("New York, NY@"))
        self.assertFalse(is_location_valid("New York, NY#"))
        self.assertFalse(is_location_valid("New York, NY$"))
        self.assertFalse(is_location_valid("New York, NY%"))
        self.assertFalse(is_location_valid("New York, NY^"))
        self.assertFalse(is_location_valid("New York, NY&"))
        self.assertFalse(is_location_valid("New York, NY*"))
        self.assertFalse(is_location_valid("New York, NY("))
        self.assertFalse(is_location_valid("New York, NY)"))
        self.assertFalse(is_location_valid(None))
        self.assertFalse(is_location_valid(1234567890))


    def test_is_description_valid(self):
        self.assertTrue(is_description_valid("This is a description."))
        self.assertTrue(is_description_valid("This is a description. " * 50))
        self.assertTrue(is_description_valid("This is a description. " * 70))
        self.assertTrue(is_description_valid("This is a description. " * 80))
        self.assertFalse(is_description_valid("This is a description. " * 90))
        self.assertFalse(is_description_valid(""))
        self.assertFalse(is_description_valid(None))
        self.assertFalse(is_description_valid(1234567890))


    def test_is_name_valid(self):
        self.assertTrue(is_name_valid("John Doe"))
        self.assertTrue(is_name_valid("John"))
        self.assertTrue(is_name_valid("John Doe" * 10))
        self.assertFalse(is_name_valid("John Doe!"))
        self.assertFalse(is_name_valid("John123"))
        self.assertFalse(is_name_valid("John!@#$%^&*()"))
        self.assertFalse(is_name_valid("John Doe" * 100))
        self.assertFalse(is_name_valid(""))
        self.assertFalse(is_name_valid(None))
        self.assertFalse(is_name_valid(1234567890))


    def test_is_degreeProgram_valid(self):
        self.assertTrue(is_degreeProgram_valid("Computer Science"))
        self.assertTrue(is_degreeProgram_valid("Computer Science" * 10))
        self.assertTrue(is_degreeProgram_valid("Mechanical Engineering"))
        self.assertTrue(is_degreeProgram_valid("Electrical Engineering"))
        self.assertTrue(is_degreeProgram_valid("Civil Engineering"))
        self.assertTrue(is_degreeProgram_valid("Biomedical Engineering"))
        self.assertTrue(is_degreeProgram_valid("Chemical Engineering"))
        self.assertTrue(is_degreeProgram_valid("Aerospace Engineering"))
        self.assertTrue(is_degreeProgram_valid("Environmental Engineering"))
        self.assertTrue(is_degreeProgram_valid("Industrial Engineering"))
        self.assertTrue(is_degreeProgram_valid("Software Engineering"))
        self.assertTrue(is_degreeProgram_valid("Data Science"))
        self.assertFalse(is_degreeProgram_valid("Computer Science!"))
        self.assertFalse(is_degreeProgram_valid(""))
        self.assertFalse(is_degreeProgram_valid(None))
        self.assertFalse(is_degreeProgram_valid(1234567890))


    def test_is_gpa_valid(self):
        self.assertTrue(is_gpa_valid(3.5))
        self.assertTrue(is_gpa_valid(4.0))
        self.assertTrue(is_gpa_valid(0.0))
        self.assertTrue(is_gpa_valid(None))
        self.assertFalse(is_gpa_valid(5.0))
        self.assertFalse(is_gpa_valid(-1.0))
        self.assertFalse(is_gpa_valid("3.5"))
        self.assertFalse(is_gpa_valid(""))
        self.assertFalse(is_gpa_valid(1234567890))
        self.assertFalse(is_gpa_valid("abc"))
        self.assertFalse(is_gpa_valid("3.5a"))
        self.assertFalse(is_gpa_valid(" "))


    def test_is_graduationYear_valid(self):
        self.assertTrue(is_graduationYear_valid(2021))
        self.assertTrue(is_graduationYear_valid(2023))
        self.assertTrue(is_graduationYear_valid(2025))
        self.assertTrue(is_graduationYear_valid(None))
        self.assertFalse(is_graduationYear_valid(2026))
        self.assertFalse(is_graduationYear_valid(1800))
        self.assertFalse(is_graduationYear_valid("2021"))
        self.assertFalse(is_graduationYear_valid(""))
        self.assertFalse(is_graduationYear_valid(1234567890))
        self.assertFalse(is_graduationYear_valid("abc"))
        self.assertFalse(is_graduationYear_valid("2021a"))


    def test_is_path_valid(self):
        self.assertTrue(is_path_valid("/valid/path"))
        self.assertTrue(is_path_valid("/valid/path/"))
        self.assertTrue(is_path_valid("/valid/path/to"))
        self.assertTrue(is_path_valid("/valid/path/to/"))
        self.assertTrue(is_path_valid("/valid/path/to/file"))
        self.assertTrue(is_path_valid("/valid/path/to/file/"))
        self.assertFalse(is_path_valid("invalid/path"))
        self.assertFalse(is_path_valid("invalid/path/"))
        self.assertFalse(is_path_valid("invalid/path/to"))
        self.assertFalse(is_path_valid("invalid/path/to/"))
        self.assertFalse(is_path_valid(""))
        self.assertFalse(is_path_valid(None))
        self.assertFalse(is_path_valid(1234567890))
        self.assertFalse(is_path_valid("abc"))


    def test_is_optional_path_valid(self):
        self.assertTrue(is_optional_path_valid(""))
        self.assertTrue(is_optional_path_valid(None))
        self.assertTrue(is_optional_path_valid("valid_filename.txt"))
        self.assertTrue(is_optional_path_valid("valid-file_name.txt"))
        self.assertTrue(is_optional_path_valid("valid file name.txt"))
        self.assertTrue(is_optional_path_valid("valid-file-name-123.txt"))
        self.assertTrue(is_optional_path_valid("valid.file.name.txt"))
        self.assertTrue(is_optional_path_valid("valid_filename" * 50 + ".txt"))
        self.assertFalse(is_optional_path_valid("invalid/filename.txt"))
        self.assertFalse(is_optional_path_valid("invalid\\filename.txt"))
        self.assertFalse(is_optional_path_valid("invalid:filename.txt"))
        self.assertFalse(is_optional_path_valid("invalid*filename.txt"))
        self.assertFalse(is_optional_path_valid("invalid?filename.txt"))
        self.assertFalse(is_optional_path_valid("invalid\"filename.txt"))
        self.assertFalse(is_optional_path_valid("invalid<filename.txt"))
        self.assertFalse(is_optional_path_valid("invalid>filename.txt"))
        self.assertFalse(is_optional_path_valid("invalid|filename.txt"))
        self.assertFalse(is_optional_path_valid("invalid filename" * 100 + ".txt"))
        self.assertFalse(is_optional_path_valid(1234567890))
        self.assertFalse(is_optional_path_valid(" "))


    def test_is_skills_valid(self):
        self.assertTrue(is_skills_valid("Python, Java"))
        self.assertTrue(is_skills_valid("Python, Java, C++"))
        self.assertTrue(is_skills_valid("Python, Java, C++, SQL"))
        self.assertTrue(is_skills_valid("Python, Java, C++, SQL, HTML5"))
        self.assertTrue(is_skills_valid("Python, Java, C++, SQL, HTML, CSS"))
        self.assertTrue(is_skills_valid("Python, Java, C++, SQL, HTML, CSS, JavaScript"))
        self.assertTrue(is_skills_valid("Python, Java, C++, SQL, HTML, CSS, JavaScript, React"))
        self.assertTrue(is_skills_valid("Python, Java, C++, SQL, HTML, CSS, JavaScript, React, Angular"))
        self.assertTrue(is_skills_valid("Python, Java, C++, SQL, HTML, CSS, JavaScript, React, Angular, Node.js"))
        self.assertTrue(is_skills_valid("Python, Java, C++, SQL, HTML, CSS, JavaScript, React, Angular, Node.js, Express"))
        self.assertTrue(is_skills_valid("Python, Java, C++, SQL, HTML, CSS, JavaScript, React, Angular, Node.js, Express, MongoDB"))
        self.assertTrue(is_skills_valid("Python, Java, C++, SQL, HTML, CSS, JavaScript, React, Angular, Node.js, Express, MongoDB, Firebase"))
        self.assertTrue(is_skills_valid("Python, Java, C++, SQL, HTML, CSS, JavaScript, React, Angular, Node.js, Express, MongoDB, Firebase, AWS"))
        self.assertTrue(is_skills_valid("Python, Java, C++, SQL, HTML, CSS, JavaScript, React, Angular, Node.js, Express, MongoDB, Firebase, AWS, Docker"))
        self.assertTrue(is_skills_valid("Python, Java, C++, SQL, HTML, CSS, JavaScript, React, Angular, Node.js, Express, MongoDB, Firebase, AWS, Docker, Kubernetes"))
        self.assertTrue(is_skills_valid("Python, Java, C++, SQL, HTML, CSS, JavaScript, React, Angular, Node.js, Express, MongoDB, Firebase, AWS, Docker, Kubernetes, Jenkins"))
        self.assertFalse(is_skills_valid(""))
        self.assertFalse(is_skills_valid(None))
        self.assertFalse(is_skills_valid(1234567890))


    def test_is_userType_valid(self):
        self.assertTrue(is_userType_valid("student"))
        self.assertTrue(is_userType_valid("university"))
        self.assertTrue(is_userType_valid("company"))
        self.assertFalse(is_userType_valid("invalid"))
        self.assertFalse(is_userType_valid(""))
        self.assertFalse(is_userType_valid(None))
        self.assertFalse(is_userType_valid(1234567890))


    def test_is_languageSpoken_valid(self):
        self.assertTrue(is_languageSpoken_valid("English"))
        self.assertTrue(is_languageSpoken_valid("English, Spanish"))
        self.assertTrue(is_languageSpoken_valid("English, Spanish, French"))
        self.assertTrue(is_languageSpoken_valid("English, Spanish, French, German"))
        self.assertTrue(is_languageSpoken_valid("English, Spanish, French, German, Italian"))
        self.assertTrue(is_languageSpoken_valid("English, Spanish, French, German, Italian, Portuguese"))
        self.assertFalse(is_languageSpoken_valid(""))
        self.assertFalse(is_languageSpoken_valid(None))
        self.assertFalse(is_languageSpoken_valid(1234567890))
        self.assertFalse(is_languageSpoken_valid("English; Spanish"))


    def test_is_id_valid(self):
        self.assertTrue(is_id_valid(123))
        self.assertTrue(is_id_valid(0))
        self.assertFalse(is_id_valid(-123))
        self.assertFalse(is_id_valid("123"))
        self.assertFalse(is_id_valid("abc"))
        self.assertFalse(is_id_valid(123.45))
        self.assertFalse(is_id_valid(None))
        self.assertFalse(is_id_valid(""))
        self.assertFalse(is_id_valid(" "))
        self.assertFalse(is_id_valid("123a"))


    def test_is_duration_valid(self):
        self.assertTrue(is_duration_valid(6))
        self.assertTrue(is_duration_valid(12))
        self.assertTrue(is_duration_valid(3))
        self.assertFalse(is_duration_valid(0))
        self.assertFalse(is_duration_valid(13))
        self.assertFalse(is_duration_valid("6"))
        self.assertFalse(is_duration_valid("abc"))
        self.assertFalse(is_duration_valid(123.45))
        self.assertFalse(is_duration_valid(None))
        self.assertFalse(is_duration_valid(""))
        self.assertFalse(is_duration_valid(" "))


    def test_is_compensation_valid(self):
        self.assertTrue(is_compensation_valid(1000))
        self.assertTrue(is_compensation_valid(0))
        self.assertTrue(is_compensation_valid(None))
        self.assertFalse(is_compensation_valid(-100))
        self.assertFalse(is_compensation_valid("1000"))
        self.assertFalse(is_compensation_valid("abc"))
        self.assertFalse(is_compensation_valid(123.45))
        self.assertFalse(is_compensation_valid(""))
        self.assertFalse(is_compensation_valid(" "))



    def test_is_benefits_valid(self):
        self.assertTrue(is_benefits_valid("Health insurance, 401k"))
        self.assertTrue(is_benefits_valid("Health insurance, 401k, Paid time off"))
        self.assertTrue(is_benefits_valid("Health insurance, 401k, Paid time off, Tuition reimbursement"))
        self.assertTrue(is_benefits_valid(None))
        self.assertFalse(is_benefits_valid(""))
        self.assertFalse(is_benefits_valid(123))
        self.assertFalse(is_benefits_valid(" "))


if __name__ == '__main__':
    unittest.main()