from sqlite3 import connect, Row
from os import getenv
from dotenv import load_dotenv
from typing import Union

class UserDB:
    def __init__(self):
        load_dotenv()
        self.con = connect(getenv("DATABASE"))
        self.con.row_factory = Row

    def create_table(self):
        try:
            with self.con:
                self.con.execute(""" DROP TABLE IF EXISTS User """)
                self.con.execute(""" CREATE TABLE IF NOT EXISTS User (
                                            UserId INTEGER PRIMARY KEY AUTOINCREMENT,
                                            Email TEXT NOT NULL UNIQUE,
                                            Password TEXT NOT NULL,
                                            Type TEXT NOT NULL 
                                    ); """)
        except Exception as e:
            self.con.rollback()
            raise e
    
    def insert(self, email: str, password: str, type: str) -> Union[int, None, Exception]:
        """
        Insert a new user into the database and return the ID of the inserted row.
        :param items: email: str, password: str, type: str).
        :return: The ID of the inserted row.
        :raises Exception: If an error occurs during the query execution.
        """
        if not self.is_email_unique(email):
            raise ValueError("UNIQUE constraint failed: User.Email")
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ INSERT INTO User (Email, Password, Type) VALUES (?, ?, ?) """
                cur.execute(query, (email, password, type))
                return cur.lastrowid
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    def remove(self, id: int) -> Union[None, Exception]:
        """
        Remove a user from the database by its ID.

        :param id: The ID of the user to remove.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = " DELETE FROM User WHERE UserId = ? "
                cur.execute(query, (id,))
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    def is_email_unique(self, email: str) -> bool:
        """
        Check if the provided email is unique in the Users table.

        :param email: The email address to check.
        :return: True if the email is unique (not present in the Users table), otherwise False.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = " SELECT * FROM User WHERE Email = ?"
                row = cur.execute(query, (email,)).fetchone()
                return row[0] == 0 if row else True
        except Exception as e:
            self.con.rollback()
            return True
        finally:
            cur.close()

    def get_type_by_email(self, email: str) -> Union[str, None, Exception]:
        """
        Retrieve the user's type by its email.

        :param email: The unique email of the user.
        :return: The type representing the user if found, otherwise None.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ SELECT Type 
                            FROM User
                            WHERE Email = ? """
                user = cur.execute(query, (email,)).fetchone()
            return user['Type'] if user else None

        except Exception as e:
            self.con.rollback()
            raise e 
        finally:
            cur.close()

    def get_type_by_id(self, id: str) -> Union[str, None, Exception]:
        """
        Retrieve the user's type by its ID.

        :param id: The unique ID of the user.
        :return: The type representing the user if found, otherwise None.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ SELECT Type 
                            FROM User
                            WHERE UserId = ? """
                user = cur.execute(query, (id,)).fetchone()
            return user['Type'] if user else None

        except Exception as e:
            self.con.rollback()
            raise e 
        finally:
            cur.close()
     
    def close(self):
        self.con.close()