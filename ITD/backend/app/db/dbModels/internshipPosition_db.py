from sqlite3 import connect, Row
from typing import Optional, Union
from os import getenv
from dotenv import load_dotenv

class InternshipPositionDB:
    def __init__(self):
        load_dotenv()
        self.con = connect(getenv("DATABASE"))
        self.con.row_factory = Row

    def create_table(self):
        try:
            with self.con:
                self.con.execute(""" DROP TABLE IF EXISTS InternshipPosition """)
                self.con.execute(""" CREATE TABLE IF NOT EXISTS InternshipPosition (
                                        InternshipPositionId INTEGER PRIMARY KEY AUTOINCREMENT,
                                        CompanyId INTEGER NOT NULL,
                                        ProgramName TEXT NOT NULL,
                                        Duration INTEGER NOT NULL,
                                        Location TEXT NOT NULL,
                                        RoleTitle TEXT NOT NULL,
                                        SkillsRequired TEXT NOT NULL,
                                        Compensation INTEGER,
                                        Benefits TEXT,
                                        LanguagesRequired TEXT NOT NULL,
                                        Description TEXT NOT NULL,
                                        Status TEXT NOT NULL DEFAULT 'Open'
                                    ); """)
        except Exception as e:
            self.con.rollback()
            raise e

    def insert(self, companyId: int, programName: str, duration: int, location: str, roleTitle: str, skillsRequired: str, 
                compensation: Optional[int], benefits: Optional[str], languagesRequired: str, description: str, status: str) -> Union[int, None, Exception]:
        """
        Insert a new internship position into the database and return the ID of the inserted row.

        :param items: companyId: int, programName: str, duration: int, location: str, roleTitle: str, skillsRequired: str, 
                        compensation: int, benefits: str, languagesRequired: str, description: str.
        :return: The ID of the inserted row.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ INSERT INTO InternshipPosition (CompanyId, ProgramName, Duration, Location, RoleTitle, SkillsRequired, 
                                                            Compensation, Benefits, LanguagesRequired, Description, Status) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """
                cur.execute(query, (companyId, programName, duration, location, roleTitle, skillsRequired, 
                                    compensation, benefits, languagesRequired, description, status))
                return cur.lastrowid
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()


    #############
    #    GET    #
    #############

    def get_by_id(self, internshipPositionId: int) -> Union[dict, None, Exception]:
        """
        Retrieve an internship position by its ID.

        :param internshipPositionId: The ID of the internship position.
        :return: A dictionary representing the internship position or None if not found.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ SELECT * 
                            FROM InternshipPosition
                            WHERE InternshipPositionId = ? """
                row = cur.execute(query, (internshipPositionId,)).fetchone()

                return {
                    "internshipPositionId": row["InternshipPositionId"],
                    "companyId": row["CompanyId"],
                    "programName": row["ProgramName"],
                    "duration": row["Duration"],
                    "location": row["Location"],
                    "roleTitle": row["RoleTitle"],
                    "skillsRequired": row["SkillsRequired"],
                    "compensation": row["Compensation"],
                    "benefits": row["Benefits"],
                    "languagesRequired": row["LanguagesRequired"],
                    "description": row["Description"],
                    "status": row["Status"]
                } if row else None
            
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    def get_by_companyId(self, companyId: int) -> Union[list, Exception]:
        """
        Retrieve all internship positions for a given company ID.

        :param companyId: The ID of the company.
        :return: A list of dictionaries representing the internship positions.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ SELECT *
                            FROM InternshipPosition 
                            WHERE CompanyId = ? """
                cur.execute(query, (companyId,))
                rows = cur.fetchall()
                return [
                    {
                        "internshipPositionId": row["InternshipPositionId"],
                        "companyId": row["CompanyId"],
                        "programName": row["ProgramName"],
                        "duration": row["Duration"],
                        "location": row["Location"],
                        "roleTitle": row["RoleTitle"],
                        "skillsRequired": row["SkillsRequired"],
                        "compensation": row["Compensation"],
                        "benefits": row["Benefits"],
                        "languagesRequired": row["LanguagesRequired"],
                        "description": row["Description"],
                        "status": row["Status"]
                    } for row in rows
                ]
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    def get_by_program_name(self, programName: str) -> Union[list, Exception]:
        """
        Retrieve all internship positions for a given program name.

        :param programName: The name of the program.
        :return: A list of dictionaries representing the internship positions.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ SELECT *
                            FROM InternshipPosition 
                            WHERE ProgramName = ? """
                cur.execute(query, (programName,))
                rows = cur.fetchall()
                return [
                    {
                        "internshipPositionId": row["InternshipPositionId"],
                        "companyId": row["CompanyId"],
                        "programName": row["ProgramName"],
                        "duration": row["Duration"],
                        "location": row["Location"],
                        "roleTitle": row["RoleTitle"],
                        "skillsRequired": row["SkillsRequired"],
                        "compensation": row["Compensation"],
                        "benefits": row["Benefits"],
                        "languagesRequired": row["LanguagesRequired"],
                        "description": row["Description"],
                        "status": row["Status"]
                    } for row in rows
                ]
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    def get_list(self):
        """
        Retrieve a list of all internship positions from the database.

        :return: A list of rows, where each row represents an internship position with all its fields.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ SELECT * FROM InternshipPosition """
                rows = cur.execute(query).fetchall()
                return [
                    {
                        "internshipPositionId": row["InternshipPositionId"],
                        "companyId": row["CompanyId"],
                        "programName": row["ProgramName"],
                        "duration": row["Duration"],
                        "location": row["Location"],
                        "roleTitle": row["RoleTitle"],
                        "skillsRequired": row["SkillsRequired"],
                        "compensation": row["Compensation"],
                        "benefits": row["Benefits"],
                        "languagesRequired": row["LanguagesRequired"],
                        "description": row["Description"],
                        "status": row["Status"]
                    } for row in rows
                ]
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    def get_role_titles(self) -> Union[list, Exception]:
        """
        Retrieve all distinct role titles from the database.

        :return: A list of role titles.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ SELECT DISTINCT RoleTitle FROM InternshipPosition """
                rows = cur.execute(query).fetchall()
                return [row["RoleTitle"] for row in rows] if rows else []
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    def get_locations(self) -> Union[list, Exception]:
        """
        Retrieve all distinct locations from the database.

        :return: A list of locations.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ SELECT DISTINCT Location FROM InternshipPosition """
                rows = cur.execute(query).fetchall()
                return [row["Location"] for row in rows] if rows else []
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    def search(self, filters: dict) -> Union[list, Exception]:
        """
        Search for internship positions based on the provided filters.

        :param filters: A dictionary containing the search filters.
        :return: A list of dictionaries representing the internship positions.
        :raises Exception: If an error occurs during the database query execution.

        values = {
                'roleTitle': filters.get('roleTitle', None),        DONE
                'location': filters.get('location', None),          DONE
                'companyName': filters.get('companyName', None),
                'minStipend': filters.get('minStipend', None),      DONE
                'minDuration': filters.get('minDuration', None),    DONE
                'maxDuration': filters.get('maxDuration', None),    DONE
            }
        """
        try:
            with self.con:
                cur = self.con.cursor()
                conditions = []
                parameters = []

                if 'roleTitle' in filters and filters['roleTitle'] is not None:
                    conditions.append("RoleTitle = ?")
                    parameters.append(filters['roleTitle'])
                if 'location' in filters and filters['location'] is not None:
                    conditions.append("I.Location = ?")
                    parameters.append(filters['location'])
                if 'companyName' in filters and filters['companyName'] is not None:
                    conditions.append("CompanyName = ?")
                    parameters.append(filters['companyName'])
                if 'minStipend' in filters and filters['minStipend'] is not None:
                    conditions.append("Compensation >= ?")
                    parameters.append(filters['minStipend'])
                if 'minDuration' in filters and filters['minDuration'] is not None:
                    conditions.append("Duration >= ?")
                    parameters.append(filters['minDuration'])
                if 'maxDuration' in filters and filters['maxDuration'] is not None:
                    conditions.append("Duration <= ?")
                    parameters.append(filters['maxDuration'])

                query = """ SELECT * 
                            FROM InternshipPosition AS I JOIN Company AS C ON C.UserId = I.CompanyId
                            WHERE I.Status = 'Open'"""
                if conditions:
                    query += " AND " + " AND ".join(conditions)

                cur.execute(query, parameters)
                rows = cur.fetchall()
                return [
                    {
                        "internshipPositionId": row["InternshipPositionId"],
                        "companyId": row["CompanyId"],
                        "programName": row["ProgramName"],
                        "duration": row["Duration"],
                        "location": row["Location"],
                        "roleTitle": row["RoleTitle"],
                        "skillsRequired": row["SkillsRequired"],
                        "compensation": row["Compensation"],
                        "benefits": row["Benefits"],
                        "languagesRequired": row["LanguagesRequired"],
                        "description": row["Description"],
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
    def update_status(self, internshipPositionId: int, status: str):
        """
        Update the status of an internship position.

        :param internshipPositionId: The ID of the internship position.
        :param status: The new status of the internship position.
        :return: True if the status was updated successfully, otherwise False.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ UPDATE InternshipPosition
                            SET Status = ?
                            WHERE InternshipPositionId = ? """
                res = cur.execute(query, (status, internshipPositionId))
                return True if res.rowcount > 0 else False
        except Exception as e:
            self.con.rollback()
            return False
        finally:
            cur.close()
    
    def close(self):
        self.con.close()
