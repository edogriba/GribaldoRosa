from sqlite3 import connect, Row
from app.db.dbModels.user_db import UserDB

DATABASE = 'app/db/SC.db'

class CompanyDB:
    def __init__(self):
        self.con = connect(DATABASE)
        self.con.row_factory = Row

    def create_table(self):
        try:
            with self.con:
                # self.con.execute(""" DROP TABLE Company """)
                self.con.execute(""" CREATE TABLE IF NOT EXISTS Company (
                                        UserId INTEGER PRIMARY KEY,
                                        CompanyName TEXT NOT NULL,
                                        LogoPath TEXT,
                                        Description TEXT NOT NULL,
                                        Location TEXT NOT NULL,
                                        FOREIGN KEY (UserId) REFERENCES User(UserId)
                                ); """)
        except Exception as e:
            self.con.rollback()
            raise e
    
    def insert(self, email: str, password: str, companyName: str, logoPath: str, description: str, location: str):
        """
        Insert a new company into the database and return the ID of the inserted row.
        :param item: A tuple containing (email: str, password: str, companyName: str, logoPath: str, description: str, location: str).
        :return: The ID of the inserted row.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            userConn = UserDB()
            userId = userConn.insert(email, password, "company")
            with self.con:
                query = """ INSERT INTO Company (UserId, CompanyName, LogoPath, Description, Location) VALUES (?, ?, ?, ?, ?) """
                self.con.execute(query, (userId, companyName, logoPath, description, location))
            return userId
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            userConn.close()

    def close(self):
        self.con.close()   