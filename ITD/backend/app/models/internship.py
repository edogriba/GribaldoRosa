from app.db.dbModels.internship_db import InternshipDB

class Internship():
    def __init__(self, internshipId: int, internshipPositionId: int, applicationId: int, status: str):
        self.internshipId = internshipId
        self.internshipPositionId = internshipPositionId
        self.applicationId = applicationId
        self.status = status

    def get_internshipId(self):
        return self.internshipId

    def get_internshipPositionId(self):
        return self.internshipPositionId

    def get_applicationId(self):
        return self.applicationId

    def get_status(self):
        return self.status

    def to_dict(self):
        return {
            'internshipId': self.internshipId,
            'internshipPositionId': self.internshipPositionId,
            'applicationId': self.applicationId,
            'status': self.status,
        }

    @staticmethod
    def add(internshipPositionId: int, applicationId: int):
        """
        Adds a new internship to the database.

        :param internshipPositionId: The ID of the internship position.
        :param applicationId: The ID of the application.
        :param status: The current status of the internship.
        :return: An instance of the Internship class with the new internship details.
        :raises Exception: If an error occurs during the insertion process.
        """
        try:
            values = {
                'internshipPositionId': internshipPositionId,
                'applicationId': applicationId,
                'status': 'Ongoing',
            }
            internshipConn = InternshipDB()
            internshipId = internshipConn.insert(**values)
            values.update({'internshipId': internshipId})
            return Internship(**values)
        except Exception as e:
            raise e
        finally:
            internshipConn.close()

    #############
    #    GET    #
    #############

    @staticmethod
    def get_by_id(internshipId: int):
        """
        Retrieve an internship by its ID.

        :param internshipId: The ID of the internship.
        :return: An instance of the Internship class with the internship details, otherwise None.
        :raises Exception: If an error occurs during the retrieval process.
        """
        try:
            internshipConn = InternshipDB()
            row = internshipConn.get_by_id(internshipId)
            return Internship(**row) if row else None
        except Exception as e:
            raise e
        finally:
            internshipConn.close()

    @staticmethod
    def get_by_applicationId(applicationId: int):
        """
        Retrieve internships by their application ID.

        :param applicationId: The ID of the application.
        :return: A list of Internship instances with the internship details.
        :raises Exception: If an error occurs during the retrieval process.
        """
        try:
            internshipConn = InternshipDB()
            rows = internshipConn.get_by_application_id(applicationId)
            return [Internship(**row) for row in rows] if rows else []
        except Exception as e:
            raise e
        finally:
            internshipConn.close()

    @staticmethod
    def get_by_internshipPositionId(internshipPositionId: int):
        """
        Retrieve internships by their position ID.

        :param internshipPositionId: The ID of the internship position.
        :return: A list of Internship instances with the internship details.
        :raises Exception: If an error occurs during the retrieval process.
        """
        try:
            internshipConn = InternshipDB()
            rows = internshipConn.get_by_internshipPosition_id(internshipPositionId)
            return [Internship(**row) for row in rows] if rows else []
        except Exception as e:
            raise e
        finally:
            internshipConn.close()

    @staticmethod
    def get_by_applicationId_internshipPositionId(applicationId: int, internshipPositionId: int):
        """
        Retrieve an internship by its application ID and internship position ID.

        :param applicationId: The ID of the application.
        :param internshipPositionId: The ID of the internship position.
        :return: An instance of the Internship class with the internship details, otherwise None.
        :raises Exception: If an error occurs during the retrieval process.
        """
        try:
            internshipConn = InternshipDB()
            row = internshipConn.get_by_applicationId_internshipPositionId(applicationId, internshipPositionId)
            return Internship(**row) if row else None
        except Exception as e:
            raise e
        finally:
            internshipConn.close()

    #############
    #   UPDATE  #
    #############
    def update_status(self, status: str):
        """
        Update the status of the internship.

        :param status: The new status of the internship.
        :return: An instance of the Internship class with the updated status.
        :raises Exception: If an error occurs during the update process.
        """
        try:
            internshipConn = InternshipDB()
            internshipConn.update_status(self.internshipId, status)
            self.status = status
            return self
        except Exception as e:
            raise e
        finally:
            internshipConn.close()

    def make_ongoing(self):
        """
        Update the status of the internship to ongoing.

        :raises Exception: If an error occurs during the update process.
        """
        try:
            self.update_status('Ongoing')
        except Exception as e:
            raise e
        
    def make_completed(self):
        """
        Update the status of the internship to completed.

        :raises Exception: If an error occurs during the update process.
        """
        try:
            self.update_status('Completed')
        except Exception as e:
            raise e
        
    ################
    #   CHECKERS   #
    ################
    def is_ongoing(self):
        """
        Check if the internship is ongoing.

        :return: True if the internship is ongoing, otherwise False.
        """
        return self.status == 'Ongoing'
    
    def is_completed(self):
        """
        Check if the internship is completed.

        :return: True if the internship is completed, otherwise False.
        """
        return self.status == 'Completed'
    