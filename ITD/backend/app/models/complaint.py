from typing import Union
from ..db.dbModels import ComplaintDB


class Complaint():
    def __init__(self, complaintId: int, internshipId: int, sourceId: int, date: str, content: str):
        self.complaintId = complaintId
        self.internshipId = internshipId
        self.sourceId = sourceId
        self.date = date
        self.content = content

    def get_complaint_id(self) -> int:
        return self.complaintId
    
    def get_internship_id(self) -> int:
        return self.internshipId
    
    def get_source_id(self) -> int:
        return self.sourceId
    
    def get_date(self) -> str:
        return self.date
    
    def get_content(self) -> str:
        return self.content
    
    def to_dict(self) -> dict:
        return {
            'complaintId': self.complaintId,
            'internshipId': self.internshipId,
            'sourceId': self.sourceId,
            'date': self.date,
            'content': self.content
        }

    @staticmethod
    def add(internshipId: int, sourceId: int, date: str, content: str) -> Union['Complaint', Exception, None]:
        """
        Add a new complaint to the database.

        :param internshipId: The unique identifier of the internship.
        :param sourceId: The unique identifier of the source.
        :param date: The date of the complaint.
        :param content: The content of the complaint.
        :return: A Complaint object populated with the inserted data.
        :raises Exception: If an error occurs during the insertion process.
        """
        try:
            complaintConn = ComplaintDB()
            complaintId = complaintConn.insert(internshipId, sourceId, date, content)
            return Complaint(complaintId, internshipId, sourceId, date, content) if complaintId else None
        except Exception as e:
            raise e
        finally:
            complaintConn.close()

    
    @staticmethod
    def get_by_internship_id(internshipId: int) -> Union[list, Exception]:
        """
        Retrieve complaints by their internship ID.

        :param internshipId: The ID of the internship.
        :return: A list of Complaint objects.
        :raises Exception: If an error occurs during the database query execution.
        """
        try:
            complaintConn = ComplaintDB()
            complaints = complaintConn.get_by_internship_id(internshipId)
            return [Complaint(**complaint) for complaint in complaints] if complaints else []
        except Exception as e:
            raise e
        finally:
            complaintConn.close()