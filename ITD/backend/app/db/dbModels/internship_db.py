from sqlite3 import connect, Row
from os import getenv
from typing import Union
from dotenv import load_dotenv


class InternshipDB:                 # Ongoing Finished
    def __init__(self):
        load_dotenv()
        self.con = connect(getenv("DATABASE"))
        self.con.row_factory = Row

    def create_table(self):
        try:
            with self.con:
                self.con.execute(""" DROP TABLE IF EXISTS Internship """)
                self.con.execute(""" CREATE TABLE IF NOT EXISTS Internship (
                                        InternshipId INTEGER PRIMARY KEY AUTOINCREMENT,
                                        InternshipPositionId INTEGER NOT NULL,
                                        ApplicationId INTEGER NOT NULL,
                                        Status TEXT NOT NULL
                                    ); """)
        except Exception as e:
            self.con.rollback()
            raise e

    def insert(self, internshipPositionId: int, applicationId: int, status: str) -> Union[int, None, Exception]:
        """
        Insert a new internship into the database and return the ID of the inserted row.

        :params internshipPositionId: int, applicationId: int, status: str.
        :return: The ID of the inserted row.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ INSERT INTO Internship (InternshipPositionId, ApplicationId, Status) VALUES (?, ?, ?) """
                cur.execute(query, (internshipPositionId, applicationId, status))
                return cur.lastrowid
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()


    #############
    #    GET    #
    ############# 
    def get_by_id(self, internshipId: int) -> Union[dict, None, Exception]:
        """
        Retrieve an internship by its ID.

        :param internshipId: The ID of the internship.
        :return: A dictionary representing the internship or None if not found.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT * FROM Internship WHERE InternshipId = ? """
            row = cur.execute(query, (internshipId,)).fetchone()
            
            return {
                "internshipId": row["InternshipId"],
                "internshipPositionId": row["InternshipPositionId"],
                "applicationId": row["ApplicationId"],
                "status": row["Status"]
            } if row else None
        
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()
        
    def get_by_application_id(self, applicationId: int) -> Union[dict, None, Exception]:
        """
        Retrieve an internship by its application ID.

        :param applicationId: The ID of the application.
        :return: A dictionary representing the internship or None if not found.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT * FROM Internship WHERE ApplicationId = ? """
            row = cur.execute(query, (applicationId,)).fetchone()
            
            return {
                "internshipId": row["InternshipId"],
                "internshipPositionId": row["InternshipPositionId"],
                "applicationId": row["ApplicationId"],
                "status": row["Status"]
            } if row else None
        
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    def get_by_internshipPosition_id(self, internshipPositionId: int) -> Union[list, Exception]:
        """
        Retrieve internships by their position ID.

        :param internshipPositionId: The ID of the internship position.
        :return: A list of dictionaries representing the internships or an empty list if not found.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT * FROM Internship WHERE InternshipPositionId = ? """
            rows = cur.execute(query, (internshipPositionId,)).fetchall()
            
            return [
                {
                    "internshipId": row["InternshipId"],
                    "internshipPositionId": row["InternshipPositionId"],
                    "applicationId": row["ApplicationId"],
                    "status": row["Status"]
                } for row in rows
            ] if rows else []
        
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    def get_by_applicationId_internshipPositionId(self, applicationId: int, internshipPositionId: int) -> Union[dict, None, Exception]:
        """
        Retrieve an internship by the application ID and the internship position ID.

        :param applicationId: The ID of the application.
        :param internshipPositionId: The ID of the internship position.
        :return: A dictionary representing the internship or None if not found.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT * FROM Internship WHERE ApplicationId = ? AND InternshipPositionId = ? """
            row = cur.execute(query, (applicationId, internshipPositionId)).fetchone()
            
            return {
                "internshipId": row["InternshipId"],
                "internshipPositionId": row["InternshipPositionId"],
                "applicationId": row["ApplicationId"],
                "status": row["Status"]
            } if row else None
        
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    
    def get_by_company_id(self, companyId: int) -> Union[list, Exception]:
        """
        Retrieve internships by their company ID.

        :param companyId: The ID of the company.
        :return: A list of dictionaries representing the internships or an empty list if not found.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT InternshipId, InternshipPositionId, ApplicationId, Status 
                        FROM Internship 
                        WHERE InternshipPositionId IN (SELECT InternshipPositionId 
                                                       FROM InternshipPosition 
                                                       WHERE CompanyId = ?) """
            rows = cur.execute(query, (companyId,)).fetchall()
            
            return [
                {
                    "internshipId": row["InternshipId"],
                    "internshipPositionId": row["InternshipPositionId"],
                    "applicationId": row["ApplicationId"],
                    "status": row["Status"]
                } for row in rows
            ] if rows else []
        
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    
    def get_preview_by_company_id(self, companyId: int) -> Union[list, Exception]:
        """
        Retrieve internships by their company ID.

        :param companyId: The ID of the company.
        :return: A list of dictionaries representing the internships or an empty list if not found. Each dictionary contains:
            - student_name (str): The full name of the student.
            - student_photoPath (str | None): The path to the student's photo.
            - internshipId (int): The ID of the internship.
            - roleTitle (str): The title of the role.
            - status (str): The status of the internship.

        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT S.FirstName, S.LastName, S.ProfilePicturePath, I.InternshipId, I.Status, IP.RoleTitle
                        FROM Internship AS I, Application AS A, Student AS S, InternshipPosition AS IP
                        WHERE I.ApplicationId = A.ApplicationId AND 
                              A.StudentId = S.UserId AND 
                              I.InternshipPositionId = IP.InternshipPositionId AND 
                              IP.CompanyId = ?"""
            rows = cur.execute(query, (companyId,)).fetchall()
            
            return [
                {
                    "student_name": row["FirstName"] + " " + row["LastName"],
                    "student_photoPath": row["ProfilePicturePath"],
                    "internshipId": row["InternshipId"],
                    "roleTitle": row["RoleTitle"],
                    "status": row["Status"]
                } for row in rows
            ] if rows else []
        
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()


    def get_preview_by_student_id(self, studentId: int) -> Union[list, Exception]:
        """
        Retrieve internships by their student ID.

        :param studentId: The ID of the student.
        :return: A list of dictionaries representing the internships or an empty list if not found. Each dictionary contains:
            - company_name (str): The name of the company.
            - company_photoPath (str | None): The path to the company's photo.
            - internshipId (int): The ID of the internship.
            - roleTitle (str): The title of the role.
            - status (str): The status of the internship.

        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT C.CompanyName, C.LogoPath, I.InternshipId, I.Status, IP.RoleTitle
                        FROM Internship AS I, Application AS A, Company AS C, InternshipPosition AS IP
                        WHERE I.ApplicationId = A.ApplicationId AND 
                              A.InternshipPositionId = IP.InternshipPositionId AND 
                              IP.CompanyId = C.UserId AND 
                              A.StudentId = ?"""
            rows = cur.execute(query, (studentId,)).fetchall()
            
            return [
                {
                    "company_name": row["CompanyName"],
                    "company_photoPath": row["LogoPath"],
                    "internshipId": row["InternshipId"],
                    "roleTitle": row["RoleTitle"],
                    "status": row["Status"]
                } for row in rows
            ] if rows else []
        
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close


    def get_preview_by_university_id(self, universityId: int) -> Union[list, Exception]:
        """
        Retrieve internships by their university ID.

        :param universityId: The ID of the university.
        :return: A list of dictionaries representing the internships or an empty list if not found. Each dictionary contains:
            - student_name (str): The full name of the student.
            - company_name (str): The name of the company.
            - internshipId (int): The ID of the internship.
            - roleTitle (str): The title of the role.
            - status (str): The status of the internship.

        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT S.FirstName, S.LastName, C.CompanyName, I.InternshipId, I.Status, IP.RoleTitle
                        FROM Internship AS I, Application AS A, Student AS S, InternshipPosition AS IP, Company AS C
                        WHERE I.ApplicationId = A.ApplicationId AND 
                              A.StudentId = S.UserId AND 
                              A.InternshipPositionId = IP.InternshipPositionId AND 
                              IP.CompanyId = C.UserId AND 
                              S.UniversityId = ?"""
            rows = cur.execute(query, (universityId,)).fetchall()
            
            return [
                {
                    "student_name": row["FirstName"] + " " + row["LastName"],
                    "company_name": row["CompanyName"],
                    "internshipId": row["InternshipId"],
                    "roleTitle": row["RoleTitle"],
                    "status": row["Status"]
                } for row in rows
            ] if rows else []
        
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()


    ################
    #    UPDATE    #
    ################ 
    def update_status(self, internshipId: int, status: str) -> bool:
        """
        Update the status of an internship by its ID.

        :param internshipId: The ID of the internship.
        :param status: The new status of the internship.
        :return: True if the update was successful, otherwise False.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ UPDATE Internship SET Status = ? WHERE InternshipId = ? """
                res = cur.execute(query, (status, internshipId))
                return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            return False
        finally:
            cur.close()


    def close(self):
        self.con.close()