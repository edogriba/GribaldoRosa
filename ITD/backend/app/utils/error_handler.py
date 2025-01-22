from flask import jsonify
from sqlite3 import IntegrityError, OperationalError, ProgrammingError, InterfaceError, DataError
from werkzeug.exceptions import Unauthorized, MethodNotAllowed, Conflict, ServiceUnavailable

def invalid_request_error(missing_fields):
    """  
    Handles errors related to missing required fields in a request.  
    Returns an error message specifying the missing fields.  
    """ 
    if isinstance(missing_fields, str):
        missing_fields = [missing_fields]
    return jsonify({
        "type": "invalid_request",
        "message": f"The following fields are required: {', '.join(missing_fields)}."
    }), 400

###################### 
##  General Errors  ##
###################### 

def bad_request_error_response():
    """ Handles general bad request errors, such as invalid input or missing data. """
    return jsonify({
        "type": "bad_request",
        "message": "Bad request. Please check the input data."
    }), 400


def type_error_response():
    """Handles TypeError exceptions and returns a custom response."""
    return jsonify({
        "type": "type_error",
        "message": "A TypeError occurred. Please check your input types."
    }), 400


def unauthorized_error_response():
    """ Handles unauthorized access errors. """
    return jsonify({
        "type": "unauthorized",
        "message": "Unauthorized access. Please log in."
    }), 401


def forbidden_error_response():
    """ Handles forbidden errors, typically for restricted resources. """
    return jsonify({
        "type": "forbidden",
        "message": "Forbidden. You do not have permission to access this resource."
    }), 403


def not_found_error_response():
    """ Handles errors when a requested resource is not found. """
    return jsonify({
        "type": "not_found",
        "message": "Resource not found."
    }), 404


def method_not_allowed_error_response():
    """ Handles errors when an HTTP method is not allowed for a resource. """
    return jsonify({
        "type": "method_not_allowed",
        "message": "Method not allowed."
    }), 405


def conflict_error_response():
    """ Handles conflict errors, like trying to create something that already exists. """
    return jsonify({
        "type": "conflict",
        "message": "Conflict. The request could not be completed due to a conflict with the current state of the target resource."
    }), 409


def service_unavailable_error_response():
    """ Handles service unavailability errors, typically during maintenance. """
    return jsonify({
        "type": "service_unavailable",
        "message": "Service unavailable. Please try again later."
    }), 503


def gateway_timeout_error_response():
    """ Handles errors where a server did not respond in time during a proxy or gateway request. """
    return jsonify({
        "type": "gateway_timeout",
        "message": "Gateway timeout. The server did not respond in time."
    }), 504


def internal_server_error_response(error: str):
    """ Handles unexpected internal server errors. """
    return jsonify({
        "type": "internal_server_error",
        "message": error        # "An unexpected error occurred on the server. Please try again later."
    }), 500


####################### 
##  Database Errors  ##
####################### 

def integrity_error_response():
    """ Handles integrity constraint violations like duplicate or missing fields. """
    return jsonify({
        "type": "database_integrity_error",
        "message": "A database integrity constraint was violated. Possible duplicate or missing required fields."
    }), 400


def operation_error_response():
    """ Handles errors related to database operations, such as syntax or connection issues. """
    return jsonify({
        "type": "database_operation_error",
        "message": "There was an issue with the database operation. Please check your request."
    }), 500


def programming_error_response():
    """ Handles programming errors, such as incorrect query syntax. """
    return jsonify({
        "type": "database_programming_error",
        "message": "A database programming error occurred. Please contact support."
    }), 500


def interface_error_response():
    """ Handles errors related to the database interface, such as a closed or invalid connection. """
    return jsonify({
            "type": "database_interface_error",
            "message": "There was an issue with the database connection interface. The connection might be closed."
        }), 500


def data_error_response():
    """ Handles errors when the data doesn't match the expected format or range. """
    return jsonify({
        "type": "database_data_error",
        "message": "The data provided is invalid. Please check the input data."
    }), 400


def generic_database_error_response(error: str):
    """ Handles unexpected database errors. """
    return jsonify({
        "type": "database_error",
        "message": error        # "An unexpected database error occurred."
    }), 500


################
##  Handlers  ##
################ 

def handle_database_error(error):
    """Handles database exceptions and maps them to custom exceptions."""
    if isinstance(error, IntegrityError):
        return integrity_error_response()
    elif isinstance(error, OperationalError):
        return operation_error_response()
    elif isinstance(error, ProgrammingError):
        return programming_error_response()
    elif isinstance(error, InterfaceError):
        return interface_error_response()
    elif isinstance(error, DataError):
        return data_error_response()
    else:
        return generic_database_error_response(str(error))


def handle_general_error(error):
    """Handles general exceptions and maps them to custom general exceptions."""
    if isinstance(error, ValueError):
        return bad_request_error_response()
    if isinstance(error, TypeError):
        return type_error_response()
    elif isinstance(error, Unauthorized):
        return unauthorized_error_response()
    elif isinstance(error, PermissionError):
        return forbidden_error_response()
    elif isinstance(error, KeyError):
        return not_found_error_response()
    elif isinstance(error, MethodNotAllowed):
        return method_not_allowed_error_response()
    elif isinstance(error, Conflict):
        return conflict_error_response()
    elif isinstance(error, ServiceUnavailable):
        return service_unavailable_error_response()
    elif isinstance(error, TimeoutError):
        return gateway_timeout_error_response()
    else:
        return internal_server_error_response(str(error))
    
