from flask_login import UserMixin
from app.db.dbModels.user_db import UserDB

DATABASE = 'app/SC.db'

class User(UserMixin):
    def __init__(self, id, email, password, type):
        self.id = id
        self.email = email
        self.password = password
        self.type = type
        
    def get_id(self):
        return self.id
    
    def get_type(self):
        return self.type

    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password
    
    @staticmethod
    def is_email_unique(email: str):
        """
        Check if the provided email is unique in the Users table.

        :param email: The email address to check.
        :return: True if the email is unique (not present in the Users table), otherwise False.
        :raises Exception: If an error occurs during the database query execution.
        """        
        try:
            userConn = UserDB()
            return userConn.is_email_unique(email)
        except Exception as e:
            raise e
        finally:
            userConn.close()
            
    def get_by_email(self, email: str):
        """
        Retrieve a user by its email.

        :param email: The unique email of the user.
        :return: A tuple representing the user record if found, otherwise None.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            with self.con:
                query = """ SELECT * 
                            FROM User
                            WHERE Email = ? """
                user = self.con.execute(query, (email,)).fetchone()
            return user if user else None
        except Exception as e:
            self.con.rollback()
            raise e  

    def check_password(self, password: str):
        """
        Check if the provided password matches the user's password.

        :param password: The password to check.
        :return: True if the password matches, otherwise False.
        """
        return self.password == password

    #def __repr__(self):
    #    return f"<User: {self.id}, Email: {self.email}, Type: {self.type}>"
