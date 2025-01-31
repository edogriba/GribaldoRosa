import os
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from typing import Union

# Load environment variables from .env file
load_dotenv()


def save_file(file, upload_folder) -> Union[None, Exception]:
    """
    Save an uploaded file to the specified folder.

    :param file: The file to save.
    :param upload_folder: The folder to save the file in.
    :raises Exception: If an error occurs during the save process.
    """
    try:
        # Ensure the upload folder exists
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        # Secure the filename and save the file
        filename = secure_filename(file.filename)
        file_path = os.path.join(upload_folder, filename).replace(os.sep, '/')
        file.save(file_path)

    except Exception as e:
        raise Exception(f"Error saving file: {e}")


def delete_file(file_path) -> Union[None, Exception]:
    """
    Delete a file from the file system.

    :param file_path: The path of the file to delete.
    :raises Exception: If an error occurs during the deletion process.
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise Exception(f"File not found: {file_path}")
    except Exception as e:
        raise e


def get_upload_folder_user(user_id: int) -> Union[str, Exception]:
    """
    Retrieve the upload folder path for a specific user from the environment variables.

    :param user_id: The ID of the user.
    :return: The upload folder path.
    """
    upload_folder = os.getenv('UPLOAD_FOLDER')
    if not upload_folder:
        raise Exception("UPLOAD_FOLDER environment variable not set")
    return os.path.join(upload_folder, str(user_id)).replace(os.sep, '/')


def get_upload_file_path_user(user_id: int, filename: str) -> Union[str, Exception]:
    """
    Retrieve the upload file path for a specific user from the environment variables.

    :param user_id: The ID of the user.
    :param filename: The name of the file.
    :return: The upload file path.
    """
    try:
        return os.path.join(get_upload_folder_user(user_id), filename).replace(os.sep, '/')
    except Exception as e:
        raise Exception(f"Error retrieving upload file path for user {user_id}: {e}")


def delete_file_user(user_id: int, filename: str) -> Union[None, Exception]:
    """
    Delete a file from the file system for a specific user.

    :param user_id: The ID of the user.
    :param filename: The name of the file.
    :raises Exception: If an error occurs during the deletion process.
    """
    try:
        file_path = get_upload_file_path_user(user_id, filename)
        delete_file(file_path)
    except Exception as e:
        raise Exception(f"Error deleting file: {e}")
    

def update_file_user(user_id: int, old_filename: str, new_file) -> Union[None, Exception]:
    """
    Update a file for a specific user.

    :param user_id: The ID of the user.
    :param old_filename: The name of the file to update.
    :param new_file: The new file to replace the old file with.
    :raises Exception: If an error occurs during the update process.
    """
    try:
        delete_file_user(user_id, old_filename)

        save_file(new_file, get_upload_folder_user(user_id))
    except Exception as e:
        raise Exception(f"Error updating file: {e}")