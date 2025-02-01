from typing import Union
from ..db.dbModels import AssessmentDB

class Assessment:
    def __init__(self, assessmentId: int, applicationId: int, date: str, link: str):
        self.assessmentId = assessmentId
        self.applicationId = applicationId
        self.date = date
        self.link = link

    def get_assessment_id(self) -> int:
        return self.assessmentId
    
    def get_application_id(self) -> int:
        return self.applicationId
    
    def get_date(self) -> str:
        return self.date
    
    def get_link(self) -> str:
        return self.link
    
    def to_dict(self) -> dict:
        return {
            'assessmentId': self.assessmentId,
            'applicationId': self.applicationId,
            'date': self.date,
            'link': self.link
        }
    
    @staticmethod
    def add(applicationId: int, date: str, link: str) -> Union['Assessment', Exception, None]:
        """
        Add a new assessment to the database.

        :param assessmentId: The unique identifier of the assessment.
        :param applicationId: The unique identifier of the application.
        :param date: The date of the assessment.
        :param link: The link to the assessment.
        :return: An Assessment object populated with the inserted data.
        :raises Exception: If an error occurs during the insertion process.
        """
        try:
            assessmentConn = AssessmentDB()
            assessmentId = assessmentConn.insert(applicationId, date, link)
            return Assessment(assessmentId, applicationId, date, link) if assessmentId else None
        except Exception as e:
            raise e
        finally:
            assessmentConn.close()

    @staticmethod
    def get_last_assessment_by_application_id(applicationId: int) -> Union['Assessment', None, Exception]:
        """
        Retrieve the last assessment by application ID.

        :param applicationId: The ID of the application.
        :return: An Assessment object populated with the retrieved data or None if not found.
        :raises Exception: If an error occurs during the retrieval process.
        """
        try:
            assessmentConn = AssessmentDB()
            assessmentData = assessmentConn.get_last_assessment_by_application_id(applicationId)
            return Assessment(**assessmentData) if assessmentData else None
        except Exception as e:
            raise e
        finally:
            assessmentConn.close()