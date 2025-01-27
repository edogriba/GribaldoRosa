from sqlite3 import connect, Row

DATABASE = 'app/db/SC.db'
                                # pending -> rejected / accepted -> refused (if accepted) / confirmed (if accepted)
class ApplicationDB:            # confirmed (student), refused (student), pending, rejected (company), accepted (company)
    def __init__(self):
        self.con = connect(DATABASE)
        self.con.row_factory = Row

    def create_table(self):
        try:
            with self.con:
                # self.con.execute(""" DROP TABLE Application """)
                self.con.execute(""" CREATE TABLE IF NOT EXISTS Application (
                                        ApplicationId INTEGER PRIMARY KEY AUTOINCREMENT,
                                        StudentId INTEGER NOT NULL,
                                        InternshipPositionId INTEGER NOT NULL,
                                        State TEXT NOT NULL
                                    ); """)
        except Exception as e:
            self.con.rollback()
            raise e

    def insert(self, studentId: int, internshipPositionId: int, state: str):
        """
        Insert a new application into the database and return the ID of the inserted row.

        :params studentId: int, internshipPositionId: int, state: str.
        :return: The ID of the inserted row.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ INSERT INTO Application (StudentId, InternshipPositionId, State) VALUES (?, ?, ?) """
                cur.execute(query, (studentId, internshipPositionId, state))
                return cur.lastrowid
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    #############
    #    GET    #
    ############# 
    def get_by_id(self, applicationId: int):
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
                "state": row["State"]
            } if row else None
        
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    def get_by_studentId(self, studentId: int):
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
                    "state": row["State"]
                } for row in rows
            ] if rows else []
        
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    def get_by_internshipPositionId(self, internshipPositionId: int):
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
                    "state": row["State"]
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
    def update_state(self, applicationId: int, state: str):
        """
        Update the state of an application by its ID.

        :param applicationId: The ID of the application.
        :param state: The new state of the application.
        :return: True if the update was successful, otherwise False.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ UPDATE Application SET State = ? WHERE ApplicationId = ? """
                cur.execute(query, (state, applicationId))
                return True
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()


    def close(self):
        self.con.close()