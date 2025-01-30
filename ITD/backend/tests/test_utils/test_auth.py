import unittest
from unittest.mock import patch
import bcrypt
from app.utils.auth import hash_password, verify_password


class TestAuthUtils(unittest.TestCase):

    def test_hash_password_success(self):
        password = "securepassword"
        hashed = hash_password(password)
        self.assertTrue(bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8')))


    @patch('app.utils.auth.bcrypt.gensalt', side_effect=Exception("Hashing error"))
    def test_hash_password_failure(self, mock_gensalt):
        with self.assertRaises(Exception) as context:
            hash_password("securepassword")
        self.assertEqual(str(context.exception), "Hashing error")
        mock_gensalt.assert_called_once()


    def test_verify_password_success(self):
        password = "securepassword"
        hashed = hash_password(password)
        self.assertTrue(verify_password(password, hashed))


    def test_verify_password_failure(self):
        password = "securepassword"
        hashed = hash_password(password)
        self.assertFalse(verify_password("wrongpassword", hashed))


    @patch('app.utils.auth.bcrypt.checkpw', side_effect=Exception("Verification error"))
    def test_verify_password_exception(self, mock_checkpw):
        self.assertFalse(verify_password("securepassword", "hashedpassword"))


if __name__ == '__main__':
    unittest.main()
