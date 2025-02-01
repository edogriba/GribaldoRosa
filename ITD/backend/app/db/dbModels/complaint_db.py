from sqlite3 import connect, Row
from typing import Union
from os import getenv
from dotenv import load_dotenv

class ComplaintDB():
    def __init__(self):
        load_dotenv()
        self.con = connect(getenv("DATABASE"))
        self.con.row_factory = Row

    def create_table(self):
        try:
            with self.con:
                self.con.execute(""" DROP TABLE IF EXISTS Complaint """)
                self.con.execute(""" CREATE TABLE IF NOT EXISTS Complaint (
                                        ComplaintId INTEGER PRIMARY KEY AUTOINCREMENT,
                                        InternshipId INTEGER NOT NULL,
                                        SourceId INTEGER NOT NULL,
                                        Date TEXT NOT NULL,
                                        Content TEXT NOT NULL
                                    ); """)
        except Exception as e:
            self.con.rollback()
            raise e
    
    def insert(self, internshipId: int, sourceId: int, date: str, content: str) -> Union[int, None, Exception]:
        """
        Insert a new complaint into the database and return the ID of the inserted row.

        :params internshipId: int, sourceId: int, date: str, content: str.
        :return: The ID of the inserted row.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ INSERT INTO Complaint (InternshipId, SourceId, Date, Content) VALUES (?, ?, ?, ?) """
                cur.execute(query, (internshipId, sourceId, date, content))
                return cur.lastrowid
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    
    #############
    #    GET    #
    #############
    def get_by_internship_id(self, internshipId: int) -> Union[list, Exception]:
        """
        Retrieve complaints by their internship ID.

        :param internshipId: The ID of the internship.
        :return: A list of dictionaries representing the complaints.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT * FROM Complaint WHERE InternshipId = ? """
            rows = cur.execute(query, (internshipId,)).fetchall()
            
            return [
                {
                    "complaintId": row["ComplaintId"],
                    "internshipId": row["InternshipId"],
                    "sourceId": row["SourceId"],
                    "date": row["Date"],
                    "content": row["Content"]
                } for row in rows
            ] if rows else []
        
        except Exception as e:
            raise e
        finally:
            cur.close()

    
    def close(self):
        self.con.close()