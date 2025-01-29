from sqlite3 import IntegrityError, OperationalError, ProgrammingError, InterfaceError, DataError, Error
from werkzeug.exceptions import Unauthorized, MethodNotAllowed, Conflict, ServiceUnavailable
from .json_return import *
import logging

logging.basicConfig(level=logging.ERROR)


###################### 
##  General Errors  ##
###################### 

def bad_request_error_response():
    """ Handles general bad request errors, such as invalid input or missing data. """
    return json_invalid_request("The request could not be processed. Please ensure all required fields are correctly filled and try again.")


def type_error_response():
    """Handles TypeError exceptions and returns a custom response."""
    return json_invalid_request("Oops! It looks like there's a type mismatch. Please check your input and try again.")


def unauthorized_error_response():
    """ Handles unauthorized access errors. """
    return json_unauthorized("You are not authorized to access this resource. Please log in and try again.")


def forbidden_error_response():
    """ Handles forbidden errors, typically for restricted resources. """
    return json_forbidden("Access denied. You don't have the necessary permissions to view this resource. Please contact support if you believe this is an error.")


def not_found_error_response():
    """ Handles errors when a requested resource is not found. """
    return json_not_found("Sorry, we couldn't find what you're looking for. Please check your input or contact support if the problem persists.")


def method_not_allowed_error_response():
    """ Handles errors when an HTTP method is not allowed for a resource. """
    return json_method_not_allowed("The method you tried to use is not allowed for this resource. Please check the allowed methods and try again.")


def conflict_error_response():
    """ Handles conflict errors, like trying to create something that already exists. """
    return json_conflict("It seems there's a conflict with the current state of the resource. Please check your request and try again.")


def service_unavailable_error_response():
    """ Handles service unavailability errors, typically during maintenance. """
    return json_service_unavailable("Our service is currently undergoing maintenance. Please try again in a few minutes.")


def gateway_timeout_error_response():
    """ Handles errors where a server did not respond in time during a proxy or gateway request. """
    return json_gateway_timeout("Our servers are taking longer than expected to respond. Please try again in a few moments.")


def internal_server_error_response(error: str):
    """ Handles unexpected internal server errors. """
    return json_internal_server_error("Something went wrong on our end. We're working to fix it. Please try again later.")


####################### 
##  Database Errors  ##
####################### 

def integrity_error_response():
    """ Handles integrity constraint violations like duplicate or missing fields. """
    return json_invalid_request("It seems there's an issue with the data you provided. Please check for duplicates or missing fields and try again.")


def operation_error_response():
    """ Handles errors related to database operations, such as syntax or connection issues. """
    return json_internal_server_error("We encountered an issue while processing your request. Please try again or contact support if the problem persists.")


def programming_error_response():
    """ Handles programming errors, such as incorrect query syntax. """
    return json_internal_server_error("We encountered a problem with our database. Please try again later or contact support if the issue persists.")


def interface_error_response():
    """ Handles errors related to the database interface, such as a closed or invalid connection. """
    return json_internal_server_error("We encountered a problem with the database connection. Please try again later.")


def data_error_response():
    """ Handles errors when the data doesn't match the expected format or range. """
    return json_invalid_request("The data you provided doesn't seem to be in the correct format. Please review your input and try again.")


def generic_database_error_response(error: str):
    """ Handles unexpected database errors. """
    return json_internal_server_error("We encountered an unexpected issue with our database. Please try again later or contact support if the problem persists.")


################
##  Handlers  ##
################ 

def handle_database_error(error):
    """Handles database exceptions and maps them to custom exceptions."""
    if isinstance(error, IntegrityError):
        logging.exception(error)
        return integrity_error_response()
    elif isinstance(error, OperationalError):
        logging.exception(error)
        return operation_error_response()
    elif isinstance(error, ProgrammingError):
        logging.exception(error)
        return programming_error_response()
    elif isinstance(error, InterfaceError):
        logging.exception(error)
        return interface_error_response()
    elif isinstance(error, DataError):
        logging.exception(error)
        return data_error_response()
    else:
        logging.exception(error)
        return generic_database_error_response(str(error))


def handle_general_error(error):
    """Handles general exceptions and maps them to custom general exceptions."""
    if isinstance(error, ValueError):
        logging.exception(error)
        return bad_request_error_response()
    if isinstance(error, TypeError):
        logging.exception(error)
        return type_error_response()
    elif isinstance(error, Unauthorized):
        logging.exception(error)
        return unauthorized_error_response()
    elif isinstance(error, PermissionError):
        logging.exception(error)
        return forbidden_error_response()
    elif isinstance(error, KeyError):
        logging.exception(error)
        return not_found_error_response()
    elif isinstance(error, MethodNotAllowed):
        logging.exception(error)
        return method_not_allowed_error_response()
    elif isinstance(error, Conflict):
        logging.exception(error)
        return conflict_error_response()
    elif isinstance(error, ServiceUnavailable):
        logging.exception(error)
        return service_unavailable_error_response()
    elif isinstance(error, TimeoutError):
        logging.exception(error)
        return gateway_timeout_error_response()
    else:
        logging.exception(error)
        return internal_server_error_response(str(error))
    

def handle_error(error):
    """Handles both general and database errors."""
    if isinstance(error, Error):
        return handle_database_error(error)
    else:
        return handle_general_error(error)