from app.models.user import User
from app.db.dbModels.student_db import StudentDB

class Student(User):
    def __init__(self, id, email, password, firstName, lastName, phoneNumber, profilePicture, location, universityId, degreeProgram, GPA, graduationYear, skills, CV, languageSpoken):
        super().__init__(id, email, password, "student")
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.profilePicture = profilePicture
        self.location = location
        self.universityId = universityId          
        self.degreeProgram = degreeProgram
        self.GPA = GPA
        self.graduationYear = graduationYear
        self.skills = skills
        self.CV = CV
        self.languageSpoken = languageSpoken

    #def __repr__(self):
    #    return f"<Student: ({self.id}) {self.firstName} {self.lastName}, Email: {self.email}"
    
    def get_id(self):
        return super().get_id()
    
    def get_email(self):
        return super().get_email()
    
    def get_password(self):
        return super().get_password()
    
    def get_type(self):
        return super().get_type()
    
    def get_firstName(self):
        return self.firstName
    
    def get_lastName(self):
        return self.lastName

    def get_phoneNumber(self):
        return self.phoneNumber
    
    def get_profilePicture(self):
        return self.profilePicture
    
    def get_location(self):
        return self.location
    
    def get_universityId(self):
        return self.universityId
    
    def get_degreeProgram(self):
        return self.degreeProgram
    
    def get_gpa(self):
        return self.GPA
    
    def get_graduationYear(self):
        return self.graduationYear
    
    def get_skills(self):
        return self.skills
    
    def get_cv(self):
        return self.CV
    
    def get_languageSpoken(self):
        return self.languageSpoken
    
    def to_dict(self):
        user_dict = super().to_dict()
        user_dict.update({
            'firstName': self.firstName,
            'lastName': self.lastName,
            'phoneNumber': self.phoneNumber,
            'profilePicture': self.profilePicture,
            'location': self.location,
            'universityId': int(self.universityId),          
            'degreeProgram': self.degreeProgram,
            'GPA': float(self.GPA),
            'graduationYear': int(self.graduationYear),
            'skills': self.skills,
            'CV': self.CV,
            'languageSpoken': self.languageSpoken,
        })
        return user_dict

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False
    
    @staticmethod
    def add(email: str, password: str, firstName: str, lastName: str, phoneNumber: str, profilePicturePath: str, location: str, 
            degreeProgram: str, gpa: float, graduationYear: int, CVpath: str, skills: str, languageSpoken: str, universityId: int):
        """
        Add a new student record to the database and return a Student object.

        :param email: The email address of the student.
        :param password: The password for the student's account.
        :param firstName: The first name of the student.
        :param lastName: The last name of the student.
        :param phoneNumber: The contact number of the student.
        :param profilePicturePath: The file path to the student's profile picture.
        :param location: The current location of the student.
        :param degreeProgram: The degree program the student is enrolled in.
        :param gpa: The grade point average of the student.
        :param graduationYear: The expected graduation year of the student.
        :param CVpath: The file path to the student's CV.
        :param skills: A list of skills possessed by the student.
        :param languageSpoken: Languages spoken by the student.
        :param universityId: The ID of the university the student is associated with.
        :return: A Student object containing the newly inserted student's data.
        :raises Exception: If an error occurs during the insertion process.
        """
        try:
            # Insert student data into the database
            studentConn = StudentDB()
            studentId = studentConn.insert(email, password, firstName, lastName, phoneNumber, profilePicturePath, location, 
                degreeProgram, gpa, graduationYear, CVpath, skills, languageSpoken, universityId)

            return Student(studentId, email, password, firstName, lastName, phoneNumber, profilePicturePath, location,
                           degreeProgram, gpa, graduationYear, CVpath, skills, languageSpoken, universityId)
        
        except Exception as e:
            raise e
        
        finally:
            studentConn.close()

    @staticmethod
    def get_by_id(id: int):
        """
        Retrieve a student record by its unique identifier and return it as a Student object.

        :param id: The unique identifier of the student.
        :return: A Student object populated with the retrieved data if found, otherwise None.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            studentConn = StudentDB()
            studentData = studentConn.get_by_id(id)
            return Student(**studentData) if studentData else None
        except Exception as e:
            raise e
        finally:
            studentConn.close()

    @staticmethod
    def get_by_email(email: str):
        """
        Retrieve a student record by its email and return it as a Student object.

        :param email: The email of the student.
        :return: A Student object populated with the retrieved data if found, otherwise None.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            studentConn = StudentDB()
            studentData = studentConn.get_by_email(email)
            return Student(**studentData) if studentData else None
        except Exception as e:
            raise e
        finally:
            studentConn.close()
