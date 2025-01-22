from sqlite3 import connect, Row
from app.db.dbModels.user_db import UserDB
from app.utils.error_handler import handle_database_error

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
        :raises Exception: If an error occurs during the query execution.
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
    
    def get_list(self):
        """
        Retrieve a list of all universities from the database.
        :return: A list of rows, where each row represents a university with all its fields.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            with self.con:
                query = """ SELECT * FROM University """
                universities = self.con.execute(query).fetchall()
            return universities
        except Exception as e:
            self.con.rollback()
            raise e
    
    def get_list_dict(self):
        """
        Retrieve a simplified list of universities from the database containing only their UserId and Name.
        :return: A list of dictionaries, where each dictionary contains 'id' (UserId) and 'name' (Name) for a university.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            with self.con:
                query = """ SELECT UserId, Name FROM University """
                universities = self.con.execute(query).fetchall()
                result = [{'id': uni['UserId'], 'name': uni['Name']} for uni in universities]
            return result
        except Exception as e:
            self.con.rollback()
            raise e


    def close(self):
        self.con.close()    