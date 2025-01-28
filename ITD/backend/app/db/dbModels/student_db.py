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
            degreeProgram: str, gpa: Optional[float], graduationYear: Optional[int], CVpath: str, skills: str, languageSpoken: str, universityId: int) -> Union[int, Exception]:
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
    def update_phone_number_by_id(self, id: int, phoneNumber: str) -> bool:
        """
        Update the phone number of a student based on their unique ID.

        :param id: The unique ID of the student.
        :param phoneNumber: The new phone number to update.
        :return: True if the update is successful, otherwise False.
        """
        if phoneNumber == "":
                return False
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ UPDATE Student
                            SET PhoneNumber = ?
                            WHERE UserId = ? """
                res = cur.execute(query, (phoneNumber, id))
            return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            return False     
        finally:
            cur.close()
    
    def update_profile_picture_path_by_id(self, id: int, profilePicturePath: Optional[str]) -> bool:
        """
        Update the profile picture path of a student based on their unique ID.

        :param id: The unique ID of the student.
        :param profilePicturePath: The new profile picture path to update.
        :return: True if the update is successful, otherwise False.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ UPDATE Student
                            SET ProfilePicturePath = ?
                            WHERE UserId = ? """
                res = cur.execute(query, (profilePicturePath, id))
            return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            return False
        finally:
            cur.close()
          
    def update_location_by_id(self, id: int, location: str) -> bool:
        """
        Update the location of a student based on their unique ID.

        :param id: The unique ID of the student.
        :param location: The new location to update.
        :return: True if the update is successful, otherwise False.
        """
        if location == "":
                return False
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ UPDATE Student
                            SET Location = ?
                            WHERE UserId = ? """
                res = cur.execute(query, (location, id))
            return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            False
        finally:
            cur.close()

    def update_degree_program_by_id(self, id: int, degreeProgram: str) -> bool:
        """
        Update the degree program of a student based on their unique ID.

        :param id: The unique ID of the student.
        :param degreeProgram: The new degree program to update.
        :return: True if the update is successful, otherwise False.
        """
        if degreeProgram == "":
                return False
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ UPDATE Student
                            SET DegreeProgram = ?
                            WHERE UserId = ? """
                res = cur.execute(query, (degreeProgram, id))
            return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            return False
        finally:
            cur.close()
    
    def update_gpa_by_id(self, id: int, gpa: Optional[float]) -> bool:
        """
        Update the gpa of a student based on their unique ID.

        :param id: The unique ID of the student.
        :param gpa: The new gpa to update.
        :return: True if the update is successful, otherwise False.
        """
        if gpa is not None and not isinstance(gpa, (float, int)):
            return False
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ UPDATE Student
                            SET Gpa = ?
                            WHERE UserId = ? """
                res = cur.execute(query, (gpa, id))
            return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            return False
        finally:
            cur.close()
           
    def update_graduation_year_by_id(self, id: int, graduationYear: Optional[str]) -> bool:
        """
        Update the graduation year of a student based on their unique ID.

        :param id: The unique ID of the student.
        :param graduationYear: The new graduation year to update.
        :return: True if the update is successful, otherwise False.
        """
        if graduationYear is not None and not isinstance(graduationYear, int):
            return False
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ UPDATE Student
                            SET GraduationYear = ?
                            WHERE UserId = ? """
                res = cur.execute(query, (graduationYear, id))
            return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            return False
        finally:
            cur.close()
        
    def update_cv_path_by_id(self, id: int, cvPath: str) -> bool:
        """
        Update the CV path of a student based on their unique ID.

        :param id: The unique ID of the student.
        :param cvPath: The new CV path to update.
        :return: True if the update is successful, otherwise False.
        """
        if cvPath == "":
            return False
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ UPDATE Student
                            SET CVpath = ?
                            WHERE UserId = ? """
                res = cur.execute(query, (cvPath, id))
            return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            return False
        finally:
            cur.close()
    
    def update_skills_by_id(self, id: int, skills: str) -> bool:
        """
        Update the skills of a student based on their unique ID.

        :param id: The unique ID of the student.
        :param skills: The new skills to update.
        :return: True if the update is successful, otherwise False.
        """
        if skills == "":
            return False
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ UPDATE Student
                            SET Skills = ?
                            WHERE UserId = ? """
                res = cur.execute(query, (skills, id))
            return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            return False
        finally:
            cur.close()
    
    def update_language_spoken_by_id(self, id: int, languageSpoken: str) -> bool:
        """
        Update the languages spoken by a student based on their unique ID.

        :param id: The unique ID of the student.
        :param languageSpoken: The new languages spoken to update.
        :return: True if the update is successful, otherwise False.
        """
        if languageSpoken == "":
            return False
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ UPDATE Student
                            SET LanguageSpoken = ?
                            WHERE UserId = ? """
                res = cur.execute(query, (languageSpoken, id))
            return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            return False
        finally:
            cur.close()
      
    def update_university_by_id(self, id: int, universityId: int) -> bool:
        """
        Update the university of a student based on their unique ID.

        :param id: The unique ID of the student.
        :param universityId: The new university to update.
        :return: True if the update is successful, otherwise False.
        """
        if not isinstance(universityId, int):
            return False
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ UPDATE Student
                            SET UniversityId = ?
                            WHERE UserId = ? """
                res = cur.execute(query, (universityId, id))
            return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            return False
        finally:
            cur.close()

    def close(self):
        self.con.close()    