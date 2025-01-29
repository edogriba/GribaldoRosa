from sqlite3 import connect, Row
from typing import Union
from os import getenv
from dotenv import load_dotenv
                                # pending -> rejected / accepted -> refused (if accepted) / confirmed (if accepted)
class ApplicationDB:            # confirmed (student), refused (student), pending, rejected (company), accepted (company)
    def __init__(self):
        load_dotenv()
        self.con = connect(getenv("DATABASE"))
        self.con.row_factory = Row

    def create_table(self):
        try:
            with self.con:
                self.con.execute(""" DROP TABLE IF EXISTS Application """)
                self.con.execute(""" CREATE TABLE IF NOT EXISTS Application (
                                        ApplicationId INTEGER PRIMARY KEY AUTOINCREMENT,
                                        StudentId INTEGER NOT NULL,
                                        InternshipPositionId INTEGER NOT NULL,
                                        Status TEXT NOT NULL
                                    ); """)
        except Exception as e:
            self.con.rollback()
            raise e

    def insert(self, studentId: int, internshipPositionId: int, status: str) -> Union[int, None, Exception]:
        """
        Insert a new application into the database and return the ID of the inserted row.

        :params studentId: int, internshipPositionId: int, status: str.
        :return: The ID of the inserted row.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ INSERT INTO Application (StudentId, InternshipPositionId, Status) VALUES (?, ?, ?) """
                cur.execute(query, (studentId, internshipPositionId, status))
                return cur.lastrowid
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    #############
    #    GET    #
    ############# 
    def get_by_id(self, applicationId: int) -> Union[dict, None, Exception]:
        """
        Retrieve an application by its ID.

        :param applicationId: The ID of the application.
        :return: A dictionary representing the application or None if not found.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT * FROM Application WHERE ApplicationId = ? """
            row = cur.execute(query, (applicationId,)).fetchone()
            
            return {
                "applicationId": row["ApplicationId"],
                "studentId": row["StudentId"],
                "internshipPositionId": row["InternshipPositionId"],
                "status": row["Status"]
            } if row else None
        
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    def get_by_studentId(self, studentId: int) -> Union[list, Exception]:
        """
        Retrieve applications by their student ID.

        :param studentId: The ID of the student.
        :return: A list of dictionaries representing the applications or an empty list if not found.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT * FROM Application WHERE StudentId = ? """
            rows = cur.execute(query, (studentId,)).fetchall()
            
            return [
                {
                    "applicationId": row["ApplicationId"],
                    "studentId": row["StudentId"],
                    "internshipPositionId": row["InternshipPositionId"],
                    "status": row["Status"]
                } for row in rows
            ] if rows else []
        
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    def get_by_internshipPositionId(self, internshipPositionId: int) -> Union[list, Exception]:
        """
        Retrieve applications by their internship position ID.

        :param internshipPositionId: The ID of the internship position.
        :return: A list of dictionaries representing the applications or an empty list if not found.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT * FROM Application WHERE InternshipPositionId = ? """
            rows = cur.execute(query, (internshipPositionId,)).fetchall()
            
            return [
                {
                    "applicationId": row["ApplicationId"],
                    "studentId": row["StudentId"],
                    "internshipPositionId": row["InternshipPositionId"],
                    "status": row["Status"]
                } for row in rows
            ] if rows else []
        
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    def get_by_studentId_internshipPositionId(self, studentId: int, internshipPositionId: int):
        """
        Retrieve an application by its student ID and internship position ID.

        :param studentId: The ID of the student.
        :param internshipPositionId: The ID of the internship position.
        :return: A dictionary representing the application or None if not found.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT * FROM Application WHERE StudentId = ? AND InternshipPositionId = ? """
            row = cur.execute(query, (studentId, internshipPositionId)).fetchone()
            
            return {
                "applicationId": row["ApplicationId"],
                "studentId": row["StudentId"],
                "internshipPositionId": row["InternshipPositionId"],
                "status": row["Status"]
            } if row else None
        
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    ################
    #    UPDATE    #
    ################
    def update_status(self, applicationId: int, status: str):
        """
        Update the status of an application by its ID.

        :param applicationId: The ID of the application.
        :param status: The new status of the application.
        :return: True if the update was successful, otherwise False.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ UPDATE Application SET Status = ? WHERE ApplicationId = ? """
                res = cur.execute(query, (status, applicationId))
                return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            return False
        finally:
            cur.close()


    def close(self):
        self.con.close()