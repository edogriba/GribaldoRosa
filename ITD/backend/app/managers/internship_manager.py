from flask import jsonify
from flask_jwt_extended import get_current_user

from ..services.auth_service import *
from ..models import InternshipPosition
from ..utils import json_unauthorized, json_invalid_request, json_not_found, json_created, json_success

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
            
            internship_position = InternshipPosition.add(**internship_position_data)

            return json_created("Internship position added successfully.", internship_position = internship_position.to_dict())
        
        except Exception as e:
            return e
        
        
    def get_internship_position_by_id(self, internshipPositionId: int):
        """
        Get an internship position by its ID.

        :param internshipPositionId: The ID of the internship position.
        :return: JSON response containing the internship details if the request is successful, 
             or an error message if the request fails
        """
        try:
            internship_position = InternshipPosition.get_by_id(internshipPositionId)
            if internship_position:
                return json_success(internship_position = internship_position.to_dict())
            else:
                return json_not_found("Internship not found.")
        
        except Exception as e:
            return e


    def get_internship_positions_by_company(self, companyId: int):
        """
        Get all internship positions posted by a company.

        :param companyId: The ID of the company.
        :return: JSON response containing the internship positions posted by the company 
            if the request is successful, or an error message if the request fails
        """
        try:
            internship_positions = InternshipPosition.get_by_companyId(companyId)
            return json_success(internship_positions = [internship_position.to_dict() for internship_position in internship_positions])
        
        except Exception as e:
            return e
        

    def close_internship_position(self, internshipId: int):
        """
        Close an internship position.

        :param internshipId: The ID of the internship.
        :return: JSON response containing the status of the internship if the request is successful, 
                 or an error message if the request fails
        """
        try:
            if get_current_user().get_type() != "company":
                return json_unauthorized("Only companies can close internships.")
            
            internship = InternshipPosition.get_by_id(internshipId)
            if internship:
                if internship.get_companyId() == get_current_user().get_id():
                    internship.close()
                    return json_success("Internship position closed successfully.")
                else:
                    return json_unauthorized("You are not authorized to close this internship.")
            else:
                return json_not_found("Internship not found.")
        
        except Exception as e:
            return e
        


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
        print(f"Error: {e}")
        return json_invalid_request("Invalid internship position data")
