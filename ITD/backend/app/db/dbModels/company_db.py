from sqlite3 import connect, Row
from .user_db import UserDB
from typing import Optional, Union
from os import getenv
from dotenv import load_dotenv

class CompanyDB:
    def __init__(self):
        load_dotenv()
        self.con = connect(getenv("DATABASE"))
        self.con.row_factory = Row

    def create_table(self):
        try:
            with self.con:
                self.con.execute(""" DROP TABLE IF EXISTS Company """)
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
    
    def insert(self, email: str, password: str, companyName: str, logoPath: Optional[str], description: str, location: str) -> Union[int, None, Exception]:
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
                cur = self.con.cursor()
                query = """ INSERT INTO Company (UserId, CompanyName, LogoPath, Description, Location) VALUES (?, ?, ?, ?, ?) """
                cur.execute(query, (userId, companyName, logoPath, description, location))
                cur.close()
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
        Retrieve a company record by its id and return the data as a dictionary.

        :param id: The id of the company.
        :return: A dictionary with company data if found, otherwise None.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT * 
                        FROM Company AS C JOIN User AS U ON C.UserId = U.UserId
                        WHERE C.UserId = ? """
            company = cur.execute(query, (id,)).fetchone()

            return {    'id': company['UserId'], 
                        'email': company['Email'],
                        'password': company['Password'],
                        'companyName': company['CompanyName'], 
                        'logoPath': company['LogoPath'], 
                        'description': company['Description'], 
                        'location': company['Location'], 
                    } if company else None
        

        except Exception as e:
            self.con.rollback()
            raise e  
        finally:
            cur.close()

    def get_by_email(self, email: str) -> Union[dict, None, Exception]:
        """
        Retrieve a company record by email and return the data as a dictionary.

        :param email: The email address of the company.
        :return: A dictionary with company data if found, otherwise None.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT * 
                        FROM Company AS C JOIN User AS U ON C.UserId = U.UserId
                        WHERE Email = ? """
            company = cur.execute(query, (email,)).fetchone()

            return {    'id': company['UserId'], 
                        'email': company['Email'],
                        'password': company['Password'],
                        'companyName': company['CompanyName'], 
                        'logoPath': company['LogoPath'], 
                        'description': company['Description'], 
                        'location': company['Location'], 
                    } if company else None

        except Exception as e:
            self.con.rollback()
            raise e  
        finally:
            cur.close()

    
    def get_companies_names(self) -> Union[list, Exception]:
        """
        Retrieve the names of all companies in the database.
        :return: A list of dictionaries containing the 'name' of each company.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            cur = self.con.cursor()
            query = """ SELECT DISTINCT CompanyName FROM Company """
            rows = cur.execute(query).fetchall()
            return [row["CompanyName"] for row in rows] if rows else []
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()


    def update(self, id: int, logoPath: Optional[str], description: str, location: str) -> Union[None, Exception]:
        """
        Update a company record in the database.
        :param id: The id of the company.
        :param logoPath: The path to the company's logo.
        :param description: The description of the company.
        :param location: The location of the company.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            with self.con:
                cur = self.con.cursor()
                if logoPath is not None:
                    query = """ UPDATE Company 
                                SET LogoPath = ?, Description = ?, Location = ?
                                WHERE UserId = ? """
                    cur.execute(query, (logoPath, description, location, id))
                else:
                    query = """ UPDATE Company 
                                SET Description = ?, Location = ?
                                WHERE UserId = ? """
                    cur.execute(query, (description, location, id))
                if not cur.rowcount > 0:
                    raise Exception("Company not found")
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            cur.close()


    def close(self):
        self.con.close()   