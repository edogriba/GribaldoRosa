from sqlite3 import connect, Row

DATABASE = 'app/db/SC.db'

class InternshipPositionDB:
    def __init__(self):
        self.con = connect(DATABASE)
        self.con.row_factory = Row

    def create_table(self):
        try:
            with self.con:
                # self.con.execute(""" DROP TABLE InternshipPosition """)
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
                                        Description TEXT NOT NULL
                                    ); """)
        except Exception as e:
            self.con.rollback()
            raise e

    def insert(self, companyId: int, programName: str, duration: int, location: str, roleTitle: str, skillsRequired: str, 
                compensation: int, benefits: str, languagesRequired: str, description: str):
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
                                                            Compensation, Benefits, LanguagesRequired, Description) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) """
                cur.execute(query, (companyId, programName, duration, location, roleTitle, skillsRequired, 
                                    compensation, benefits, languagesRequired, description))
                return cur.lastrowid
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()


    #############
    #    GET    #
    #############
    def get_by_id(self, internshipPositionId: int):
        """
        Retrieve an internship position by its ID.
        :param internshipPositionId: The ID of the internship position.
        :return: A dictionary representing the internship position or None if not found.
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
                    "description": row["Description"]
                } if row else None
            
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    def get_by_company(self, companyId: int):
        """
        Retrieve all internship positions for a given company ID.
        :param companyId: The ID of the company.
        :return: A list of dictionaries representing the internship positions.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ SELECT InternshipPositionId, CompanyId, ProgramName, Duration, Location, RoleTitle, SkillsRequired, 
                            Compensation, Benefits, LanguagesRequired, Description 
                            FROM InternshipPosition WHERE CompanyId = ? """
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
                        "description": row["Description"]
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
                        "description": row["Description"]
                    } for row in rows
                ]
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()
        

    def close(self):
        self.con.close()
