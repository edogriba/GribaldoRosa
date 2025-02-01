from app.db.dbModels.application_db import ApplicationDB
from .internshipPosition import InternshipPosition
from .student import Student
from typing import Union

class Application():
    def __init__(self, applicationId: int, studentId: int, internshipPositionId: int, status: str):
        self.applicationId = applicationId
        self.studentId = studentId
        self.internshipPositionId = internshipPositionId
        self.status = status

    def get_applicationId(self) -> int:
        return self.applicationId

    def get_studentId(self) -> int:
        return self.studentId

    def get_internshipPositionId(self) -> int:
        return self.internshipPositionId

    def get_status(self) -> str:
        return self.status

    def to_dict(self) -> dict:
        return {
            'applicationId': self.applicationId,
            'studentId': self.studentId,
            'internshipPositionId': self.internshipPositionId,
            'status': self.status,
        }

    @staticmethod
    def add(studentId: int, internshipPositionId: int) -> Union['Application', Exception, None]:
        """
        Add a new application to the database with a default status of 'Pending'.

        :param studentId: The unique identifier of the student applying.
        :param internshipPositionId: The unique identifier of the internship position.
        :return: An Application object populated with the inserted data.
        :raises Exception: If an error occurs during the insertion process.
        """
        try:
            applicationConn = ApplicationDB()
            applicationId = applicationConn.insert(studentId, internshipPositionId, 'Pending')
            return Application(applicationId, studentId, internshipPositionId, 'Pending') if applicationId else None
        except Exception as e:
            raise e
        finally:
            applicationConn.close()
 
    #############
    #    GET    #
    ############# 
    @staticmethod
    def get_by_id(applicationId: int) -> Union['Application', None, Exception]:
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
    def get_by_studentId(studentId: int) -> Union[list, Exception]:
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
    def get_by_internshipPositionId(internshipPositionId: int) -> Union[list, Exception]:
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
    def get_by_studentId_internshipPositionId(studentId: int, internshipPositionId: int) -> Union['Application', None, Exception]:
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

    def get_internshipPosition(self) -> Union['InternshipPosition', None, Exception]:
        """
        Retrieve the internship position associated with the application.

        :return: An instance of the InternshipPosition class with the internship position details if found or None.
        :raises Exception: If an error occurs during the retrieval process.
        """
        try:
            return InternshipPosition.get_by_id(self.internshipPositionId)
        except Exception as e:
            raise e

    def get_student(self) -> Union['Student', None, Exception]:
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

    def update_status(self, status: str) -> Union[None, Exception]:
        """
        Update the status of the application.

        :param status: The new status of the application.
        :raises Exception: If an error occurs during the update process.
        """
        try:
            applicationConn = ApplicationDB()
            applicationConn.update_status(self.applicationId, status)
            self.status = status
        except Exception as e:
            raise e
        finally:
            applicationConn.close()
    
    def pending(self) -> Union[None, Exception]:
        """
        Set the application status to "Pending".
        This method changes the status of the application to "Pending", indicating that the application is under review.

        :raises Exception: If an error occurs during the update process.
        """
        try:
            self.update_status("Pending")
        except Exception as e:
            raise e

    def accept(self) -> Union[None, Exception]:
        """
        Accept the application by updating its status to "Accepted".
        This method changes the status of the application to "Accepted", indicating that the application has been approved.

        :raises Exception: If an error occurs during the update process.
        """
        try:
            self.update_status("Accepted")
        except Exception as e:
            raise e
        
    def reject(self) -> Union[None, Exception]:
        """
        Reject the application by updating its status to "Rejected".
        This method changes the status of the application to "Rejected", indicating that the application has been denied.

        :raises Exception: If an error occurs during the update process.
        """
        try:
            self.update_status("Rejected")
        except Exception as e:
            raise e
    
    def confirm(self) -> Union[None, Exception]:
        """
        Confirm the application by updating its status to "Confirmed".
        This method changes the status of the application to "Confirmed", indicating that the application has been approved and confirmed.

        :raises Exception: If an error occurs during the update process.
        """
        try:
            self.update_status("Confirmed")
        except Exception as e:
            raise e
        
    def refuse(self) -> Union[None, Exception]:
        """
        Refuse the application by updating its status to "Refused".
        This method changes the status of the application to "Refused", indicating that the application has been rejected.

        :raises Exception: If an error occurs during the update process.
        """
        try:
            self.update_status("Refused")
        except Exception as e:
            raise e  

    def access(self) -> Union[None, Exception]:
        """
        Access the application by updating its status to "Accessed".
        This method changes the status of the application to "Accessed", indicating that the application has been accessed.

        :raises Exception: If an error occurs during the update process.
        """
        try:
            self.update_status("Accessed")
        except Exception as e:
            raise e


    ################
    #   CHECKERS   #
    ################

    def is_pending(self) -> bool:
        """
        Check if the application is pending review.

        :return: True if the application status is "Pending", otherwise False.
        """
        return self.status == "Pending"
    
    def is_accessed(self) -> bool:
        """
        Check if the application has been accessed.
        
        :return: True if the application status is "Accessed", otherwise False.
        """
        return self.status == "Accessed"
    
    def is_accepted(self) -> bool:
        """
        Check if the application has been accepted.
        
        :return: True if the application status is "Accepted", otherwise False.
        """
        return self.status == "Accepted"
    
    def is_rejected(self) -> bool:
        """
        Check if the application has been rejected.

        :return: True if the application status is "Rejected", otherwise False.
        """
        return self.status == "Rejected"
    
    def is_confirmed(self) -> bool:
        """
        Check if the application has been confirmed.

        :return: True if the application status is "Confirmed", otherwise False.
        """
        return self.status == "Confirmed"
    
    def is_refused(self) -> bool:
        """
        Check if the application has been refused.

        :return: True if the application status is "Refused", otherwise False.
        """
        return self.status == "Refused"
