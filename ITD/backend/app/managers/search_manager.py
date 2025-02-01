from ..models import InternshipPosition, Company
from ..utils import json_success, json_invalid_request
from ..services import is_int_valid


class SearchManager:
    
    @staticmethod
    def get_search_filters():
        try:
            roleTitles = InternshipPosition.get_role_titles()
            locations = InternshipPosition.get_locations()
            companiesNames = Company.get_companies_names()
        except Exception as e:
            raise e
        return json_success("Search filters found successfully.",
                            roleTitles = roleTitles,
                            locations = locations,
                            companiesNames = companiesNames)
    

    @staticmethod
    def search_internship_positions_with_filters(filters):
        try:
            values = {
                'roleTitle': filters.get('roleTitle', None),
                'location': filters.get('location', None),
                'companyName': filters.get('companyName', None),
                'minStipend': filters.get('minStipend', None),
                'minDuration': filters.get('minDuration', None),
                'maxDuration': filters.get('maxDuration', None),
            }
            if values['roleTitle'] and values['roleTitle'] not in InternshipPosition.get_role_titles():
                return json_invalid_request("Invalid role title.")
            if values['location'] and values['location'] not in InternshipPosition.get_locations():
                return json_invalid_request("Invalid location.")
            if values['companyName'] and values['companyName'] not in Company.get_companies_names():
                return json_invalid_request("Invalid company name.")
            if values['minStipend'] and not is_int_valid(values['minStipend']):
                return json_invalid_request("Invalid min stipend.")
            if values['minDuration'] and not is_int_valid(values['minDuration']):
                return json_invalid_request("Invalid min duration.")
            if values['maxDuration'] and not is_int_valid(values['maxDuration']):
                return json_invalid_request("Invalid max duration.")
            
            internships = InternshipPosition.search_internship_positions(filters)
        except Exception as e:
            raise e
        return json_success("Internships found successfully.", internships = [internship.to_dict() for internship in internships] if internships else [])
    

    @staticmethod
    def search_internship_positions_without_filters():
        try:
            internships = InternshipPosition.search_internship_positions({})
        except Exception as e:
            raise e
        return json_success("Internships found successfully.", internships = [internship.to_dict() for internship in internships] if internships else [])
        
