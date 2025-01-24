from app.db.dbModels.application_db import ApplicationDB

class Application():
    def __init__(self, applicationId, studentId, internshipPositionId, state):
        self.applicationId = applicationId
        self.studentId = studentId
        self.internshipPositionId = internshipPositionId
        self.state = state

    def get_applicationId(self):
        return self.applicationId

    def get_studentId(self):
        return self.studentId

    def get_internshipPositionId(self):
        return self.internshipPositionId

    def get_state(self):
        return self.state

    def to_dict(self):
        return {
            'applicationId': self.applicationId,
            'studentId': self.studentId,
            'internshipPositionId': self.internshipPositionId,
            'state': self.state,
        }

    @staticmethod
    def add(studentId: int, internshipPositionId: int, state: str):
        """
        Adds a new application to the database.

        :param studentId: The ID of the student applying.
        :param internshipPositionId: The ID of the internship position.
        :param state: The current state of the application.
        :return: An instance of the Application class with the new application details.
        :raises Exception: If an error occurs during the insertion process.
        """
        try:
            values = {
                'studentId': studentId,
                'internshipPositionId': internshipPositionId,
                'state': state,
            }
            applicationConn = ApplicationDB()
            applicationId = applicationConn.insert(**values)
            values.update({'applicationId': applicationId})
            return Application(**values)
        except Exception as e:
            raise e
        finally:
            applicationConn.close()
 
    #############
    #    GET    #
    ############# 
    @staticmethod
    def get_by_id(applicationId: int):
        """
        Retrieve an application record by its unique identifier and return it as an Application object.

        :param applicationId: The unique identifier of the application.
        :return: An Application object populated with the retrieved data if found, otherwise None.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            applicationConn = ApplicationDB()
            applicationData = applicationConn.get_by_id(applicationId)
            return Application(**applicationData) if applicationData else None
        except Exception as e:
            raise e
        finally:
            applicationConn.close()

    @staticmethod
    def get_by_studentId(studentId: int):
        """
        Retrieve a list of application records by the student's unique identifier.

        :param studentId: The unique identifier of the student.
        :return: A list of Application objects populated with the retrieved data.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            applicationConn = ApplicationDB()
            applicationsData = applicationConn.get_by_studentId(studentId)
            return [Application(**data) for data in applicationsData] if applicationsData else []
        except Exception as e:
            raise e
        finally:
            applicationConn.close()

    @staticmethod
    def get_by_internshipPositionId(internshipPositionId: int):
        """
        Retrieve a list of application records by the internship position's unique identifier.

        :param internshipPositionId: The unique identifier of the internship position.
        :return: A list of Application objects populated with the retrieved data.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            applicationConn = ApplicationDB()
            applicationsData = applicationConn.get_by_internshipPositionId(internshipPositionId)
            return [Application(**data) for data in applicationsData] if applicationsData else []
        except Exception as e:
            raise e
        finally:
            applicationConn.close()

    @staticmethod
    def get_by_studentId_internshipPositionId(studentId: int, internshipPositionId: int):
        """
        Retrieve an application record by the student's unique identifier and the internship position's unique identifier.

        :param studentId: The unique identifier of the student.
        :param internshipPositionId: The unique identifier of the internship position.
        :return: An Application object populated with the retrieved data if found, otherwise None.
        :raises Exception: If an error occurs during the query execution.
        """
        try:
            applicationConn = ApplicationDB()
            applicationData = applicationConn.get_by_studentId_internshipPositionId(studentId, internshipPositionId)
            return Application(**applicationData) if applicationData else None
        except Exception as e:
            raise e
        finally:
            applicationConn.close()

    ################
    #    UPDATE    #
    ################
    def update_state(self, state: str):
        """
        Update the state of the application.

        :param state: The new state of the application.
        :raises Exception: If an error occurs during the update process.
        """
        try:
            applicationConn = ApplicationDB()
            applicationConn.update_state(self.applicationId, state)
            self.state = state
        except Exception as e:
            raise e
        finally:
            applicationConn.close()
    
    def accept(self):
        """
        Accept the application by updating its state to "accepted".
        This method changes the state of the application to "accepted", indicating that the application has been approved.

        :raises Exception: If an error occurs during the update process.
        """
        try:
            self.update_state("accepted")
        except Exception as e:
            raise e
    
    def refuse(self):
        """
        Refuse the application by updating its state to "refused".
        This method changes the state of the application to "refused", indicating that the application has been rejected.

        :raises Exception: If an error occurs during the update process.
        """
        self.update_state("refused")

    def pending(self):
        """
        Set the application state to "pending".
        This method changes the state of the application to "pending", indicating that the application is under review.

        :raises Exception: If an error occurs during the update process.
        """
        self.update_state("pending")

    ################
    #   CHECKERS   #
    ################
    def is_accepted(self):
        """
        Check if the application has been accepted.
        
        :return: True if the application state is "accepted", otherwise False.
        """
        return self.state == "accepted"
    
    def is_refused(self):
        """
        Check if the application has been refused.

        :return: True if the application state is "refused", otherwise False.
        """
        return self.state == "refused"
    
    def is_pending(self):
        """
        Check if the application is pending review.

        :return: True if the application state is "pending", otherwise False.
        """
        return self.state == "pending"
