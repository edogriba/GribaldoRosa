from sqlite3 import connect, Row
from typing import Union
from os import getenv
from dotenv import load_dotenv

class AssessmentDB:
    def __init__(self):
        load_dotenv()
        self.con = connect(getenv("DATABASE"))
        self.con.row_factory = Row

    def create_table(self):
        try:
            with self.con:
                self.con.execute(""" DROP TABLE IF EXISTS Assessment """)
                self.con.execute(""" CREATE TABLE IF NOT EXISTS Assessment (
                                        AssessmentId INTEGER PRIMARY KEY AUTOINCREMENT,
                                        ApplicationId INTEGER NOT NULL,
                                        Date TEXT NOT NULL,
                                        Link TEXT NOT NULL
                                    ); """)
        except Exception as e:
            self.con.rollback()
            raise e
        
    def insert(self, applicationId: int, date: str, link: str) -> Union[int, None, Exception]:
        """
        Insert a new assessment into the database and return the ID of the inserted row.

        :params applicationId: int, date: str, link: str.
        :return: The ID of the inserted row.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ INSERT INTO Assessment(ApplicationId, Date, Link) VALUES (?, ?, ?) """
                cur.execute(query, (applicationId, date, link))
                return cur.lastrowid 
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    #############
    #    GET    #
    #############
    def get_last_assessment_by_application_id(self, applicationId: int) -> Union[dict, None, Exception]:
        """
        Retrieve the last assessmentby application ID.

        :param applicationId: The ID of the application.
        :return: A dictionary representing the assessmentor None if not found.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT * FROM Assessment WHERE ApplicationId = ? ORDER BY Date DESC LIMIT 1 """
            row = cur.execute(query, (applicationId,)).fetchone()
            
            return {
                "assessmentId": row["AssessmentId"],
                "applicationId": row["ApplicationId"],
                "date": row["Date"],
                "link": row["Link"]
            } if row else None
        except Exception as e:
            raise e
        finally:
            cur.close()

    
    def close(self):
        self.con.close()