from flask import jsonify
from flask_login import current_user

from app.models.internshipPosition import InternshipPosition
from app.services.auth_service import *

class InternshipManager:

    def post_internship(self, internship_data):
        """
        Post a new internship position.

        :param internship_data: Dictionary containing the internship position data.
        :return: JSON response containing the newly added internship position if post is successful, 
                 or an error message if registration fails
        """
        try:
            if current_user.get_type() != "company":
                return jsonify({
                    "type": "unauthorized",
                    "message": "Only companies can post internships."
                }), 401
            
            if not self.validate_internship_position_data(internship_data):
                return jsonify({
                    "type": "invalid_request",
                    "message": "Invalid internship position data."
                }), 400
            
            internship = InternshipPosition.add(**internship_data)

            return jsonify({
                "message": "Internship position added successfully.",
                "internship": internship.to_dict()
            }), 201
        
        except Exception as e:
            return e
        
        
    def get_internship_by_id(self, internshipId):
        """
        Get an internship by its ID.

        :param internshipId: The ID of the internship.
        :return: JSON response containing the internship details if the request is successful, 
                 or an error message if the request fails
        """
        try:
            internship = InternshipPosition.get_by_id(internshipId)
            if internship:
                return jsonify({
                    "internship": internship.to_dict()
                }), 200
            else:
                return jsonify({
                    "type": "not_found",
                    "message": "Internship not found."
                }), 404
        
        except Exception as e:
            return e


    def get_internships_by_company(self, companyId):
        """
        Get all internships posted by a company.

        :param companyId: The ID of the company.
        :return: JSON response containing the internships posted by the company 
                if the request is successful, or an error message if the request fails
        """
        try:
            internships = InternshipPosition.get_by_companyId(companyId)
            return jsonify({
                "internships": [internship.to_dict() for internship in internships]
            }), 200
        
        except Exception as e:
            return e
        
    def validate_internship_position_data(self, internship_data):
        """
        Validate the internship position data.

        :param internship_data: Dictionary containing internship position data
        :return: True if the internship position data is valid, otherwise False
        """
        try:
            if not (is_id_valid(internship_data.get("companyId")) and internship_data.get("companyId") == current_user.get_id()):
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
