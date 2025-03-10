from ..db.dbModels import InternshipPositionDB
from .company import Company
from typing import Optional, Union

class InternshipPosition():
    def __init__(self, internshipPositionId: int, companyId: int, programName: str, duration: int, location: str, roleTitle: str, 
                 skillsRequired: str, compensation: Optional[int], benefits: Optional[str], languagesRequired: str, description: str, status: str):
        self.internshipPositionId = internshipPositionId
        self.companyId = companyId
        self.programName = programName
        self.duration = duration
        self.location = location
        self.roleTitle = roleTitle
        self.skillsRequired = skillsRequired
        self.compensation = compensation        # optional
        self.benefits = benefits                # optional
        self.languagesRequired = languagesRequired
        self.description = description
        self.status = status

    def get_internshipPositionId(self) -> int:
        return self.internshipPositionId

    def get_companyId(self) -> int:
        return self.companyId

    def get_programName(self) -> str:
        return self.programName

    def get_duration(self) -> int:
        return self.duration

    def get_location(self) -> str:
        return self.location

    def get_roleTitle(self) -> str:
        return self.roleTitle

    def get_skillsRequired(self) -> str:
        return self.skillsRequired

    def get_compensation(self) -> Union[int, None]:
        return self.compensation

    def get_benefits(self) -> Union[str, None]:
        return self.benefits

    def get_languagesRequired(self) -> str:
        return self.languagesRequired

    def get_description(self) -> str:
        return self.description
    
    def get_status(self) -> str:
        return self.status

    def to_dict(self) -> dict:
        return {
            'internshipPositionId': self.internshipPositionId,
            'companyId': self.companyId,
            'programName': self.programName,
            'duration': self.duration,
            'location': self.location,
            'roleTitle': self.roleTitle,
            'skillsRequired': self.skillsRequired,
            'compensation': self.compensation,
            'benefits': self.benefits,
            'languagesRequired': self.languagesRequired,
            'description': self.description,
            'status': self.status
        }

    @staticmethod
    def add(companyId: int, programName: str, duration: int, location: str, roleTitle: str, 
            skillsRequired: str, compensation: Optional[int], benefits: Optional[str], languagesRequired: str, description: str) -> Union['InternshipPosition', None, Exception]:
        """
        Adds a new internship position to the database.

        :param companyId: The ID of the company.
        :param programName: The name of the program.
        :param duration: The duration of the internship.
        :param location: The location of the internship.
        :param roleTitle: The title of the role.
        :param skillsRequired: The skills required for the internship.
        :param compensation: The compensation for the internship.
        :param benefits: The benefits of the internship.
        :param languagesRequired: The languages required for the internship.
        :param description: The description of the internship.
        :return: An instance of the InternshipPosition class with the new internship position details.
        :raises Exception: If an error occurs during the insertion process.
        """
        try:
            values = {
                'companyId': companyId,
                'programName': programName,
                'duration': duration,
                'location': location,
                'roleTitle': roleTitle,
                'skillsRequired': skillsRequired,
                'compensation': compensation,
                'benefits': benefits,
                'languagesRequired': languagesRequired,
                'description': description,
                'status': 'Open'
            }
            internshipPositionConn = InternshipPositionDB()
            internshipPositionId = internshipPositionConn.insert(**values)
            values.update({'internshipPositionId': internshipPositionId})
            return InternshipPosition(**values) if internshipPositionId else None
        except Exception as e:
            raise e
        finally:
            internshipPositionConn.close()

    @staticmethod
    def get_by_id(internshipPositionId: int) -> Union['InternshipPosition', None, Exception]:
        """
        Retrieve an internship position by its ID.

        :param internshipPositionId: The ID of the internship position.
        :return: An instance of the InternshipPosition class with the internship position details, otherwise None.
        :raises Exception: If an error occurs during the retrieval process.
        """
        try:
            internshipPositionConn = InternshipPositionDB()
            row = internshipPositionConn.get_by_id(internshipPositionId)
            return InternshipPosition(**row) if row else None
        except Exception as e:
            raise e
        finally:
            internshipPositionConn.close()

    @staticmethod
    def get_by_companyId(companyId: int) -> Union[list, Exception]:
        """
        Retrieve internship positions by their company ID.

        :param companyId: The ID of the company.
        :return: A list of InternshipPosition instances with the internship position details.
        :raises Exception: If an error occurs during the retrieval process.
        """
        try:
            internshipPositionConn = InternshipPositionDB()
            rows = internshipPositionConn.get_by_companyId(companyId)
            return [InternshipPosition(**row) for row in rows] if rows else []
        except Exception as e:
            raise e
        finally:
            internshipPositionConn.close()

    @staticmethod
    def get_by_programName(programName: str) -> Union[list, Exception]:
        """
        Retrieve internship positions by their program name.

        :param programName: The name of the program.
        :return: A list of InternshipPosition instances with the internship position details.
        :raises Exception: If an error occurs during the retrieval process.
        """
        try:
            internshipPositionConn = InternshipPositionDB()
            rows = internshipPositionConn.get_by_program_name(programName)
            return [InternshipPosition(**row) for row in rows] if rows else []
        except Exception as e:
            raise e
        finally:
            internshipPositionConn.close()

    def get_company(self) -> Union[Company, None, Exception]:
        """
        Retrieve the company that posted the internship position.

        :return: An instance of the Company class with the company details, or None if no company is found.
        :raises Exception: If an error occurs during the retrieval process.
        """
        try:
            return Company.get_by_id(self.companyId)
        except Exception as e:
            raise e
        
    def close(self) -> Union[bool, Exception]:
        """
        Close the internship position.

        :return: True if the internship position is successfully closed, otherwise False.
        :raises Exception: If an error occurs during the update process.
        """
        try:
            internshipPositionConn = InternshipPositionDB()
            return internshipPositionConn.update_status(self.internshipPositionId, status='Closed')
        except Exception as e:
            raise e
        finally:
            internshipPositionConn.close()

    def is_open(self) -> bool:
        """
        Check if the internship position is open.

        :return: True if the internship position is open, otherwise False.
        """
        return self.status == 'Open'
    
    def is_closed(self) -> bool:
        """
        Check if the internship position is closed.

        :return: True if the internship position is closed, otherwise False.
        """
        return self.status == 'Closed'
    
    @staticmethod
    def get_role_titles() -> Union[list, Exception]:
        """
        Retrieve the role titles of internship positions.

        :return: A list of role titles.
        :raises Exception: If an error occurs during the retrieval process.
        """
        try:
            internshipPositionConn = InternshipPositionDB()
            return internshipPositionConn.get_role_titles()
        except Exception as e:
            raise e
        finally:
            internshipPositionConn.close()
    
    @staticmethod
    def get_locations() -> Union[list, Exception]:
        """
        Retrieve the locations of internship positions.

        :return: A list of locations.
        :raises Exception: If an error occurs during the retrieval process.
        """
        try:
            internshipPositionConn = InternshipPositionDB()
            return internshipPositionConn.get_locations()
        except Exception as e:
            raise e
        finally:
            internshipPositionConn.close()

    @staticmethod
    def search_internship_positions(filters: dict) -> Union[list, Exception]:
        """
        Search for internship positions based on the given filters.

        :param filters: The filters to search for internship positions.
        :return: A list of InternshipPosition instances with the internship position details.
        :raises Exception: If an error occurs during the search process.
        """
        try:
            internshipPositionConn = InternshipPositionDB()
            rows = internshipPositionConn.search(filters)
            return [InternshipPosition(**row) for row in rows] if rows else []
        except Exception as e:
            raise e
        finally:
            internshipPositionConn.close()
    