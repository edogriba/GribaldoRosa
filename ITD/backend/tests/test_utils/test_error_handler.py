import unittest
from flask import Flask
from sqlite3 import IntegrityError, OperationalError, ProgrammingError, InterfaceError, DataError, Error
from werkzeug.exceptions import Unauthorized, MethodNotAllowed, Conflict, ServiceUnavailable

from app.utils.error_handler import *

class TestErrorHandler(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.testing = True
        self.client = self.app.test_client()


    def test_bad_request_error_response(self):
        with self.app.app_context():
            (response, status_code) = bad_request_error_response()
            self.assertEqual(status_code, 400)


    def test_type_error_response(self):
        with self.app.app_context():
            (response, status_code) = type_error_response()
            self.assertEqual(status_code, 400)


    def test_unauthorized_error_response(self):
        with self.app.app_context():
            (response, status_code) = unauthorized_error_response()
            self.assertEqual(status_code, 401)


    def test_forbidden_error_response(self):
        with self.app.app_context():
            (response, status_code) = forbidden_error_response()
            self.assertEqual(status_code, 403)


    def test_not_found_error_response(self):
        with self.app.app_context():
            (response, status_code) = not_found_error_response()
            self.assertEqual(status_code, 404)


    def test_method_not_allowed_error_response(self):
        with self.app.app_context():
            (response, status_code) = method_not_allowed_error_response()
            self.assertEqual(status_code, 405)


    def test_conflict_error_response(self):
        with self.app.app_context():
            (response, status_code) = conflict_error_response()
            self.assertEqual(status_code, 409)


    def test_service_unavailable_error_response(self):
        with self.app.app_context():
            (response, status_code) = service_unavailable_error_response()
            self.assertEqual(status_code, 503)


    def test_gateway_timeout_error_response(self):
        with self.app.app_context():
            (response, status_code) = gateway_timeout_error_response()
            self.assertEqual(status_code, 504)


    def test_internal_server_error_response(self):
        with self.app.app_context():
            (response, status_code) = internal_server_error_response("Internal Server Error")
            self.assertEqual(status_code, 500)


    def test_integrity_error_response(self):
        with self.app.app_context():
            (response, status_code) = integrity_error_response()
            self.assertEqual(status_code, 400)


    def test_operation_error_response(self):
        with self.app.app_context():
            (response, status_code) = operation_error_response()
            self.assertEqual(status_code, 500)


    def test_programming_error_response(self):
        with self.app.app_context():
            (response, status_code) = programming_error_response()
            self.assertEqual(status_code, 500)


    def test_interface_error_response(self):
        with self.app.app_context():
            (response, status_code) = interface_error_response()
            self.assertEqual(status_code, 500)


    def test_data_error_response(self):
        with self.app.app_context():
            (response, status_code) = data_error_response()
            self.assertEqual(status_code, 400)


    def test_handle_database_error(self):
        with self.app.app_context():
            (response, status_code) = handle_database_error(IntegrityError("Integrity error occurred"))
            self.assertEqual(status_code, 400)
            self.assertIsNotNone(response)

            (response, status_code) = handle_database_error(OperationalError("Operational error occurred"))
            self.assertEqual(status_code, 500)
            self.assertIsNotNone(response)

            (response, status_code) = handle_database_error(ProgrammingError("Programming error occurred"))
            self.assertEqual(status_code, 500)
            self.assertIsNotNone(response)

            (response, status_code) = handle_database_error(InterfaceError("Interface error occurred"))
            self.assertEqual(status_code, 500)
            self.assertIsNotNone(response)

            (response, status_code) = handle_database_error(DataError("Data error occurred"))
            self.assertEqual(status_code, 400)
            self.assertIsNotNone(response)

            (response, status_code) = handle_database_error(Error("General database error occurred"))
            self.assertEqual(status_code, 500)
            self.assertIsNotNone(response)


    def test_handle_general_error(self):
        with self.app.app_context():
            (response, status_code) = handle_general_error(ValueError("Invalid value provided"))
            self.assertEqual(status_code, 400)
            self.assertIsNotNone(response)

            (response, status_code) = handle_general_error(TypeError("Type mismatch error"))
            self.assertEqual(status_code, 400)
            self.assertIsNotNone(response)

            (response, status_code) = handle_general_error(Unauthorized("Unauthorized access"))
            self.assertEqual(status_code, 401)
            self.assertIsNotNone(response)

            (response, status_code) = handle_general_error(PermissionError("Permission denied"))
            self.assertEqual(status_code, 403)
            self.assertIsNotNone(response)

            (response, status_code) = handle_general_error(KeyError("Key not found"))
            self.assertEqual(status_code, 404)
            self.assertIsNotNone(response)

            (response, status_code) = handle_general_error(MethodNotAllowed("Method not allowed"))
            self.assertEqual(status_code, 405)
            self.assertIsNotNone(response)

            (response, status_code) = handle_general_error(Conflict("Conflict occurred"))
            self.assertEqual(status_code, 409)
            self.assertIsNotNone(response)

            (response, status_code) = handle_general_error(ServiceUnavailable("Service is unavailable"))
            self.assertEqual(status_code, 503)
            self.assertIsNotNone(response)

            (response, status_code) = handle_general_error(TimeoutError("Request timed out"))
            self.assertEqual(status_code, 504)
            self.assertIsNotNone(response)

            (response, status_code) = handle_general_error(Exception("An unexpected error occurred"))
            self.assertEqual(status_code, 500)
            self.assertIsNotNone(response)


    def test_handle_error(self):
        with self.app.app_context():
            (response, status_code) = handle_error(IntegrityError("Integrity error occurred"))
            self.assertEqual(status_code, 400)
            self.assertIsNotNone(response)

            (response, status_code) = handle_error(ValueError("Invalid value provided"))
            self.assertEqual(status_code, 400)
            self.assertIsNotNone(response)

            (response, status_code) = handle_error(Exception("An unexpected error occurred"))
            self.assertEqual(status_code, 500)
            self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()