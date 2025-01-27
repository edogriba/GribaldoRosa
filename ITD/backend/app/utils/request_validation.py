from flask import request, jsonify
from .json_return import json_success, json_unsupported_media_type

def validate_request():
    """
    Validates the incoming HTTP request.

    This function checks the HTTP request method and content type to ensure they meet the expected criteria.
    - If the request method is `OPTIONS`, it returns a JSON response with status `OK` and HTTP status code 200.
    - If the request content type is not `application/json`, it returns a JSON response indicating an unsupported media type and HTTP status code 415.
    - If the request passes both checks, it returns None.

    Returns:
        Response: A Flask JSON response with appropriate status and message if validation fails.
        None: If the request is valid.
    """
    if request.method == 'OPTIONS':
        return json_success()

    if request.content_type != 'application/json':
        return json_unsupported_media_type()

    return None