from sqlite3 import connect, Row
from app.db.dbModels.user_db import UserDB

DATABASE = 'app/db/SC.db'

class StudentDB:
    def __init__(self):
        self.con = connect(DATABASE)
        self.con.row_factory = Row

    def create_table(self):
        try:
            with self.con:
                # self.con.execute(""" DROP TABLE Student """)
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

    
    def insert(self, email: str, password: str, firstName: str, lastName: str, phoneNumber: str, profilePicturePath: str, location: str, 
            degreeProgram: str, gpa: float, graduationYear: int, CVpath: str, skills: str, languageSpoken: str, universityId: int):
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
                query = """ INSERT INTO Student (
                        UserId, FirstName, LastName, PhoneNumber, ProfilePicturePath, 
                        Location, DegreeProgram, Gpa, GraduationYear, CVpath, Skills, 
                        LanguageSpoken, UniversityId
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """
                self.con.execute(query, (userId, firstName, lastName, phoneNumber, profilePicturePath, 
                                    location, degreeProgram, gpa, graduationYear, CVpath, skills, 
                                    languageSpoken, universityId))
            return userId
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            userConn.close()


    def get_by_id(self, id: int):
        """
        Retrieve a student record by its unique identifier.

        :param id: The unique identifier of the student.
        :return: A tuple representing the student record if found, otherwise None.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                query = """ SELECT * 
                            FROM Student AS S JOIN User AS U ON S.UserId = U.UserId
                            WHERE S.UserId = ? """
                student = self.con.execute(query, (id,)).fetchone()
            return student if student else None
        except Exception as e:
            self.con.rollback()
            raise e    


    def get_by_email(self, email: str):
        """
        Retrieve a student record by its email.

        :param email: The unique email of the student.
        :return: A tuple representing the student record if found, otherwise None.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                query = """ SELECT * 
                            FROM Student AS S JOIN User AS U ON S.UserId = U.UserId
                            WHERE Email = ? """
                student = self.con.execute(query, (email,)).fetchone()
            return student if student else None
        except Exception as e:
            self.con.rollback()
            raise e  


    def update_phone_number_by_id(self, id: int, phoneNumber: str):
        """
        Update the phone number of a student based on their unique ID.

        :param id: The unique ID of the student.
        :param phoneNumber: The new phone number to update.
        :return: True if the update is successful, otherwise False.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                query = """ UPDATE Student
                            SET PhoneNumber = ?
                            WHERE UserId = ? """
                res = self.con.execute(query, (phoneNumber, id))
            return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            raise e 
        
    
    def update_profile_picture_path_by_id(self, id: int, profilePicturePath: str):
        """
        Update the profile picture path of a student based on their unique ID.

        :param id: The unique ID of the student.
        :param profilePicturePath: The new profile picture path to update.
        :return: True if the update is successful, otherwise False.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                query = """ UPDATE Student
                            SET ProfilePicturePath = ?
                            WHERE UserId = ? """
                res = self.con.execute(query, (profilePicturePath, id))
            return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            raise e 
        
    
    def update_location_by_id(self, id: int, location: str):
        """
        Update the location of a student based on their unique ID.

        :param id: The unique ID of the student.
        :param location: The new location to update.
        :return: True if the update is successful, otherwise False.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                query = """ UPDATE Student
                            SET Location = ?
                            WHERE UserId = ? """
                res = self.con.execute(query, (location, id))
            return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            raise e 


    def update_degree_program_by_id(self, id: int, degreeProgram: str):
        """
        Update the degree program of a student based on their unique ID.

        :param id: The unique ID of the student.
        :param degreeProgram: The new degree program to update.
        :return: True if the update is successful, otherwise False.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                query = """ UPDATE Student
                            SET DegreeProgram = ?
                            WHERE UserId = ? """
                res = self.con.execute(query, (degreeProgram, id))
            return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            raise e 
    

    def update_gpa_by_id(self, id: int, gpa: str):
        """
        Update the gpa of a student based on their unique ID.

        :param id: The unique ID of the student.
        :param gpa: The new gpa to update.
        :return: True if the update is successful, otherwise False.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                query = """ UPDATE Student
                            SET Gpa = ?
                            WHERE UserId = ? """
                res = self.con.execute(query, (gpa, id))
            return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            raise e 
        
    
    def update_graduation_year_by_id(self, id: int, graduationYear: str):
        """
        Update the graduation year of a student based on their unique ID.

        :param id: The unique ID of the student.
        :param graduationYear: The new graduation year to update.
        :return: True if the update is successful, otherwise False.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                query = """ UPDATE Student
                            SET GraduationYear = ?
                            WHERE UserId = ? """
                res = self.con.execute(query, (graduationYear, id))
            return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            raise e 
        

    def update_cv_path_by_id(self, id: int, cvPath: str):
        """
        Update the CV path of a student based on their unique ID.

        :param id: The unique ID of the student.
        :param cvPath: The new CV path to update.
        :return: True if the update is successful, otherwise False.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                query = """ UPDATE Student
                            SET CVpath = ?
                            WHERE UserId = ? """
                res = self.con.execute(query, (cvPath, id))
            return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            raise e 
    

    def update_skills_by_id(self, id: int, skills: str):
        """
        Update the skills of a student based on their unique ID.

        :param id: The unique ID of the student.
        :param skills: The new skills to update.
        :return: True if the update is successful, otherwise False.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                query = """ UPDATE Student
                            SET Skills = ?
                            WHERE UserId = ? """
                res = self.con.execute(query, (skills, id))
            return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            raise e 
    

    def update_language_spoken_by_id(self, id: int, languageSpoken: str):
        """
        Update the languages spoken by a student based on their unique ID.

        :param id: The unique ID of the student.
        :param languageSpoken: The new languages spoken to update.
        :return: True if the update is successful, otherwise False.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                query = """ UPDATE Student
                            SET LanguageSpoken = ?
                            WHERE UserId = ? """
                res = self.con.execute(query, (languageSpoken, id))
            return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            raise e 
      

    def update_university_by_id(self, id: int, universityId: str):
        """
        Update the university of a student based on their unique ID.

        :param id: The unique ID of the student.
        :param universityId: The new university to update.
        :return: True if the update is successful, otherwise False.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                query = """ UPDATE Student
                            SET UniversityId = ?
                            WHERE UserId = ? """
                res = self.con.execute(query, (universityId, id))
            return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            raise e 
        

    def close(self):
        self.con.close()    