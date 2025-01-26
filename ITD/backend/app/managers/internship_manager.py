from flask import jsonify
from flask_jwt_extended import get_current_user

from ..services.auth_service import *
from ..models import InternshipPosition

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
                return jsonify({
                    "type": "unauthorized",
                    "message": "Only companies can post internships."
                }), 401
            
            if not validate_internship_position_data(internship_position_data):
                return jsonify({
                    "type": "invalid_request",
                    "message": "Invalid internship position data."
                }), 400
            
            internship_position = InternshipPosition.add(**internship_position_data)

            return jsonify({
                "message": "Internship position added successfully.",
                "internship position": internship_position.to_dict()
            }), 201
        
        except Exception as e:
            return e
        
        
    def get_internship_position_by_id(self, internshipPositionId):
        """
        Get an internship position by its ID.

        :param internshipPositionId: The ID of the internship position.
        :return: JSON response containing the internship details if the request is successful, 
             or an error message if the request fails
        """
        try:
            internship_position = InternshipPosition.get_by_id(internshipPositionId)
            if internship_position:
                return jsonify({
                    "internship_position": internship_position.to_dict()
                }), 200
            else:
                return jsonify({
                    "type": "not_found",
                    "message": "Internship not found."
                }), 404
        
        except Exception as e:
            return e


    def get_internship_positions_by_company(self, companyId):
        """
        Get all internship positions posted by a company.

        :param companyId: The ID of the company.
        :return: JSON response containing the internship positions posted by the company 
            if the request is successful, or an error message if the request fails
        """
        try:
            internship_positions = InternshipPosition.get_by_companyId(companyId)
            return jsonify({
                "internship_positions": [internship_position.to_dict() for internship_position in internship_positions]
            }), 200
        
        except Exception as e:
            return e
        

    def close_internship_position(self, internshipId):
        """
        Close an internship position.

        :param internshipId: The ID of the internship.
        :return: JSON response containing the status of the internship if the request is successful, 
                 or an error message if the request fails
        """
        try:
            if get_current_user().get_type() != "company":
                return jsonify({
                    "type": "unauthorized",
                    "message": "Only companies can close internships."
                }), 401
            
            internship = InternshipPosition.get_by_id(internshipId)
            if internship:
                if internship.get_companyId() == get_current_user().get_id():
                    internship.close()
                    return jsonify({
                        "message": "Internship position closed successfully."
                    }), 200
                else:
                    return jsonify({
                        "type": "unauthorized",
                        "message": "You are not authorized to close this internship."
                    }), 401
            else:
                return jsonify({
                    "type": "not_found",
                    "message": "Internship not found."
                }), 404
        
        except Exception as e:
            return e
        


def validate_internship_position_data(internship_data):
    """
    Validate the internship position data.

    :param internship_data: Dictionary containing internship position data
    :return: True if the internship position data is valid, otherwise False
    """
    try:
        if not (internship_data.get("companyId") == get_current_user().get_id()):
            print("Invalid company ID")
            return False
        if not is_name_valid(internship_data.get("programName")):
            print("Invalid program name")
            return False
        if not is_duration_valid(internship_data.get("duration")):
            print("Invalid duration")
            return False
        if not is_location_valid(internship_data.get("location")):
            print("Invalid location")
            return False
        if not is_name_valid(internship_data.get("roleTitle")):
            print("Invalid role title")
            return False
        if not is_skills_valid(internship_data.get("skillsRequired")):
            print("Invalid skills required")
            return False
        if not is_compensation_valid(internship_data.get("compensation")):
            print("Invalid compensation")
            return False
        if not is_benefits_valid(internship_data.get("benefits")):
            print("Invalid benefits")
            return False
        if not is_languageSpoken_valid(internship_data.get("languagesRequired")):
            print("Invalid languages required")
            return False
        if not is_description_valid(internship_data.get("description")):
            print("Invalid description")
            return False
        return True
    except Exception as e:
        print(f"Exception in validate_internship_position_data: {e}")
        return False
