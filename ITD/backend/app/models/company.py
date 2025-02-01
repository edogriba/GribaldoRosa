from app.models.user import User
from app.db.dbModels.company_db import CompanyDB
from typing import Optional, Union


class Company(User):
    def __init__(self, id: int, email: str, password: str, companyName: str, logoPath: Optional[str], description: str, location: str):
        super().__init__(id, email, password, "company")
        self.companyName = companyName
        self.logoPath = logoPath        # optional
        self.description = description
        self.location = location
    
    #def __repr__(self):
    #    return f"<Company: ({self.id}) {self.companyName}, Email: {self.email}"

    def get_id(self) -> int:
        return super().get_id()
    
    def get_email(self) -> str:
        return super().get_email()
    
    def get_password(self) -> str:
        return super().get_password()
    
    def get_type(self) -> str:
        return super().get_type()
    
    def get_companyName(self) -> str:
        return self.companyName
    
    def get_logoPath(self) -> Union[str, None]:
        return self.logoPath
    
    def get_description(self) -> str:
        return self.description
    
    def get_location(self) -> str:
        return self.location
    
    def to_dict(self) -> dict:
        user_dict = super().to_dict()
        user_dict.update({
            'companyName': self.companyName,
            'logoPath': self.logoPath,
            'description': self.description,
            'location': self.location
        })
        return user_dict


    @staticmethod
    def add(email: str, password: str, companyName: str, logoPath: Optional[str], description: str, location: str) -> Union['Company', Exception, None]:
        try:
            # Insert company data into the database
            companyConn = CompanyDB()
            companyId = companyConn.insert(email, password, companyName, logoPath, description, location)
            return Company(companyId, email, password, companyName, logoPath, description, location) if companyId else None
        
        except Exception as e:
            raise e
        
        finally:
            companyConn.close() 
    

    @staticmethod
    def get_by_id(id: int) -> Union['Company', None, Exception]:
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
    def get_by_email(email: str) -> Union['Company', None, Exception]:
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


    @staticmethod
    def get_companies_names() -> Union[list, Exception]:
        """
        Retrieve a list of company names from the database.

        :return: A list of company names.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            companyConn = CompanyDB()
            companyNames = companyConn.get_companies_names()
            return companyNames
        except Exception as e:
            raise e
        finally:
            companyConn.close()

    @staticmethod
    def update(id: int, logoPath: Optional[str], description: str, location: str) -> Union['Company', None, Exception]:
        """
        Update an existing company record in the database and return the updated company data as a dictionary.

        :param id: The unique identifier of the company.
        :param companyName: The name of the company.
        :param logoPath: The path to the company's logo.
        :param description: A description of the company.
        :param location: The location of the company.
        :return: None if the update was successful.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            companyConn = CompanyDB()
            companyConn.update(id, logoPath, description, location)
            companyData = companyConn.get_by_id(id)
            return Company(**companyData) if companyData else None
        except Exception as e:
            raise e
        finally:
            companyConn.close()