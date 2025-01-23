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
    
    def to_dict(self):
        return {
            'id': int(self.id),
            'email': self.email,
            'type': self.type
        }

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

    @staticmethod        
    def get_type_by_email(email: str):
        """
        Retrieve a user record by email and return the corresponding type.

        :param email: The email address of the user.
        :return: Type of the user, otherwise None.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            userConn = UserDB()
            userType = userConn.get_type_by_email(email)
            return userType
        except Exception as e:
            raise e
        finally:
            userConn.close()

    def check_password(self, password: str):
        """
        Check if the provided password matches the user's password.

        :param password: The password to check.
        :return: True if the password matches, otherwise False.
        """
        return self.password == password

    #def __repr__(self):
    #    return f"<User: {self.id}, Email: {self.email}, Type: {self.type}>"
