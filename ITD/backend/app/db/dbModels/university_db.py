from sqlite3 import connect, Row
from .user_db import UserDB
from typing import Optional, Union
from os import getenv
from dotenv import load_dotenv

class UniversityDB:
    def __init__(self):
        load_dotenv()
        self.con = connect(getenv("DATABASE"))
        self.con.row_factory = Row

    def create_table(self):
        try:
            with self.con:
                self.con.execute(""" DROP TABLE IF EXISTS University """)
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
    
    def insert(self, email: str, password: str, name: str, address: str, websiteURL: str, description: str, logoPath: Optional[str]) -> Union[int, Exception, None]:
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
            if str(e) != "UNIQUE constraint failed: User.Email":
                userConn.remove(userId)
            self.con.rollback()
            raise e
        finally:
            userConn.close()
    
    
    #############
    #    GET    #
    ############# 
    def get_by_id(self, id: int) -> Union[dict, None, Exception]:
        """
        Retrieve a university record by its id and return the data as a dictionary.

        :param id: The id of the university.
        :return: A dictionary with university data if found, otherwise None.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT * 
                        FROM University AS Uni JOIN User AS U ON Uni.UserId = U.UserId
                        WHERE U.UserId = ? """
            university = cur.execute(query, (id,)).fetchone()

            return {    'id': university['UserId'], 
                        'email': university['Email'],
                        'password': university['Password'],
                        'name': university['Name'], 
                        'address': university['Address'],
                        'websiteURL': university['WebsiteURL'],
                        'description': university['Description'],
                        'logoPath': university['LogoPath']
                    } if university else None

        except Exception as e:
            self.con.rollback()
            raise e  
        finally:
            cur.close()

    def get_by_email(self, email: str) -> Union[dict, None, Exception]:
        """
        Retrieve a university record by email and return the data as a dictionary.

        :param email: The email address of the university.
        :return: A dictionary with university data if found, otherwise None.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT * 
                        FROM University AS Uni JOIN User AS U ON Uni.UserId = U.UserId
                        WHERE Email = ? """
            university = self.con.execute(query, (email,)).fetchone()

            return {    'id': university['UserId'], 
                        'email': university['Email'],
                        'password': university['Password'],
                        'name': university['Name'], 
                        'address': university['Address'],
                        'websiteURL': university['WebsiteURL'],
                        'description': university['Description'],
                        'logoPath': university['LogoPath']
                    } if university else None 

        except Exception as e:
            self.con.rollback()
            raise e 
        finally:   
            cur.close()
    
    def get_list_dict(self) -> Union[list, None, Exception]:
        """
        Retrieve a simplified list of universities from the database containing only their UserId and Name.
        :return: A list of dictionaries, where each dictionary contains 'id' (UserId) and 'name' (Name) for a university.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ SELECT UserId, Name FROM University """
                universities = cur.execute(query).fetchall()
                result = [{'id': uni['UserId'], 'name': uni['Name']} for uni in universities]
            return result
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    def update(self, id: int, websiteURL: str, description: str, logoPath: Optional[str]) -> Union[None, Exception]:
        """
        Update a university record in the database.
        :param id: The id of the university.
        :param websiteURL: The website URL of the university.
        :param description: The description of the university.
        :param logoPath: The logo path of the university (optional).
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                if logoPath is not None:
                    query = """ UPDATE University 
                                SET WebsiteURL = ?, Description = ?, LogoPath = ? 
                                WHERE UserId = ? """
                    cur.execute(query, (websiteURL, description, logoPath, id))
                else:
                    query = """ UPDATE University 
                                SET WebsiteURL = ?, Description = ? 
                                WHERE UserId = ? """
                    cur.execute(query, (websiteURL, description, id))
                if not cur.rowcount > 0:
                    raise Exception("University not found")
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()

    def close(self):
        self.con.close()    