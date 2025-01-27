from flask import jsonify

def json_response(message, status_code=200, **kwargs):
    response = {"message": message}
    response.update(kwargs)
    return jsonify(response), status_code


def json_success(message="Success", **kwargs):
    """
    Return a JSON response for a successful request.

    :param message: The success message to return.
    :param kwargs: Additional key-value pairs to include in the response.
    :return: A JSON response containing the success message and any additional data.
    :status: 200 OK
    """
    return json_response(message, status_code=200, type="success", **kwargs)


def json_created(message="Created", **kwargs):
    """
    Return a JSON response for a successful resource creation.

    :param message: The success message to return.
    :param kwargs: Additional key-value pairs to include in the response.
    :return: A JSON response containing the success message and any additional data.
    :status: 201 Created
    """
    return json_response(message, status_code=201, type="created", **kwargs)


def json_invalid_request(message="Invalid request", **kwargs):
    """
    Return a JSON response for an invalid request. 

    :param message: The error message to return.
    :param kwargs: Additional key-value pairs to include in the response.
    :return: A JSON response containing the error message and any additional data.
    :status: 400 Bad Request
    """
    return json_response(message, status_code=400, type="invalid_request", **kwargs)


def json_unauthorized(message="Unauthorized", **kwargs):
    """
    Return a JSON response for an unauthorized request.

    :param message: The error message to return.
    :param kwargs: Additional key-value pairs to include in the response.
    :return: A JSON response containing the error message and any additional data.
    :status: 401 Unauthorized
    """
    return json_response(message, status_code=401, type="unauthorized", **kwargs)


def json_forbidden(message="Forbidden", **kwargs):
    """
    Return a JSON response for a forbidden request.

    :param message: The error message to return.
    :param kwargs: Additional key-value pairs to include in the response.
    :return: A JSON response containing the error message and any additional data.
    :status: 403 Forbidden
    """
    return json_response(message, status_code=403, type="forbidden", **kwargs)


def json_not_found(message="Not found", **kwargs):
    """
    Return a JSON response for a resource not found.

    :param message: The error message to return.
    :param kwargs: Additional key-value pairs to include in the response.
    :return: A JSON response containing the error message and any additional data.
    :status: 404 Not Found
    """
    return json_response(message, status_code=404, type="not_found", **kwargs)


def json_method_not_allowed(message="Method not allowed", **kwargs):
    """
    Return a JSON response for a method not allowed on a resource.

    :param message: The error message to return.
    :param kwargs: Additional key-value pairs to include in the response.
    :return: A JSON response containing the error message and any additional data.
    :status: 405 Method Not Allowed
    """
    return json_response(message, status_code=405, type="method_not_allowed", **kwargs)


def json_conflict(message="Conflict", **kwargs):
    """
    Return a JSON response for a conflict in the request.

    :param message: The error message to return.
    :param kwargs: Additional key-value pairs to include in the response.
    :return: A JSON response containing the error message and any additional data.
    :status: 409 Conflict
    """
    return json_response(message, status_code=409, type="conflict", **kwargs)


def json_unsupported_media_type(message="Content-Type must be application/json", **kwargs):
    """
    Return a JSON response for an unsupported media type.

    :param message: The error message to return.
    :param kwargs: Additional key-value pairs to include in the response.
    :return: A JSON response containing the error message and any additional data.
    :status: 415 Unsupported Media Type
    """
    return json_response(message, status_code=415, type="unsupported_media_type", **kwargs)


def json_internal_server_error(message="Internal server error", **kwargs):
    """
    Return a JSON response for an internal server error.

    :param message: The error message to return.
    :param kwargs: Additional key-value pairs to include in the response.
    :return: A JSON response containing the error message and any additional data.
    :status: 500 Internal Server Error
    """
    return json_response(message, status_code=500, type="internal_server_error", **kwargs)


def json_service_unavailable(message="Service unavailable", **kwargs):
    """
    Return a JSON response for a service that is temporarily unavailable.

    :param message: The error message to return.
    :param kwargs: Additional key-value pairs to include in the response.
    :return: A JSON response containing the error message and any additional data.
    :status: 503 Service Unavailable
    """
    return json_response(message, status_code=503, type="service_unavailable", **kwargs)


def json_gateway_timeout(message="Gateway timeout", **kwargs):
    """
    Return a JSON response for a gateway timeout error.

    :param message: The error message to return.
    :param kwargs: Additional key-value pairs to include in the response.
    :return: A JSON response containing the error message and any additional data.
    :status: 504 Gateway Timeout
    """
    return json_response(message, status_code=504, type="gateway_timeout", **kwargs)
