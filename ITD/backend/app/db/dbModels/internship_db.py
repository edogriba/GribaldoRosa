from sqlite3 import connect, Row

DATABASE = 'app/db/SC.db'

class InternshipDB:                 # ongoing completed
    def __init__(self):
        self.con = connect(DATABASE)
        self.con.row_factory = Row

    def create_table(self):
        try:
            with self.con:
                # self.con.execute(""" DROP TABLE Internship """)
                self.con.execute(""" CREATE TABLE IF NOT EXISTS Internship (
                                        InternshipId INTEGER PRIMARY KEY AUTOINCREMENT,
                                        InternshipPositionId INTEGER NOT NULL,
                                        ApplicationId INTEGER NOT NULL,
                                        State TEXT NOT NULL
                                    ); """)
        except Exception as e:
            self.con.rollback()
            raise e

    def insert(self, internshipPositionId: int, applicationId: int, state: str):
        """
        Insert a new internship into the database and return the ID of the inserted row.

        :params internshipPositionId: int, applicationId: int, state: str.
        :return: The ID of the inserted row.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ INSERT INTO Internship (InternshipPositionId, ApplicationId, State) VALUES (?, ?, ?) """
                cur.execute(query, (internshipPositionId, applicationId, state))
                return cur.lastrowid
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()


    #############
    #    GET    #
    ############# 
    def get_by_id(self, internshipId: int):
        """
        Retrieve an internship by its ID.

        :param internshipId: The ID of the internship.
        :return: A dictionary representing the internship or None if not found.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT * FROM Internship WHERE InternshipId = ? """
            row = cur.execute(query, (internshipId,)).fetchone()
            
            return {
                "internshipId": row["InternshipId"],
                "internshipPositionId": row["InternshipPositionId"],
                "applicationId": row["ApplicationId"],
                "state": row["State"]
            } if row else None
        
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()
        
    def get_by_application_id(self, applicationId: int):
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
                "state": row["State"]
            } if row else None
        
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    def get_by_internshipPosition_id(self, internshipPositionId: int):
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
                    "state": row["State"]
                } for row in rows
            ] if rows else []
        
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    def get_by_applicationId_internshipPositionId(self, applicationId: int, internshipPositionId: int):
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
                "state": row["State"]
            } if row else None
        
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    ################
    #    UPDATE    #
    ################ 
    def update_state(self, internshipId: int, state: str):
        """
        Update the state of an internship by its ID.

        :param internshipId: The ID of the internship.
        :param state: The new state of the internship.
        :return: True if the update was successful, otherwise False.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ UPDATE Internship SET State = ? WHERE InternshipId = ? """
                cur.execute(query, (state, internshipId))
                return True
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()


    def close(self):
        self.con.close()