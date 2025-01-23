from sqlite3 import connect, Row
from app.utils.error_handler import handle_database_error
from student_db import StudentDB
from university_db import UniverstityDB
from company_db import CompanyDB

DATABASE = 'app/db/SC.db'

class UserDB:
    def __init__(self):
        self.con = connect(DATABASE)
        self.con.row_factory = Row

    def create_table(self):
        try:
            with self.con:
                # self.con.execute(""" DROP TABLE User """)
                self.con.execute(""" CREATE TABLE IF NOT EXISTS User (
                                            UserId INTEGER PRIMARY KEY AUTOINCREMENT,
                                            Email TEXT NOT NULL UNIQUE,
                                            Password TEXT NOT NULL,
                                            Type TEXT NOT NULL 
                                    ); """)
        except Exception as e:
            self.con.rollback()
            raise e
    
    def insert(self, email: str, password: str, type: str):
        """
        Insert a new user into the database and return the ID of the inserted row.
        :param items: email: str, password: str, type: str).
        :return: The ID of the inserted row.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ INSERT INTO User (Email, Password, Type) VALUES (?, ?, ?) """
                cur.execute(query, (email, password, type))
                return cur.lastrowid
        except Exception as e:
            self.con.rollback()
            raise handle_database_error(e)
        finally:
            cur.close()

    def is_email_unique(self, email: str):
        """
        Check if the provided email is unique in the Users table.

        :param email: The email address to check.
        :return: True if the email is unique (not present in the Users table), otherwise False.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                query = " SELECT COUNT(*) FROM Users WHERE Email = ?"
                row = self.con.execute(query, (email,)).fetchone()
                return row[0] == 0 if row else True
        except Exception as e:
            self.con.rollback()
            raise e

    def get_type_by_email(self, email: str):
        """
        Retrieve the user's type by its email.

        :param email: The unique email of the user.
        :return: The type representing the user if found, otherwise None.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                query = """ SELECT Type 
                            FROM User
                            WHERE Email = ? """
                user = self.con.execute(query, (email,)).fetchone()
            return user if user else None
        except Exception as e:
            self.con.rollback()
            raise e 
     
    def close(self):
        self.con.close()