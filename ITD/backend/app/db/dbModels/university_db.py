from sqlite3 import connect, Row
from app.db.dbModels.user_db import UserDB

DATABASE = 'app/db/SC.db'

class UniversityDB:
    def __init__(self):
        self.con = connect(DATABASE)
        self.con.row_factory = Row

    def create_table(self):
        try:
            with self.con:
                # self.con.execute(""" DROP TABLE University """)
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
    
    
    #############
    #    GET    #
    ############# 
    def get_by_id(self, id: int):
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

    def get_by_email(self, email: str):
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

    def get_list(self):
        """
        Retrieve a list of all universities from the database.
        :return: A list of rows, where each row represents a university with all its fields.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                query = """ SELECT * FROM University """
                universities = cur.execute(query).fetchall()
            return universities
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()
    
    def get_list_dict(self):
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


    def close(self):
        self.con.close()    