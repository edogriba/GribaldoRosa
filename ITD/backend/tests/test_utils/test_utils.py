import unittest
from unittest.mock import patch, MagicMock
from app.utils.utils import save_file, delete_file, get_upload_folder_user, get_upload_file_path_user, delete_file_user, update_file_user

class TestUtils(unittest.TestCase):

    @patch('app.utils.utils.os.makedirs')
    @patch('app.utils.utils.os.path.exists')
    @patch('app.utils.utils.secure_filename')
    def test_save_file(self, mock_secure_filename, mock_path_exists, mock_makedirs):
        mock_file = MagicMock()
        mock_file.filename = 'test.txt'
        mock_secure_filename.return_value = 'test.txt'
        mock_path_exists.return_value = False

        save_file(mock_file, '/fake/path')

        mock_makedirs.assert_called_once_with('/fake/path')
        mock_file.save.assert_called_once_with('/fake/path/test.txt')


    @patch('app.utils.utils.os.makedirs')
    @patch('app.utils.utils.os.path.exists')
    @patch('app.utils.utils.secure_filename')
    def test_save_file_existing_folder(self, mock_secure_filename, mock_path_exists, mock_makedirs):
        mock_file = MagicMock()
        mock_file.filename = 'test.txt'
        mock_secure_filename.return_value = 'test.txt'
        mock_path_exists.return_value = True

        save_file(mock_file, '/fake/path')

        mock_makedirs.assert_not_called()
        mock_file.save.assert_called_once_with('/fake/path/test.txt')


    @patch('app.utils.utils.os.remove')
    @patch('app.utils.utils.os.path.exists')
    def test_delete_file(self, mock_path_exists, mock_remove):
        mock_path_exists.return_value = True

        delete_file('/fake/path/test.txt')

        mock_remove.assert_called_once_with('/fake/path/test.txt')


    @patch('app.utils.utils.os.remove')
    @patch('app.utils.utils.os.path.exists')
    def test_delete_file_not_found(self, mock_path_exists, mock_remove):
        mock_path_exists.return_value = False

        with self.assertRaises(Exception) as context:
            delete_file('/fake/path/test.txt')

        self.assertEqual(str(context.exception), "File not found: /fake/path/test.txt")
        mock_remove.assert_not_called()


    @patch('app.utils.utils.os.getenv')
    def test_get_upload_folder_user(self, mock_getenv):
        mock_getenv.return_value = '/fake/upload/folder'

        result = get_upload_folder_user(1)

        self.assertEqual(result, '/fake/upload/folder/1')


    @patch('app.utils.utils.os.getenv')
    def test_get_upload_folder_user_env_not_set(self, mock_getenv):
        mock_getenv.return_value = None

        with self.assertRaises(Exception) as context:
            get_upload_folder_user(1)

        self.assertEqual(str(context.exception), "UPLOAD_FOLDER environment variable not set")


    @patch('app.utils.utils.get_upload_folder_user')
    def test_get_upload_file_path_user(self, mock_get_upload_folder_user):
        mock_get_upload_folder_user.return_value = '/fake/upload/folder/1'

        result = get_upload_file_path_user(1, 'test.txt')

        self.assertEqual(result, '/fake/upload/folder/1/test.txt')


    @patch('app.utils.utils.delete_file')
    @patch('app.utils.utils.os.path.exists')
    @patch('app.utils.utils.get_upload_file_path_user')
    def test_delete_file_user(self, mock_get_upload_file_path_user, mock_path_exists, mock_delete_file):
        mock_get_upload_file_path_user.return_value = '/fake/upload/folder/1/test.txt'
        mock_path_exists.return_value = True

        delete_file_user(1, 'test.txt')

        mock_delete_file.assert_called_once_with('/fake/upload/folder/1/test.txt')
        mock_path_exists.assert_called_once_with('/fake/upload/folder/1/test.txt')


    @patch('app.utils.utils.get_upload_file_path_user')
    @patch('app.utils.utils.os.path.exists')
    def test_delete_file_user_file_not_found(self, mock_path_exists, mock_get_upload_file_path_user):
        mock_get_upload_file_path_user.return_value = '/fake/upload/folder/1/test.txt'
        mock_path_exists.return_value = False

        result = delete_file_user(1, 'test.txt')

        self.assertIsNone(result)
        mock_path_exists.assert_called_once_with('/fake/upload/folder/1/test.txt')


    @patch('app.utils.utils.save_file')
    @patch('app.utils.utils.delete_file_user')
    @patch('app.utils.utils.get_upload_folder_user')
    def test_update_file_user(self, mock_get_upload_folder_user, mock_delete_file_user, mock_save_file):
        mock_get_upload_folder_user.return_value = '/fake/upload/folder/1'
        mock_new_file = MagicMock()
        mock_new_file.filename = 'new_test.txt'

        update_file_user(1, 'old_test.txt', mock_new_file)

        mock_delete_file_user.assert_called_once_with(1, 'old_test.txt')
        mock_save_file.assert_called_once_with(mock_new_file, '/fake/upload/folder/1')


if __name__ == '__main__':
    unittest.main()