from sqlite3 import connect, Row
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
            raise e
        finally:
            cur.close()
    
    def close(self):
        self.con.close()