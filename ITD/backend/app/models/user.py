from flask_login import UserMixin

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

    #def __repr__(self):
    #    return f"<User: {self.id}, Email: {self.email}, Type: {self.type}>"
