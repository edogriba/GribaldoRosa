from sqlite3 import connect, Row
from app.db.dbModels.user_db import UserDB

DATABASE = 'app/db/SC.db'

class UniverstityDB:
    def __init__(self):
        self.con = connect(DATABASE)
        self.con.row_factory = Row

    def create_table(self):
        try:
            with self.con:
                # self.con.execute(""" DROP TABLE Student """)
                self.con.execute(""" CREATE TABLE IF NOT EXISTS University (
                                        UserId INTEGER PRIMARY KEY,
                                        Name TEXT NOT NULL,
                                        Address TEXT NOT NULL,
                                        WebsiteURL TEXT NOT NULL,
                                        Description TEXT NOT NULL,
                                        LogoPath TEXT,
                                        FOREIGN KEY (UserId) REFERENCES User(UserId)
                                ); """)
        except Exception as e:
            self.con.rollback()
            raise e

    
    def insert(self, email: str, password: str, name: str, address: str, websiteURL: str, description: str, logoPath: str):
        """
        Insert a new university into the database and return the ID of the inserted row.
        :param item: A tuple containing (email: str, password: str, name: str, address: str, websiteURL: str, description: str, logoPath: str).
        :return: The ID of the inserted row.
        """
        try:
            userConn = UserDB()
            userId = userConn.insert(email, password, "university")
            with self.con:
                query = """ INSERT INTO University (UserId, Name, Address, WebsiteURL, Description, LogoPath) VALUES (?, ?, ?, ?, ?, ?) """
                self.con.execute(query, (userId, name, address, websiteURL, description, logoPath))
            return userId
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            userConn.close()


    def close(self):
        self.con.close()    