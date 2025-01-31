from sqlite3 import connect, Row
from .user_db import UserDB
from typing import Optional, Union
from os import getenv
from dotenv import load_dotenv

class StudentDB:
    def __init__(self):
        load_dotenv()
        self.con = connect(getenv("DATABASE"))
        self.con.row_factory = Row

    def create_table(self):
        try:
            with self.con:
                self.con.execute(""" DROP TABLE IF EXISTS Student """)
                self.con.execute(""" CREATE TABLE IF NOT EXISTS Student (
                                        UserId INTEGER PRIMARY KEY,
                                        FirstName TEXT NOT NULL,
                                        LastName TEXT NOT NULL,
                                        PhoneNumber TEXT NOT NULL,
                                        ProfilePicturePath TEXT,
                                        Location TEXT NOT NULL,
                                        DegreeProgram TEXT NOT NULL,
                                        Gpa REAL,
                                        GraduationYear INTEGER,
                                        CVpath TEXT NOT NULL,
                                        Skills TEXT NOT NULL,
                                        LanguageSpoken TEXT NOT NULL,
                                        UniversityId INTEGER NOT NULL,
                                        FOREIGN KEY (UserId) REFERENCES User(UserId)
                                ); """)
        except Exception as e:
            self.con.rollback()
            raise e

    
    def insert(self, email: str, password: str, firstName: str, lastName: str, phoneNumber: str, profilePicturePath: Optional[str], location: str, 
            degreeProgram: str, gpa: Optional[float], graduationYear: Optional[int], CVpath: str, skills: str, languageSpoken: str, universityId: int) -> Union[int, Exception, None]:
        """
        Insert a new student into the database and return the ID of the inserted row.
        
        :param item: A tuple containing (email: str, password: str, firstName: str, lastName: str, phoneNumber: str, profilePicturePath: str, location: str, 
            degreeProgram: str, gpa: float, graduationYear: int, CVpath: str, skills: str, languageSpoken: str, universityId: int).
        :return: The ID of the inserted row.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            userConn = UserDB()
            userId = userConn.insert(email, password, "student")
            with self.con:
                cur = self.con.cursor()
                query = """ INSERT INTO Student (
                        UserId, FirstName, LastName, PhoneNumber, ProfilePicturePath, 
                        Location, DegreeProgram, Gpa, GraduationYear, CVpath, Skills, 
                        LanguageSpoken, UniversityId
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """
                cur.execute(query, (userId, firstName, lastName, phoneNumber, profilePicturePath, 
                                    location, degreeProgram, gpa, graduationYear, CVpath, skills, 
                                    languageSpoken, universityId))
                cur.close()
            return userId
        except Exception as e:
            if str(e) != "UNIQUE constraint failed: User.Email":
                userConn.remove(userId)
            self.con.rollback()
            raise e
        finally:
            userConn.close()

    #############
    #    GET    #
    ############# 
    def get_by_id(self, id: int) -> Union[dict, None, Exception]:
        """
        Retrieve a student record by its id and return the data as a dictionary.

        :param id: The id of the student.
        :return: A dictionary with student data if found, otherwise None.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT * 
                        FROM Student AS S JOIN User AS U ON S.UserId = U.UserId
                        WHERE S.UserId = ? """
            student = cur.execute(query, (id,)).fetchone()

            return {    'id': student['UserId'], 
                        'email': student['Email'],
                        'password': student['Password'],
                        'firstName': student['FirstName'], 
                        'lastName': student['LastName'], 
                        'phoneNumber': student['PhoneNumber'], 
                        'profilePicture': student['ProfilePicturePath'], 
                        'location': student['Location'], 
                        'universityId': student['UniversityId'], 
                        'degreeProgram': student['DegreeProgram'], 
                        'GPA': student['Gpa'], 
                        'graduationYear': student['GraduationYear'], 
                        'skills': student['Skills'], 
                        'CV': student['CVpath'], 
                        'languageSpoken': student['LanguageSpoken']
                    } if student else None

        except Exception as e:
            self.con.rollback()
            raise e  
        finally:
            cur.close()

    def get_by_email(self, email: str) -> Union[dict, None, Exception]:
        """
        Retrieve a student record by email and return the data as a dictionary.

        :param email: The email address of the student.
        :return: A dictionary with student data if found, otherwise None.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT * 
                        FROM Student AS S JOIN User AS U ON S.UserId = U.UserId
                        WHERE Email = ? """
            student = cur.execute(query, (email,)).fetchone()
            
            return {    'id': student['UserId'], 
                        'email': student['Email'],
                        'password': student['Password'],
                        'firstName': student['FirstName'], 
                        'lastName': student['LastName'], 
                        'phoneNumber': student['PhoneNumber'], 
                        'profilePicture': student['ProfilePicturePath'], 
                        'location': student['Location'], 
                        'universityId': student['UniversityId'], 
                        'degreeProgram': student['DegreeProgram'], 
                        'GPA': student['Gpa'], 
                        'graduationYear': student['GraduationYear'], 
                        'skills': student['Skills'], 
                        'CV': student['CVpath'], 
                        'languageSpoken': student['LanguageSpoken']
                    } if student else None
          
        except Exception as e:
            self.con.rollback()
            raise e 
        finally:
            cur.close() 


    ################
    #    UPDATE    #
    ################ 

    def update(self, id: int, phoneNumber: str, profilePicture: Union[str, None], location: str, degreeProgram: str, GPA: Union[float, None], 
               graduationYear: Union[int, None], CV: str, skills: str, languageSpoken: str, universityId: int) -> Union[None, Exception]:
        """
        Update an existing student record in the database and return the updated student data as a dictionary.

        :param id: The unique identifier of the student.
        :param phoneNumber: The contact number of the student.
        :param profilePicture: The file path to the student's profile picture. [Optional]
        :param location: The current location of the student.
        :param degreeProgram: The degree program the student is enrolled in. 
        :param GPA: The grade point average of the student. [Optional]
        :param graduationYear: The expected graduation year of the student. [Optional]
        :param CV: The file path to the student's CV. 
        :param skills: A list of skills possessed by the student. 
        :param languageSpoken: Languages spoken by the student. 
        :param universityId: The ID of the university the student is associated with. 
        
        :return: The ID of the updated student if the update was successful, otherwise None.
        :raises Exception: If an error occurs during the update process.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ UPDATE Student
                            SET PhoneNumber = ?, ProfilePicturePath = ?, Location = ?, DegreeProgram = ?, Gpa = ?, GraduationYear = ?, CVpath = ?, Skills = ?, LanguageSpoken = ?, UniversityId = ?
                            WHERE UserId = ? """
                cur.execute(query, (phoneNumber, profilePicture, location, degreeProgram, GPA, graduationYear, CV, skills, languageSpoken, universityId, id))
                if not cur.rowcount > 0:
                    raise Exception("Student not found")
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()
            
    def close(self):
        self.con.close()    