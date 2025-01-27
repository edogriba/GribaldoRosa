from flask import jsonify

def json_response(message, status_code=200, **kwargs):
    response = {"message": message}
    response.update(kwargs)
    return jsonify(response), status_code


def json_invalid_request(message="Invalid request", **kwargs):
    """
    Return a JSON response for an invalid request. 

    :param message: The error message to return.
    :param kwargs: Additional key-value pairs to include in the response.
    :return: A JSON response containing the error message and any additional data.
    """
    return json_response(message, status_code=400, type="invalid_request", **kwargs)


def json_unauthorized(message="Unauthorized", **kwargs):
    """
    Return a JSON response for an unauthorized request.

    :param message: The error message to return.
    :param kwargs: Additional key-value pairs to include in the response.
    :return: A JSON response containing the error message and any additional data.
    """
    return json_response(message, status_code=401, type="unauthorized", **kwargs)


def json_not_found(message="Not found", **kwargs):
    """
    Return a JSON response for a resource not found.

    :param message: The error message to return.
    :param kwargs: Additional key-value pairs to include in the response.
    :return: A JSON response containing the error message and any additional data.
    """
    return json_response(message, status_code=404, type="not_found", **kwargs)


def json_internal_server_error(message="Internal server error", **kwargs):
    """
    Return a JSON response for an internal server error.

    :param message: The error message to return.
    :param kwargs: Additional key-value pairs to include in the response.
    :return: A JSON response containing the error message and any additional data.
    """
    return json_response(message, status_code=500, type="internal_server_error", **kwargs)


def json_success(message="Success", **kwargs):
    """
    Return a JSON response for a successful request.

    :param message: The success message to return.
    :param kwargs: Additional key-value pairs to include in the response.
    :return: A JSON response containing the success message and any additional data.
    """
    return json_response(message, status_code=200, type="success", **kwargs)


def json_created(message="Created", **kwargs):
    """
    Return a JSON response for a successful resource creation.

    :param message: The success message to return.
    :param kwargs: Additional key-value pairs to include in the response.
    :return: A JSON response containing the success message and any additional data.
    """
    return json_response(message, status_code=201, type="created", **kwargs)