from app.models.user import User
from app.db.dbModels.university_db import UniverstityDB


class University(User):
    def __init__(self, id, email, password, name, address, websiteURL, description, logoPath):
        super().__init__(id, email, password, "university")
        self.name = name
        self.address = address
        self.websiteURL = websiteURL
        self.description = description
        self.logoPath = logoPath
    
    #def __repr__(self):
    #    return f"<University: ({self.id}) {self.name}, Email: {self.email}"

    def get_id(self):
        return super().get_id()
    
    def get_email(self):
        return super().get_email()
    
    def get_password(self):
        return super().get_password()
    
    def get_type(self):
        return super().get_type()
    
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def get_websiteURL(self):
        return self.websiteURL
    
    def get_description(self):
        return self.description
    
    def get_logoPath(self):
        return self.logoPath

    @staticmethod
    def add(email: str, password: str, name: str, address: str, websiteURL: str, description: str, logoPath: str):
        try:
            # Insert university data into the database
            universityConn = UniverstityDB()
            universityId = universityConn.insert(email, password, name, address, websiteURL, description, logoPath)

            return University(universityId, email, password, name, address, websiteURL, description, logoPath)
        
        except Exception as e:
            raise e
        
        finally:
            universityConn.close()    
        