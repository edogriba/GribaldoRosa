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

    #def __repr__(self):
    #    return f"<User: {self.id}, Email: {self.email}, Type: {self.type}>"
