from app.db.dbModels.internshipPosition_db import InternshipPositionDB

class InternshipPosition():
    def __init__(self, internshipPositionId, companyId, programName, duration, location, roleTitle, skillsRequired, compensation, benefits, languagesRequired, description, status):
        self.internshipPositionId = internshipPositionId
        self.companyId = companyId
        self.programName = programName
        self.duration = duration
        self.location = location
        self.roleTitle = roleTitle
        self.skillsRequired = skillsRequired
        self.compensation = compensation
        self.benefits = benefits
        self.languagesRequired = languagesRequired
        self.description = description
        self.status = status

    def get_internshipPositionId(self):
        return self.internshipPositionId

    def get_companyId(self):
        return self.companyId

    def get_programName(self):
        return self.programName

    def get_duration(self):
        return self.duration

    def get_location(self):
        return self.location

    def get_roleTitle(self):
        return self.roleTitle

    def get_skillsRequired(self):
        return self.skillsRequired

    def get_compensation(self):
        return self.compensation

    def get_benefits(self):
        return self.benefits

    def get_languagesRequired(self):
        return self.languagesRequired

    def get_description(self):
        return self.description
    
    def get_status(self):
        return self.status

    def to_dict(self):
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
            skillsRequired: str, compensation: int, benefits: str, languagesRequired: str, description: str):
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
                'status': 'open'
            }
            internshipPositionConn = InternshipPositionDB()
            internshipPositionId = internshipPositionConn.insert(**values)
            values.update({'internshipPositionId': internshipPositionId})
            return InternshipPosition(**values)
        except Exception as e:
            raise e
        finally:
            internshipPositionConn.close()

    @staticmethod
    def get_by_id(internshipPositionId):
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
    def get_by_companyId(companyId: int):
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
    def get_by_programName(programName: str):
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

    def close(self):
        """
        Close the internship position.

        :return: True if the internship position is successfully closed, otherwise False.
        :raises Exception: If an error occurs during the update process.
        """
        try:
            internshipPositionConn = InternshipPositionDB()
            return internshipPositionConn.update_status(self.internshipPositionId, status='closed')
        except Exception as e:
            raise e
        finally:
            internshipPositionConn.close()