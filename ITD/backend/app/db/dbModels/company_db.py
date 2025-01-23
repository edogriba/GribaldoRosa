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


    #############
    #    GET    #
    ############# 
    def get_by_id(self, id: int):
        """
        Retrieve a company record by its id and return the data as a dictionary.

        :param id: The id of the company.
        :return: A dictionary with company data if found, otherwise None.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            query = """ SELECT * 
                        FROM Company AS C JOIN User AS U ON C.UserId = U.UserId
                        WHERE UserId = ? """
            company = self.con.execute(query, (id,)).fetchone()
            if company:
                return {    'id': company['UserId'], 
                            'email': company['Email'],
                            'password': company['Password'],
                            'companyName': company['CompanyName'], 
                            'logoPath': company['LogoPath'], 
                            'description': company['Description'], 
                            'location': company['Location'], 
                        }
            return None        
        except Exception as e:
            raise e  

    def get_by_email(self, email: str):
        """
        Retrieve a company record by email and return the data as a dictionary.

        :param email: The email address of the company.
        :return: A dictionary with company data if found, otherwise None.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            query = """ SELECT * 
                        FROM Company AS C JOIN User AS U ON C.UserId = U.UserId
                        WHERE Email = ? """
            company = self.con.execute(query, (email,)).fetchone()
            if company:
                return {    'id': company['UserId'], 
                            'email': company['Email'],
                            'password': company['Password'],
                            'companyName': company['CompanyName'], 
                            'logoPath': company['LogoPath'], 
                            'description': company['Description'], 
                            'location': company['Location'], 
                        }
            return None        
        except Exception as e:
            raise e  


    def close(self):
        self.con.close()   