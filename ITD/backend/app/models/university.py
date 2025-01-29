from app.models.user import User
from app.db.dbModels.university_db import UniversityDB
from typing import Optional, Union


class University(User):
    def __init__(self, id: int, email: str, password: str, name: str, address: str, websiteURL: str, description: str, logoPath: Optional[str]):
        super().__init__(id, email, password, "university")
        self.name = name
        self.address = address
        self.websiteURL = websiteURL
        self.description = description
        self.logoPath = logoPath        # optional
    
    #def __repr__(self):
    #    return f"<University: ({self.id}) {self.name}, Email: {self.email}"

    def get_id(self) -> int:
        return super().get_id()
    
    def get_email(self) -> str:
        return super().get_email()
    
    def get_password(self) -> str:
        return super().get_password()
    
    def get_type(self) -> str:
        return super().get_type()
    
    def get_name(self) -> str:
        return self.name
    
    def get_address(self) -> str:
        return self.address
    
    def get_websiteURL(self) -> str:
        return self.websiteURL
    
    def get_description(self) -> str:
        return self.description
    
    def get_logoPath(self) -> Union[str, None]:
        return self.logoPath

    def to_dict(self) -> dict:
        user_dict = super().to_dict()
        user_dict.update({
            'name': self.name,
            'address': self.address,
            'websiteURL': self.websiteURL,
            'description': self.description,
            'logoPath': self.logoPath,
        })
        return user_dict
    

    @staticmethod
    def add(email: str, password: str, name: str, address: str, websiteURL: str, description: str, logoPath: Optional[str]) -> Union['University', Exception, None]:
        try:
            # Insert university data into the database
            universityConn = UniversityDB()
            universityId = universityConn.insert(email, password, name, address, websiteURL, description, logoPath)
            if universityId is None:
                return None
            return University(universityId, email, password, name, address, websiteURL, description, logoPath)
        
        except Exception as e:
            raise e
        
        finally:
            universityConn.close()    
    

    @staticmethod
    def get_list_dict() -> Union[list, Exception, None]:
        """
        Retrieve a simplified list of universities from the database containing only their UserId and Name.
        :return: A list of dictionaries, where each dictionary contains 'id' (UserId) and 'name' (Name) for a university.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            universityConn = UniversityDB()
            universities = universityConn.get_list_dict()
            return universities
        except Exception as e:
            raise e
        finally:
            universityConn.close()
    

    @staticmethod
    def get_by_id(id: int) -> Union['University', Exception, None]:
        """
        Retrieve a university record by its unique identifier and return it as a University object.

        :param id: The unique identifier of the university.
        :return: A University object populated with the retrieved data if found, otherwise None.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            uniConn = UniversityDB()
            uniData = uniConn.get_by_id(id)
            return University(**uniData) if uniData else None
        except Exception as e:
            raise e
        finally:
            uniConn.close()


    @staticmethod
    def get_by_email(email: str) -> Union['University', Exception, None]:
        """
        Retrieve a university record by its email and return it as a University object.

        :param email: The email of the university.
        :return: A University object populated with the retrieved data if found, otherwise None.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            uniConn = UniversityDB()
            uniData = uniConn.get_by_email(email)
            return University(**uniData) if uniData else None
        except Exception as e:
            raise e
        finally:
            uniConn.close()
