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
        """
        try:
            userConn = UserDB()
            userId = userConn.insert(email, password, "student")
            with self.con:
                query = """ INSERT INTO Students (
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


    def close(self):
        self.con.close()    