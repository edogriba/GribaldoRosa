from app.models import User
from app.db.dbModels import StudentDB, UniversityDB
from typing import Optional, Union

class Student(User):
    def __init__(self, id: int, email: str, password: str, firstName: str, lastName: str, phoneNumber: str, profilePicture: Optional[str], location: str, 
                 universityId: int, degreeProgram: str, GPA: Optional[float], graduationYear: Optional[int], skills: str, CV: str, languageSpoken: str):
        super().__init__(id, email, password, "student")
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.profilePicture = profilePicture    # optional
        self.location = location
        self.universityId = universityId          
        self.degreeProgram = degreeProgram
        self.GPA = GPA                          # optional
        self.graduationYear = graduationYear    # optional
        self.skills = skills
        self.CV = CV
        self.languageSpoken = languageSpoken

    #def __repr__(self):
    #    return f"<Student: ({self.id}) {self.firstName} {self.lastName}, Email: {self.email}"
    
    def get_id(self) -> int:
        return super().get_id()
    
    def get_email(self) -> str:
        return super().get_email()
    
    def get_password(self) -> str:
        return super().get_password()
    
    def get_type(self) -> str:
        return super().get_type()
    
    def get_firstName(self) -> str:
        return self.firstName
    
    def get_lastName(self) -> str:
        return self.lastName

    def get_phoneNumber(self) -> str:
        return self.phoneNumber
    
    def get_profilePicture(self) -> Union[str, None]:
        return self.profilePicture
    
    def get_location(self) -> str:
        return self.location
    
    def get_universityId(self) -> int:
        return self.universityId
    
    def get_degreeProgram(self) -> str:
        return self.degreeProgram
    
    def get_gpa(self) -> Union[float, None]:
        return self.GPA
    
    def get_graduationYear(self) -> Union[int, None]:
        return self.graduationYear
    
    def get_skills(self) -> str:
        return self.skills
    
    def get_cv(self) -> str:
        return self.CV
    
    def get_languageSpoken(self) -> str:
        return self.languageSpoken
    
    def get_universityName(self) -> str:
        return UniversityDB.get_by_id(self.universityId).get_name()
    
    def to_dict(self) -> dict:
        user_dict = super().to_dict()
        user_dict.update({
            'firstName': self.firstName,
            'lastName': self.lastName,
            'phoneNumber': self.phoneNumber,
            'profilePicture': self.profilePicture,
            'location': self.location,
            'universityId': self.universityId,          
            'degreeProgram': self.degreeProgram,
            'GPA': self.GPA,
            'graduationYear': self.graduationYear,
            'skills': self.skills,
            'CV': self.CV,
            'languageSpoken': self.languageSpoken,
            'universityName': Student.get_universityName(self.universityId)
        })
        return user_dict


    @staticmethod
    def add(email: str, password: str, firstName: str, lastName: str, phoneNumber: str, profilePicturePath: Optional[str], location: str, 
            degreeProgram: str, gpa: Optional[float], graduationYear: Optional[int], CVpath: str, skills: str, languageSpoken: str, universityId: int)  -> Union['Student', Exception, None]:
        """
        Add a new student record to the database and return a Student object.

        :param email: The email address of the student.
        :param password: The password for the student's account.
        :param firstName: The first name of the student.
        :param lastName: The last name of the student.
        :param phoneNumber: The contact number of the student.
        :param profilePicturePath: The file path to the student's profile picture. [Optional]
        :param location: The current location of the student.
        :param degreeProgram: The degree program the student is enrolled in.
        :param gpa: The grade point average of the student. [Optional]
        :param graduationYear: The expected graduation year of the student. [Optional]
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
            if studentId is None:
                return None
            values = {
                'id': studentId,
                'email': email,
                'password': password,
                'firstName': firstName,
                'lastName': lastName,
                'phoneNumber': phoneNumber,
                'profilePicture': profilePicturePath,
                'location': location,
                'universityId': universityId,
                'degreeProgram': degreeProgram,
                'GPA': gpa,
                'graduationYear': graduationYear,
                'skills': skills,
                'CV': CVpath,
                'languageSpoken': languageSpoken
            }
            return Student(**values)
        
        except Exception as e:
            raise e
        
        finally:
            studentConn.close()


    @staticmethod
    def get_universityName(id: int) -> Union[str, None, Exception]:
        """
        Retrieve a student record by its unique identifier and return it as a Student object.

        :param id: The unique identifier of the student.
        :return: A Student object populated with the retrieved data if found, otherwise None.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            universityConn = UniversityDB()
            universityData = universityConn.get_by_id(id)
            return universityData['name'] if universityData else None
        except Exception as e:
            raise e
        finally:
            universityConn.close()


    @staticmethod
    def get_by_id(id: int) -> Union['Student', None, Exception]:
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
    def get_by_email(email: str) -> Union['Student', None, Exception]:
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

    @staticmethod
    def update(id: int, phoneNumber: str, profilePicture: Optional[str], location: str, degreeProgram: str, GPA: Optional[float], 
               graduationYear: Optional[int], CV: str, skills: str, languageSpoken: str, universityId: int) -> Union['Student', None, Exception]:
        """
        Update an existing student record in the database and return the updated Student object.

        :param id: The unique identifier of the student.
        :param phoneNumber: The contact number of the student.
        :param profilePicturePath: The file path to the student's profile picture. [Optional]
        :param location: The current location of the student.
        :param degreeProgram: The degree program the student is enrolled in. 
        :param gpa: The grade point average of the student. [Optional]
        :param graduationYear: The expected graduation year of the student. [Optional]
        :param CV: The file path to the student's CV. 
        :param skills: A list of skills possessed by the student. 
        :param languageSpoken: Languages spoken by the student. 
        :param universityId: The ID of the university the student is associated with. 
        :return: A Student object containing the updated student's data.
        :raises Exception: If an error occurs during the update process.
        """
        try:
            studentConn = StudentDB()

            studentConn.update(id, phoneNumber, profilePicture, location, degreeProgram, GPA, graduationYear, CV, skills, languageSpoken, universityId)
            studentData = studentConn.get_by_id(id)
            return Student(**studentData) if studentData else None
        except Exception as e:
            raise e
        finally:
            studentConn.close()