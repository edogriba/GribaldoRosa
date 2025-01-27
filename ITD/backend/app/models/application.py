from app.db.dbModels.application_db import ApplicationDB
from .internshipPosition import InternshipPosition
from .student import Student

class Application():
    def __init__(self, applicationId: int, studentId: int, internshipPositionId: int, state: str):
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
    def add(studentId: int, internshipPositionId: int):
        """
        Add a new application to the database with a default state of 'Pending'.

        :param studentId: The unique identifier of the student applying.
        :param internshipPositionId: The unique identifier of the internship position.
        :raises Exception: If an error occurs during the insertion process.
        """
        try:
            applicationConn = ApplicationDB()
            applicationConn.insert(studentId, internshipPositionId, 'Pending')
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

    def get_internshipPosition(self):
        """
        Retrieve the internship position associated with the application.

        :return: An instance of the InternshipPosition class with the internship position details if found or None.
        :raises Exception: If an error occurs during the retrieval process.
        """
        try:
            return InternshipPosition.get_by_id(self.internshipPositionId)
        except Exception as e:
            raise e

    def get_student(self):
        """
        Retrieve the student associated with the application.

        :return: An instance of the Student class with the student details if found or None.
        :raises Exception: If an error occurs during the retrieval process.
        """
        try:
            return Student.get_by_id(self.studentId)
        except Exception as e:  
            raise e
          
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
    
    def pending(self):
        """
        Set the application state to "Pending".
        This method changes the state of the application to "Pending", indicating that the application is under review.

        :raises Exception: If an error occurs during the update process.
        """
        self.update_state("Pending")

    def accept(self):
        """
        Accept the application by updating its state to "Accepted".
        This method changes the state of the application to "Accepted", indicating that the application has been approved.

        :raises Exception: If an error occurs during the update process.
        """
        try:
            self.update_state("Accepted")
        except Exception as e:
            raise e
        
    def reject(self):
        """
        Reject the application by updating its state to "Rejected".
        This method changes the state of the application to "Rejected", indicating that the application has been denied.

        :raises Exception: If an error occurs during the update process.
        """
        try:
            self.update_state("Rejected")
        except Exception as e:
            raise e
    
    def confirm(self):
        """
        Confirm the application by updating its state to "Confirmed".
        This method changes the state of the application to "Confirmed", indicating that the application has been approved and confirmed.

        :raises Exception: If an error occurs during the update process.
        """
        try:
            self.update_state("Confirmed")
        except Exception as e:
            raise e
        
    def refuse(self):
        """
        Refuse the application by updating its state to "Refused".
        This method changes the state of the application to "Refused", indicating that the application has been rejected.

        :raises Exception: If an error occurs during the update process.
        """
        self.update_state("Refused")


    ################
    #   CHECKERS   #
    ################

    def is_pending(self):
        """
        Check if the application is pending review.

        :return: True if the application state is "Pending", otherwise False.
        """
        return self.state == "Pending"
    
    def is_accepted(self):
        """
        Check if the application has been accepted.
        
        :return: True if the application state is "Accepted", otherwise False.
        """
        return self.state == "Accepted"
    
    def is_rejected(self):
        """
        Check if the application has been rejected.

        :return: True if the application state is "Rejected", otherwise False.
        """
        return self.state == "Rejected"
    
    def is_confirmed(self):
        """
        Check if the application has been confirmed.

        :return: True if the application state is "Confirmed", otherwise False.
        """
        return self.state == "Confirmed"
    
    def is_refused(self):
        """
        Check if the application has been refused.

        :return: True if the application state is "Refused", otherwise False.
        """
        return self.state == "Refused"
