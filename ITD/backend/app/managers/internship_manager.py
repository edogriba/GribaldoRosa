from flask_jwt_extended import get_current_user
from typing import Union

from ..services.auth_service import *
from ..models import InternshipPosition, Internship, Student, Company, Application, Complaint
from ..utils import json_unauthorized, json_invalid_request, json_not_found, json_created, json_success
from ..services.auth_service import is_id_valid

class InternshipManager:

    def post_internship_position(self, internship_position_data):
        """
        Post a new internship position.

        :param internship_position_data: Dictionary containing the internship position data.
        :return: JSON response containing the newly added internship position if post is successful, 
             or an error message if registration fails
        """
        try:
            if get_current_user().get_type() != "company":
                return json_unauthorized("Only companies can post internships.")
            
            validation_result = validate_internship_position_data(internship_position_data)
            if validation_result is not True:
                return validation_result
            
            InternshipPosition.add(**internship_position_data)

            return json_created("Internship position added successfully.")
        
        except Exception as e:
            raise e
        
        
    def get_internship_position_by_id(self, internshipPositionId: int):
        """
        Get an internship position by its ID.

        :param internshipPositionId: The ID of the internship position.
        :return: JSON response containing the internship details if the request is successful, 
             or an error message if the request fails
        """
        try:
            if not is_id_valid(internshipPositionId):
                return json_invalid_request("Invalid internship position ID.")
            internship_position = InternshipPosition.get_by_id(internshipPositionId)
            if internship_position:
                return json_success("Internship position retrieved successfully.", internship_position = internship_position.to_dict())
            else:
                return json_not_found("Internship not found.")
        
        except Exception as e:
            raise e


    def get_internship_positions_by_company(self, companyId: int):
        """
        Get all internship positions posted by a company.

        :param companyId: The ID of the company.
        :return: JSON response containing the internship positions posted by the company 
            if the request is successful, or an error message if the request fails
        """
        try:
            if not is_id_valid(companyId):
                return json_invalid_request("Invalid company ID.")
            internship_positions = InternshipPosition.get_by_companyId(companyId)
            return json_success("Internship positions retrieved successfully.", 
                                internship_positions = [internship_position.to_dict() for internship_position in internship_positions])
        
        except Exception as e:
            raise e
        

    def close_internship_position(self, internshipPositionId: int):
        """
        Close an internship position.

        :param internshipId: The ID of the internship.
        :return: JSON response containing the status of the internship if the request is successful, 
                 or an error message if the request fails
        """
        try:
            if not is_id_valid(internshipPositionId):
                return json_invalid_request("Invalid internship ID.")
            
            if get_current_user().get_type() != "company":
                return json_unauthorized("Only companies can close internships.")
            
            internship = InternshipPosition.get_by_id(internshipPositionId)
            if not internship:
                return json_not_found("Internship position not found.")
            
            if internship.get_companyId() != get_current_user().get_id():
                return json_unauthorized("You are not authorized to close this internship position.")
            
            internship.close()
            applications = Application.get_by_internshipPositionId(internshipPositionId)
            for application in applications:
                if application.is_pending() or application.is_accepted() or application.is_assessed():
                    application.reject()
            return json_success("Internship position closed successfully.")
        
        except Exception as e:
            raise e
    
    
    def get_internships_preview_by_company(self, companyId: int):
        """
        Get a preview of all internships posted by a company.

        :param companyId: The ID of the company.
        :return: JSON response containing the preview of internships posted by the company if the request is successful, 
                 or an error message if the request fails
        """
        try:
            if not is_id_valid(companyId):
                return json_invalid_request("Invalid company ID.")
            if get_current_user().get_id() != companyId:
                return json_unauthorized("You are not authorized to view internships posted by this company.")
            
            internshipsPreview = Internship.get_preview_by_companyId(companyId)
            return json_success("Internships retrieved successfully.", internshipsPreview = internshipsPreview)
        
        except Exception as e:
            raise e
        
    
    def get_internships_preview_by_student(self, studentId: int):
        """
        Get a preview of all internships applied to by a student.

        :param studentId: The ID of the student.
        :return: JSON response containing the preview of internships applied to by the student if the request is successful, 
                 or an error message if the request fails
        """
        try:
            if not is_id_valid(studentId):
                return json_invalid_request("Invalid student ID.")
            if get_current_user().get_id() != studentId:
                return json_unauthorized("You are not authorized to view internships applied to by this student.")
            
            internshipsPreview = Internship.get_preview_by_studentId(studentId)
            return json_success("Internships retrieved successfully.", internshipsPreview = internshipsPreview)
        
        except Exception as e:
            raise e
        
    
    def get_internships_preview_by_university(self, universityId: int):
        """
        Get a preview of all internships posted by companies that are affiliated with a university.

        :param universityId: The ID of the university.
        :return: JSON response containing the preview of internships posted by companies affiliated with the university 
                 if the request is successful, or an error message if the request fails
        """
        try:
            if not is_id_valid(universityId):
                return json_invalid_request("Invalid university ID.")
            if get_current_user().get_id() != universityId:
                return json_unauthorized("You are not authorized to view internships posted by companies affiliated with this university.")
            
            internshipsPreview = Internship.get_preview_by_universityId(universityId)
            return json_success("Internships retrieved successfully.", internshipsPreview = internshipsPreview)
        
        except Exception as e:
            raise e
        
    
    def get_full_internship_data_by_id(self, internshipId: int):
        """
        Get an internship by its ID.

        :param internshipId: The ID of the internship.
        :return: JSON response containing the full internship details if the request is successful, 
                 or an error message if the request fails
        """
        try:
            if not is_id_valid(internshipId):
                return json_invalid_request("Invalid internship ID.")
            
            internship = Internship.get_by_id(internshipId)
            if not internship:
                return json_not_found("Internship not found.")
            
            internshipPosition = InternshipPosition.get_by_id(internship.get_internshipPositionId())
            if not internshipPosition:
                return json_not_found("Internship position not found.")
            
            application = Application.get_by_id(internship.get_applicationId())
            if not application:
                return json_not_found("Application not found.")
            
            student = Student.get_by_id(application.get_studentId())
            if not student:
                return json_not_found("Student not found.")
            
            company = Company.get_by_id(internshipPosition.get_companyId())
            if not company:
                return json_not_found("Company not found.")
            
            if (get_current_user().get_id() != student.get_id() and 
                get_current_user().get_id() != company.get_id() and 
                get_current_user().get_id() != student.get_universityId()):
                return json_unauthorized("You are not authorized to view this internship.")
            
            complaints = Complaint.get_by_internship_id(internshipId)

            return json_success("Internship retrieved successfully.", 
                                internship = internship.to_dict(),
                                internshipPosition = internshipPosition.to_dict(),
                                application = application.to_dict(),
                                student = student.to_dict(),
                                company = company.to_dict(),
                                complaints = [complaint.to_dict() for complaint in complaints] if complaints else [])
        
        except Exception as e:
            raise e
        
    
    def finish_internship(self, internshipId: int):
        """
        Finish an internship.

        :param internshipId: The ID of the internship.
        :return: JSON response containing the status of the internship if the request is successful, 
                 or an error message if the request fails
        """
        try:
            if not is_id_valid(internshipId):
                return json_invalid_request("Invalid internship ID.")
            
            if get_current_user().get_type() != "company":
                return json_unauthorized("Only companies can finish internships.")
            
            internship = Internship.get_by_id(internshipId)
            if internship:
                if InternshipPosition.get_by_id(internship.get_internshipPositionId()).get_companyId() == get_current_user().get_id():
                    internship.finish()
                    return json_success("Internship finished successfully.")
                else:
                    return json_unauthorized("You are not authorized to finish this internship.")
            else:
                return json_not_found("Internship not found.")
        
        except Exception as e:
            raise e


    def create_complaint(self, complaint_data):
        """
        Create a new complaint.

        :param complaint_data: Dictionary containing the complaint data.
        :return: JSON response containing the newly added complaint if the request is successful, 
                 or an error message if the request fails
        """
        try:
            values = {
                "internshipId": complaint_data.get("internshipId"),
                "date": complaint_data.get("date"),
                "content": complaint_data.get("content")
            }

            internship = Internship.get_by_id(values.get("internshipId"))
            if not internship:
                return json_not_found("Internship not found.")
            
            if (get_current_user().get_id() != Application.get_by_id(internship.get_applicationId()).get_studentId() and 
                get_current_user().get_id() != InternshipPosition.get_by_id(internship.get_internshipPositionId()).get_companyId()):
                return json_unauthorized("You are not authorized to create a complaint for this internship.")
            
            if internship.is_finished():
                return json_invalid_request("You cannot create a complaint for a finished internship.")
            
            complaint = Complaint.add(**values, sourceId = get_current_user().get_id())
            if complaint:
                return json_created("Complaint added successfully.")
            else:
                return json_invalid_request("Invalid complaint data.")
        
        except Exception as e:
            raise e



def validate_internship_position_data(internship_data):
    """
    Validate the internship position data.

    :param internship_data: Dictionary containing internship position data
    :return: True if the internship position data is valid, otherwise a JSON response with an error message
    """
    try:
        if not (internship_data.get("companyId") == get_current_user().get_id()):
            return json_invalid_request("Invalid company ID")
        
        if not is_name_valid(internship_data.get("programName")):
            return json_invalid_request("Invalid program name")
        
        if not is_duration_valid(internship_data.get("duration")):
            return json_invalid_request("Invalid duration")
        
        if not is_location_valid(internship_data.get("location")):
            return json_invalid_request("Invalid location")
    
        if not is_name_valid(internship_data.get("roleTitle")):
            return json_invalid_request("Invalid role title")

        if not is_skills_valid(internship_data.get("skillsRequired")):
            return json_invalid_request("Invalid skills required")

        if not is_compensation_valid(internship_data.get("compensation")):
            return json_invalid_request("Invalid compensation")

        if not is_benefits_valid(internship_data.get("benefits")):
            return json_invalid_request("Invalid benefits")

        if not is_languageSpoken_valid(internship_data.get("languagesRequired")):
            return json_invalid_request("Invalid languages required")
     
        if not is_description_valid(internship_data.get("description")):
            return json_invalid_request("Invalid description")

        return True
    except Exception as e:
        return json_invalid_request("Invalid internship position data")
