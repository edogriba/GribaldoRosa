import unittest
from unittest.mock import patch
from app.models import Student
from app.db.dbModels import StudentDB


class TestStudentModel(unittest.TestCase):

    def setUp(self):
        self.student1 = Student(
            id=1,
            email="test1@student.com",
            password="password123",
            firstName="Test1",
            lastName="Student1",
            phoneNumber="1234567890",
            profilePicture="/path/to/profile1.png",
            location="Location1",
            universityId=1,
            degreeProgram="Computer Science",
            GPA=3.5,
            graduationYear=2023,
            skills="Python, Java",
            CV="path/to/cv1",
            languageSpoken="English"
        )

        self.student2 = Student(
            id=2,
            email="test2@student.com",
            password="password456",
            firstName="Test2",
            lastName="Student2",
            phoneNumber="0987654321",
            profilePicture=None,
            location="Location2",
            universityId=2,
            degreeProgram="Software Engineering",
            GPA=3.8,
            graduationYear=2024,
            skills="C++, JavaScript",
            CV="path/to/cv2",
            languageSpoken="Spanish"
        )

        self.student3 = Student(
            id=3,
            email="test3@student.com",
            password="password789",
            firstName="Test3",
            lastName="Student3",
            phoneNumber="1122334455",
            profilePicture="/path/to/profile3.png",
            location="Location3",
            universityId=3,
            degreeProgram="Information Technology",
            GPA=None,
            graduationYear=2025,
            skills="Ruby, Go",
            CV="path/to/cv3",
            languageSpoken="French"
        )

        self.student4 = Student(
            id=4,
            email="test4@student.com",
            password="password012",
            firstName="Test4",
            lastName="Student4",
            phoneNumber="5566778899",
            profilePicture="/path/to/profile4.png",
            location="Location4",
            universityId=4,
            degreeProgram="Data Science",
            GPA=3.0,
            graduationYear=None,
            skills="SQL, R",
            CV="path/to/cv4",
            languageSpoken="German"
        )

        self.student5 = Student(
            id=5,
            email="test5@student.com",
            password="password345",
            firstName="Test5",
            lastName="Student5",
            phoneNumber="6677889900",
            profilePicture=None,
            location="Location5",
            universityId=5,
            degreeProgram="Cyber Security",
            GPA=None,
            graduationYear=2027,
            skills="Kotlin, Swift",
            CV="path/to/cv5",
            languageSpoken="Italian"
        )

        self.student6 = Student(
            id=6,
            email="test6@student.com",
            password="password678",
            firstName="Test6",
            lastName="Student6",
            phoneNumber="7788990011",
            profilePicture=None,
            location="Location6",
            universityId=6,
            degreeProgram="Artificial Intelligence",
            GPA=3.7,
            graduationYear=None,
            skills="Perl, Rust",
            CV="path/to/cv6",
            languageSpoken="Portuguese"
        )

        self.student7 = Student(
            id=7,
            email="test7@student.com",
            password="password901",
            firstName="Test7",
            lastName="Student7",
            phoneNumber="8899001122",
            profilePicture="/path/to/profile7.png",
            location="Location7",
            universityId=7,
            degreeProgram="Robotics",
            GPA=None,
            graduationYear=None,
            skills="Scala, Haskell",
            CV="path/to/cv7",
            languageSpoken="Dutch"
        )

        self.student8 = Student(
            id=8,
            email="test8@student.com",
            password="password234",
            firstName="Test8",
            lastName="Student8",
            phoneNumber="9900112233",
            profilePicture=None,
            location="Location8",
            universityId=8,
            degreeProgram="Quantum Computing",
            GPA=None,
            graduationYear=None,
            skills="Lisp, Prolog",
            CV="path/to/cv8",
            languageSpoken="Russian"
        )


    def test_get_id(self):
        self.assertEqual(self.student1.get_id(), 1)
        self.assertEqual(self.student2.get_id(), 2)
        self.assertEqual(self.student3.get_id(), 3)
        self.assertEqual(self.student4.get_id(), 4)
        self.assertEqual(self.student5.get_id(), 5)
        self.assertEqual(self.student6.get_id(), 6)
        self.assertEqual(self.student7.get_id(), 7)
        self.assertEqual(self.student8.get_id(), 8)
    

    def test_get_email(self):
        self.assertEqual(self.student1.get_email(), "test1@student.com")
        self.assertEqual(self.student2.get_email(), "test2@student.com")
        self.assertEqual(self.student3.get_email(), "test3@student.com")
        self.assertEqual(self.student4.get_email(), "test4@student.com")
        self.assertEqual(self.student5.get_email(), "test5@student.com")
        self.assertEqual(self.student6.get_email(), "test6@student.com")
        self.assertEqual(self.student7.get_email(), "test7@student.com")
        self.assertEqual(self.student8.get_email(), "test8@student.com")


    def test_get_password(self):
        self.assertEqual(self.student1.get_password(), "password123")
        self.assertEqual(self.student2.get_password(), "password456")
        self.assertEqual(self.student3.get_password(), "password789")
        self.assertEqual(self.student4.get_password(), "password012")
        self.assertEqual(self.student5.get_password(), "password345")
        self.assertEqual(self.student6.get_password(), "password678")
        self.assertEqual(self.student7.get_password(), "password901")
        self.assertEqual(self.student8.get_password(), "password234")
    

    def test_get_type(self):
        self.assertEqual(self.student1.get_type(), "student")
        self.assertEqual(self.student2.get_type(), "student")
        self.assertEqual(self.student3.get_type(), "student")
        self.assertEqual(self.student4.get_type(), "student")
        self.assertEqual(self.student5.get_type(), "student")
        self.assertEqual(self.student6.get_type(), "student")
        self.assertEqual(self.student7.get_type(), "student")
        self.assertEqual(self.student8.get_type(), "student")


    def test_get_firstName(self):
        self.assertEqual(self.student1.get_firstName(), "Test1")
        self.assertEqual(self.student2.get_firstName(), "Test2")
        self.assertEqual(self.student3.get_firstName(), "Test3")
        self.assertEqual(self.student4.get_firstName(), "Test4")
        self.assertEqual(self.student5.get_firstName(), "Test5")
        self.assertEqual(self.student6.get_firstName(), "Test6")
        self.assertEqual(self.student7.get_firstName(), "Test7")
        self.assertEqual(self.student8.get_firstName(), "Test8")


    def test_get_lastName(self):
        self.assertEqual(self.student1.get_lastName(), "Student1")
        self.assertEqual(self.student2.get_lastName(), "Student2")
        self.assertEqual(self.student3.get_lastName(), "Student3")
        self.assertEqual(self.student4.get_lastName(), "Student4")
        self.assertEqual(self.student5.get_lastName(), "Student5")
        self.assertEqual(self.student6.get_lastName(), "Student6")
        self.assertEqual(self.student7.get_lastName(), "Student7")
        self.assertEqual(self.student8.get_lastName(), "Student8")


    def test_get_phoneNumber(self):
        self.assertEqual(self.student1.get_phoneNumber(), "1234567890")
        self.assertEqual(self.student2.get_phoneNumber(), "0987654321")
        self.assertEqual(self.student3.get_phoneNumber(), "1122334455")
        self.assertEqual(self.student4.get_phoneNumber(), "5566778899")
        self.assertEqual(self.student5.get_phoneNumber(), "6677889900")
        self.assertEqual(self.student6.get_phoneNumber(), "7788990011")
        self.assertEqual(self.student7.get_phoneNumber(), "8899001122")
        self.assertEqual(self.student8.get_phoneNumber(), "9900112233")


    def test_get_profilePicture(self):
        self.assertEqual(self.student1.get_profilePicture(), "/path/to/profile1.png")
        self.assertIsNone(self.student2.get_profilePicture())
        self.assertEqual(self.student3.get_profilePicture(), "/path/to/profile3.png")
        self.assertEqual(self.student4.get_profilePicture(), "/path/to/profile4.png")
        self.assertIsNone(self.student5.get_profilePicture())
        self.assertIsNone(self.student6.get_profilePicture())
        self.assertEqual(self.student7.get_profilePicture(), "/path/to/profile7.png")
        self.assertIsNone(self.student8.get_profilePicture())

    
    def test_get_location(self):
        self.assertEqual(self.student1.get_location(), "Location1")
        self.assertEqual(self.student2.get_location(), "Location2")
        self.assertEqual(self.student3.get_location(), "Location3")
        self.assertEqual(self.student4.get_location(), "Location4")
        self.assertEqual(self.student5.get_location(), "Location5")
        self.assertEqual(self.student6.get_location(), "Location6")
        self.assertEqual(self.student7.get_location(), "Location7")
        self.assertEqual(self.student8.get_location(), "Location8")


    def test_get_universityId(self):   
        self.assertEqual(self.student1.get_universityId(), 1)
        self.assertEqual(self.student2.get_universityId(), 2)
        self.assertEqual(self.student3.get_universityId(), 3)
        self.assertEqual(self.student4.get_universityId(), 4)
        self.assertEqual(self.student5.get_universityId(), 5)
        self.assertEqual(self.student6.get_universityId(), 6)
        self.assertEqual(self.student7.get_universityId(), 7)
        self.assertEqual(self.student8.get_universityId(), 8)


    def test_get_degreeProgram(self):
        self.assertEqual(self.student1.get_degreeProgram(), "Computer Science")
        self.assertEqual(self.student2.get_degreeProgram(), "Software Engineering")
        self.assertEqual(self.student3.get_degreeProgram(), "Information Technology")
        self.assertEqual(self.student4.get_degreeProgram(), "Data Science")
        self.assertEqual(self.student5.get_degreeProgram(), "Cyber Security")
        self.assertEqual(self.student6.get_degreeProgram(), "Artificial Intelligence")
        self.assertEqual(self.student7.get_degreeProgram(), "Robotics")
        self.assertEqual(self.student8.get_degreeProgram(), "Quantum Computing")


    def test_get_gpa(self):
        self.assertEqual(self.student1.get_gpa(), 3.5)
        self.assertEqual(self.student2.get_gpa(), 3.8)
        self.assertIsNone(self.student3.get_gpa())
        self.assertEqual(self.student4.get_gpa(), 3.0)
        self.assertIsNone(self.student5.get_gpa())
        self.assertEqual(self.student6.get_gpa(), 3.7)
        self.assertIsNone(self.student7.get_gpa())
        self.assertIsNone(self.student8.get_gpa())


    def test_get_graduationYear(self):
        self.assertEqual(self.student1.get_graduationYear(), 2023)
        self.assertEqual(self.student2.get_graduationYear(), 2024)
        self.assertEqual(self.student3.get_graduationYear(), 2025)
        self.assertIsNone(self.student4.get_graduationYear())
        self.assertEqual(self.student5.get_graduationYear(), 2027)
        self.assertIsNone(self.student6.get_graduationYear())
        self.assertIsNone(self.student7.get_graduationYear())
        self.assertIsNone(self.student8.get_graduationYear())


    def test_get_skills(self):
        self.assertEqual(self.student1.get_skills(), "Python, Java")
        self.assertEqual(self.student2.get_skills(), "C++, JavaScript")
        self.assertEqual(self.student3.get_skills(), "Ruby, Go")
        self.assertEqual(self.student4.get_skills(), "SQL, R")
        self.assertEqual(self.student5.get_skills(), "Kotlin, Swift")
        self.assertEqual(self.student6.get_skills(), "Perl, Rust")
        self.assertEqual(self.student7.get_skills(), "Scala, Haskell")
        self.assertEqual(self.student8.get_skills(), "Lisp, Prolog")

    
    def test_get_cv(self):
        self.assertEqual(self.student1.get_cv(), "path/to/cv1")
        self.assertEqual(self.student2.get_cv(), "path/to/cv2")
        self.assertEqual(self.student3.get_cv(), "path/to/cv3")
        self.assertEqual(self.student4.get_cv(), "path/to/cv4")
        self.assertEqual(self.student5.get_cv(), "path/to/cv5")
        self.assertEqual(self.student6.get_cv(), "path/to/cv6")
        self.assertEqual(self.student7.get_cv(), "path/to/cv7")
        self.assertEqual(self.student8.get_cv(), "path/to/cv8")

    
    def test_get_languageSpoken(self):
        self.assertEqual(self.student1.get_languageSpoken(), "English")
        self.assertEqual(self.student2.get_languageSpoken(), "Spanish")
        self.assertEqual(self.student3.get_languageSpoken(), "French")
        self.assertEqual(self.student4.get_languageSpoken(), "German")
        self.assertEqual(self.student5.get_languageSpoken(), "Italian")
        self.assertEqual(self.student6.get_languageSpoken(), "Portuguese")
        self.assertEqual(self.student7.get_languageSpoken(), "Dutch")
        self.assertEqual(self.student8.get_languageSpoken(), "Russian")

    
    def test_to_dict(self):
        student_dict = self.student1.to_dict()
        expected_dict = {
            'id': 1,
            'email': "test1@student.com",
            'type': "student",
            'firstName': "Test1",
            'lastName': "Student1",
            'phoneNumber': "1234567890",
            'profilePicture': "/path/to/profile1.png",
            'location': "Location1",
            'universityId': 1,
            'degreeProgram': "Computer Science",
            'GPA': 3.5,
            'graduationYear': 2023,
            'skills': "Python, Java",
            'CV': "path/to/cv1",
            'languageSpoken': "English"
        }
        self.assertEqual(student_dict, expected_dict)

        student_dict = self.student2.to_dict()
        expected_dict = {
            'id': 2,
            'email': "test2@student.com",
            'type': "student",
            'firstName': "Test2",
            'lastName': "Student2",
            'phoneNumber': "0987654321",
            'profilePicture': None,
            'location': "Location2",
            'universityId': 2,
            'degreeProgram': "Software Engineering",
            'GPA': 3.8,
            'graduationYear': 2024,
            'skills': "C++, JavaScript",
            'CV': "path/to/cv2",
            'languageSpoken': "Spanish"
        }
        self.assertEqual(student_dict, expected_dict)

        student_dict = self.student3.to_dict()
        expected_dict = {
            'id': 3,
            'email': "test3@student.com",
            'type': "student",
            'firstName': "Test3",
            'lastName': "Student3",
            'phoneNumber': "1122334455",
            'profilePicture': "/path/to/profile3.png",
            'location': "Location3",
            'universityId': 3,
            'degreeProgram': "Information Technology",
            'GPA': None,
            'graduationYear': 2025,
            'skills': "Ruby, Go",
            'CV': "path/to/cv3",
            'languageSpoken': "French"
        }
        self.assertEqual(student_dict, expected_dict)

        student_dict = self.student4.to_dict()
        expected_dict = {
            'id': 4,
            'email': "test4@student.com",
            'type': "student",
            'firstName': "Test4",
            'lastName': "Student4",
            'phoneNumber': "5566778899",
            'profilePicture': "/path/to/profile4.png",
            'location': "Location4",
            'universityId': 4,
            'degreeProgram': "Data Science",
            'GPA': 3.0,
            'graduationYear': None,
            'skills': "SQL, R",
            'CV': "path/to/cv4",
            'languageSpoken': "German"
        }
        self.assertEqual(student_dict, expected_dict)

        student_dict = self.student5.to_dict()
        expected_dict = {
            'id': 5,
            'email': "test5@student.com",
            'type': "student",
            'firstName': "Test5",
            'lastName': "Student5",
            'phoneNumber': "6677889900",
            'profilePicture': None,
            'location': "Location5",
            'universityId': 5,
            'degreeProgram': "Cyber Security",
            'GPA': None,
            'graduationYear': 2027,
            'skills': "Kotlin, Swift",
            'CV': "path/to/cv5",
            'languageSpoken': "Italian"
        }
        self.assertEqual(student_dict, expected_dict)

        student_dict = self.student6.to_dict()
        expected_dict = {
            'id': 6,
            'email': "test6@student.com",
            'type': "student",
            'firstName': "Test6",
            'lastName': "Student6",
            'phoneNumber': "7788990011",
            'profilePicture': None,
            'location': "Location6",
            'universityId': 6,
            'degreeProgram': "Artificial Intelligence",
            'GPA': 3.7,
            'graduationYear': None,
            'skills': "Perl, Rust",
            'CV': "path/to/cv6",
            'languageSpoken': "Portuguese"
        }
        self.assertEqual(student_dict, expected_dict)

        student_dict = self.student7.to_dict()
        expected_dict = {
            'id': 7,
            'email': "test7@student.com",
            'type': "student",
            'firstName': "Test7",
            'lastName': "Student7",
            'phoneNumber': "8899001122",
            'profilePicture': "/path/to/profile7.png",
            'location': "Location7",
            'universityId': 7,
            'degreeProgram': "Robotics",
            'GPA': None,
            'graduationYear': None,
            'skills': "Scala, Haskell",
            'CV': "path/to/cv7",
            'languageSpoken': "Dutch"
        }
        self.assertEqual(student_dict, expected_dict)

        student_dict = self.student8.to_dict()
        expected_dict = {
            'id': 8,
            'email': "test8@student.com",
            'type': "student",
            'firstName': "Test8",
            'lastName': "Student8",
            'phoneNumber': "9900112233",
            'profilePicture': None,
            'location': "Location8",
            'universityId': 8,
            'degreeProgram': "Quantum Computing",
            'GPA': None,
            'graduationYear': None,
            'skills': "Lisp, Prolog",
            'CV': "path/to/cv8",
            'languageSpoken': "Russian"
        }
        self.assertEqual(student_dict, expected_dict)


    @patch.object(StudentDB, 'insert', return_value=1)
    @patch.object(StudentDB, 'close')
    def test_add_student(self, mock_close, mock_insert):
        student = Student.add(
            email="test@student.com",
            password="password123",
            firstName="Test",
            lastName="Student",
            phoneNumber="1234567890",
            profilePicturePath=None,
            location="Test Location",
            degreeProgram="Computer Science",
            gpa=3.5,
            graduationYear=2023,
            CVpath="path/to/cv",
            skills="Python, Java",
            languageSpoken="English",
            universityId=1
        )
        self.assertIsInstance(student, Student)
        self.assertEqual(student.id, 1)
        self.assertEqual(student.email, "test@student.com")
        self.assertEqual(student.firstName, "Test")
        self.assertEqual(student.lastName, "Student")
        mock_insert.assert_called_once()
        mock_close.assert_called_once()

    
    @patch.object(StudentDB, 'insert', return_value=None)
    @patch.object(StudentDB, 'close')
    def test_add_student_failed(self, mock_close, mock_insert):
        student = Student.add(
            email="test@student.com",
            password="password123",
            firstName="Test",
            lastName="Student",
            phoneNumber="1234567890",
            profilePicturePath=None,
            location="Test Location",
            degreeProgram="Computer Science",
            gpa=3.5,
            graduationYear=2023,
            CVpath="path/to/cv",
            skills="Python, Java",
            languageSpoken="English",
            universityId=1
        )
        self.assertIsNone(student)
        mock_insert.assert_called_once()
        mock_close.assert_called_once()

    @patch.object(StudentDB, 'insert', side_effect=Exception("Database error"))
    @patch.object(StudentDB, 'close')
    def test_add_student_exception(self, mock_close, mock_insert):
        with self.assertRaises(Exception) as context:
            Student.add(
                email="test@student.com",
                password="password123",
                firstName="Test",
                lastName="Student",
                phoneNumber="1234567890",
                profilePicturePath=None,
                location="Test Location",
                degreeProgram="Computer Science",
                gpa=3.5,
                graduationYear=2023,
                CVpath="path/to/cv",
                skills="Python, Java",
                languageSpoken="English",
                universityId=1
            )
        self.assertTrue("Database error" in str(context.exception))
        mock_insert.assert_called_once()
        mock_close.assert_called_once()


    @patch.object(StudentDB, 'get_by_id', return_value={
        'id': 1,
        'email': "test@student.com",
        'password': "password123",
        'firstName': "Test",
        'lastName': "Student",
        'phoneNumber': "1234567890",
        'profilePicture': None,
        'location': "Test Location",
        'universityId': 1,
        'degreeProgram': "Computer Science",
        'GPA': 3.5,
        'graduationYear': 2023,
        'skills': "Python, Java",
        'CV': "path/to/cv",
        'languageSpoken': "English"
    })
    @patch.object(StudentDB, 'close')
    def test_get_student_by_id(self, mock_close, mock_get_by_id):
        student = Student.get_by_id(1)
        self.assertIsInstance(student, Student)
        self.assertEqual(student.id, 1)
        self.assertEqual(student.email, "test@student.com")
        self.assertEqual(student.firstName, "Test")
        self.assertEqual(student.lastName, "Student")
        mock_get_by_id.assert_called_once_with(1)
        mock_close.assert_called_once()


    @patch.object(StudentDB, 'get_by_id', return_value=None)
    @patch.object(StudentDB, 'close')
    def test_get_student_by_id_not_found(self, mock_close, mock_get_by_id):
        student = Student.get_by_id(999)
        self.assertIsNone(student)
        mock_get_by_id.assert_called_once_with(999)
        mock_close.assert_called_once()


    @patch.object(StudentDB, 'get_by_id', side_effect=Exception("Database error"))
    @patch.object(StudentDB, 'close')
    def test_get_student_by_id_exception(self, mock_close, mock_get_by_id):
        with self.assertRaises(Exception) as context:
            Student.get_by_id(1)
        self.assertTrue("Database error" in str(context.exception))
        mock_get_by_id.assert_called_once_with(1)
        mock_close.assert_called_once()


    @patch.object(StudentDB, 'get_by_email', return_value={
        'id': 1,
        'email': "test@student.com",
        'password': "password123",
        'firstName': "Test",
        'lastName': "Student",
        'phoneNumber': "1234567890",
        'profilePicture': None,
        'location': "Test Location",
        'universityId': 1,
        'degreeProgram': "Computer Science",
        'GPA': 3.5,
        'graduationYear': 2023,
        'skills': "Python, Java",
        'CV': "path/to/cv",
        'languageSpoken': "English"
    })
    @patch.object(StudentDB, 'close')
    def test_get_student_by_email(self, mock_close, mock_get_by_email):
        student = Student.get_by_email("test@student.com")
        self.assertIsInstance(student, Student)
        self.assertEqual(student.id, 1)
        self.assertEqual(student.email, "test@student.com")
        self.assertEqual(student.firstName, "Test")
        self.assertEqual(student.lastName, "Student")
        mock_get_by_email.assert_called_once_with("test@student.com")
        mock_close.assert_called_once()


    @patch.object(StudentDB, 'get_by_email', return_value=None)
    @patch.object(StudentDB, 'close')
    def test_get_student_by_email_not_found(self, mock_close, mock_get_by_email):
        student = Student.get_by_email("nonexistent@student.com")
        self.assertIsNone(student)
        mock_get_by_email.assert_called_once_with("nonexistent@student.com")
        mock_close.assert_called_once()

    
    @patch.object(StudentDB, 'get_by_email', side_effect=Exception("Database error"))
    @patch.object(StudentDB, 'close')
    def test_get_student_by_email_exception(self, mock_close, mock_get_by_email):
        with self.assertRaises(Exception) as context:
            Student.get_by_email("test@student.com")
        self.assertTrue("Database error" in str(context.exception))
        mock_get_by_email.assert_called_once_with("test@student.com")
        mock_close.assert_called_once()


if __name__ == '__main__':
    unittest.main()