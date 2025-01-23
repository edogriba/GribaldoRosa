from app.models.user import User
from app.db.dbModels.company_db import CompanyDB


class Company(User):
    def __init__(self, id, email, password, companyName, logoPath, description, location):
        super().__init__(id, email, password, "company")
        self.companyName = companyName
        self.logoPath = logoPath
        self.description = description
        self.location = location
    
    #def __repr__(self):
    #    return f"<Company: ({self.id}) {self.companyName}, Email: {self.email}"

    def get_id(self):
        return super().get_id()
    
    def get_email(self):
        return super().get_email()
    
    def get_password(self):
        return super().get_password()
    
    def get_type(self):
        return super().get_type()
    
    def get_companyName(self):
        return self.companyName
    
    def get_logoPath(self):
        return self.logoPath
    
    def get_description(self):
        return self.description
    
    def to_dict(self):
        user_dict = super().to_dict()
        user_dict.update({
            'companyName': self.companyName,
            'logoPath': self.logoPath,
            'description': self.description,
            'location': self.location
        })
        return user_dict

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @staticmethod
    def add(email: str, password: str, companyName: str, logoPath: str, description: str, location: str):
        try:
            # Insert company data into the database
            companyConn = CompanyDB()
            companyId = companyConn.insert(email, password, companyName, logoPath, description, location)

            return Company(companyId, email, password, companyName, logoPath, description, location)
        
        except Exception as e:
            raise e
        
        finally:
            companyConn.close() 
    
    @staticmethod
    def get_by_id(id: int):
        """
        Retrieve a company record by its unique identifier and return it as a Company object.

        :param id: The unique identifier of the company.
        :return: A Company object populated with the retrieved data if found, otherwise None.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            companyConn = CompanyDB()
            companyData = companyConn.get_by_id(id)
            return Company(**companyData) if companyData else None
        except Exception as e:
            raise e
        finally:
            companyConn.close()

    @staticmethod
    def get_by_email(email: str):
        """
        Retrieve a company record by its email and return it as a Company object.

        :param email: The email of the company.
        :return: A Company object populated with the retrieved data if found, otherwise None.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            companyConn = CompanyDB()
            companyData = companyConn.get_by_email(email)
            return Company(**companyData) if companyData else None
        except Exception as e:
            raise e
        finally:
            companyConn.close()

