from flask_jwt_extended import get_current_user
from ..models import Application, InternshipPosition
from ..utils import json_invalid_request, json_unauthorized, json_success, json_created, json_not_found

    # pending -> rejected / accepted -> refused (if accepted) / confirmed (if accepted)
    # confirmed (student), refused (student), pending, rejected (company), accepted (company)

class ApplicationManager:

    def create_application(self, internshipPositionId: int):
        """
        Create a new application.

        :param internshipPositionId: The ID of the internship position.
        :return: JSON response indicating the success or failure of the application creation.
        """
        try:
            validation_response = validate_application_data_creation(internshipPositionId)
            if validation_response is not True:
                return validation_response
    
            Application.add(get_current_user().get_id(), internshipPositionId)

            return json_created("Application created successfully.")
        
        except Exception as e:
            return e
        

    def accept_application(self, applicationId: int, internshipPositionId: int):
        """
        Accept an application.

        :param applicationId: The ID of the application.
        :param internshipPositionId: The ID of the internship position.
        :return: JSON response indicating the success or failure of the application acceptance.
        """
        try:
            application = Application.get_by_id(applicationId)
            internshipPosition = InternshipPosition.get_by_id(internshipPositionId)
            if not application:
                return json_invalid_request("Invalid application Id.")

            if application.get_internshipPositionId() != internshipPositionId:
                return json_invalid_request("Invalid internship position Id.")
            
            if get_current_user().get_id() != internshipPosition.get_companyId():
                return json_unauthorized("Only the company that posted the internship can accept applications.")
            
            if application.is_pending():
                application.accept()
                return json_success("Application accepted successfully.")
            else:
                return json_invalid_request("Invalid application state.")
        
        except Exception as e:
            return e
        

    def reject_application(self, applicationId: int, internshipPositionId: int):
        """
        Reject an application.

        :param applicationId: The ID of the application.
        :param internshipPositionId: The ID of the internship position.
        :return: JSON response indicating the success or failure of the application rejection.
        """
        try:
            application = Application.get_by_id(applicationId)
            internshipPosition = InternshipPosition.get_by_id(internshipPositionId)
            if not application:
                return json_invalid_request("Invalid application Id.")

            if application.get_internshipPositionId() != internshipPositionId:
                return json_invalid_request("Invalid internship position Id.")
            
            if get_current_user().get_id() != internshipPosition.get_companyId():
                return json_unauthorized("Only the company that posted the internship can reject applications.")
            
            if application.is_pending():
                application.reject()
                return json_success("Application rejected successfully.")
            else:
                return json_invalid_request("Invalid application state.")
        
        except Exception as e:
            return e
    

    def confirm_application(self, applicationId: int, internshipPositionId: int):
        """
        Confirm an application.

        :param applicationId: The ID of the application.
        :param internshipPositionId: The ID of the internship position.
        :return: JSON response indicating the success or failure of the application confirmation.
        """
        try:
            application = Application.get_by_id(applicationId)
            if not application:
                return json_invalid_request("Invalid application Id.")

            if application.get_internshipPositionId() != internshipPositionId:
                return json_invalid_request("Invalid internship position Id.")
            
            if get_current_user().get_id() != application.get_studentId():
                return json_unauthorized("Only the student that applied can confirm applications.")
            
            if application.is_accepted():
                application.confirm()
                return json_success("Application confirmed successfully.")
            else:
                return json_invalid_request("Invalid application state.")
        
        except Exception as e:
            return e
        
    
    def refuse_application(self, applicationId: int, internshipPositionId: int):
        """
        Refuse an application.

        :param applicationId: The ID of the application.
        :param internshipPositionId: The ID of the internship position.
        :return: JSON response containing the updated application if the request is successful, 
             or an error message if the request fails
        """
        try:
            application = Application.get_by_id(applicationId)

            if not application:
                return json_invalid_request("Invalid application Id.")

            if application.get_internshipPositionId() != internshipPositionId:
                return json_invalid_request("Invalid internship position Id.")
            
            if get_current_user().get_id() != application.get_studentId():
                return json_unauthorized("Only the student that applied can refuse applications.")
            
            if application.is_accepted():
                application.refuse()
                return json_success("Application refused successfully.")
            else:
                return json_invalid_request("Invalid application state.")
        
        except Exception as e:
            return e
        
        
    def get_application_by_id(self, applicationId: int):
        """
        Get an application by its ID.

        :param applicationId: The ID of the application.
        :return: JSON response containing the application details if the request is successful, 
             or an error message if the request fails
        """
        try:
            application = Application.get_by_id(applicationId)

            if not application:
                return json_not_found("Application not found.")
            
            internshipPosition = application.get_internshipPosition()

            if not internshipPosition:
                return json_not_found("Internship position not found.")

            if get_current_user().get_id() != application.get_studentId() and get_current_user().get_id() != internshipPosition.get_companyId():
                return json_unauthorized("You can only view your own applications.")
            
            return json_success("Application found successfully.", 
                            application          = application.to_dict(),
                            internshipPosition   = internshipPosition.to_dict(),
                            student              = application.get_student().to_dict(),
                            company              = internshipPosition.get_company().to_dict())
            
        except Exception as e:
            return e
        
    
    def get_applications_by_student(self, studentId: int):
        """
        Get all applications by a student.

        :param studentId: The ID of the student.
        :return: JSON response containing the applications if the request is successful, 
             or an error message if the request fails
        """
        try:
            if get_current_user().get_id() != studentId:
                return json_unauthorized("You can only view your own applications.")
            
            applications = Application.get_by_studentId(studentId)
            if applications:
                return json_success("Applications found successfully.",
                                 applications=[{"application": application.to_dict(), 
                                                "internship": application.get_internshipPosition().to_dict(),
                                                "company": application.get_internshipPosition().get_company().to_dict()} for application in applications])
            else:
                return json_not_found("Applications not found.")
        
        except Exception as e:
            return e


    def get_applications_by_internship_position(self, internshipPositionId: int):
        """
        Get all applications by an internship position.

        :param internshipPositionId: The ID of the internship position.
        :return: JSON response containing the applications if the request is successful, 
             or an error message if the request fails
        """
        try:
            if get_current_user().get_id() != InternshipPosition.get_by_id(internshipPositionId).get_companyId():
                return json_unauthorized("You can only view applications for your own internship positions.")
            
            applications = Application.get_by_internshipPositionId(internshipPositionId)
            if applications:
                return json_success("Applications found successfully.",
                                 applications=[{"application": application.to_dict(), 
                                                "student": application.get_student().to_dict()} for application in applications])
            else:
                return json_not_found("Applications not found.")
        
        except Exception as e:
            return e


def validate_application_data_creation(internshipPositionId: int):
    """
    Validate the application data for creation.

    :param internshipPositionId: ID of the internship position
    :return: True if the application data is valid, otherwise a JSON response with an error message
    """
    try:
        if get_current_user().get_type() != "student":
            return json_unauthorized("Only students can create applications.")
        
        internshipPosition = InternshipPosition.get_by_id(internshipPositionId)

        if not internshipPosition:
            return json_invalid_request("Invalid internship position Id.")
        
        if internshipPosition.is_closed():
            return json_invalid_request("Internship position is closed.")
        
        return True
    
    except Exception as e:
        return json_invalid_request("Invalid application data.")

