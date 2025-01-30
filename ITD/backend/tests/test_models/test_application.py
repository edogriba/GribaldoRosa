import unittest
from unittest.mock import patch
from app.models import Application, InternshipPosition, Student
from app.db.dbModels import ApplicationDB


class TestApplication(unittest.TestCase):

    def setUp(self):
        self.application1 = Application(
            applicationId=1,
            studentId=1,
            internshipPositionId=1,
            status='Pending'
        )

        self.application2 = Application(
            applicationId=2,
            studentId=2,
            internshipPositionId=2,
            status='Accepted'
        )

        self.application3 = Application(
            applicationId=3,
            studentId=3,
            internshipPositionId=3,
            status='Rejected'
        )

        self.application4 = Application(
            applicationId=4,
            studentId=4,
            internshipPositionId=4,
            status='Confirmed'
        )

        self.application5 = Application(
            applicationId=5,
            studentId=5,
            internshipPositionId=5,
            status='Refused'
        )


    def test_get_applicationId(self):
        self.assertEqual(self.application1.get_applicationId(), 1)
        self.assertEqual(self.application2.get_applicationId(), 2)
        self.assertEqual(self.application3.get_applicationId(), 3)
        self.assertEqual(self.application4.get_applicationId(), 4)
        self.assertEqual(self.application5.get_applicationId(), 5)


    def test_get_studentId(self):
        self.assertEqual(self.application1.get_studentId(), 1)
        self.assertEqual(self.application2.get_studentId(), 2)
        self.assertEqual(self.application3.get_studentId(), 3)
        self.assertEqual(self.application4.get_studentId(), 4)
        self.assertEqual(self.application5.get_studentId(), 5)
    

    def test_get_internshipPositionId(self):
        self.assertEqual(self.application1.get_internshipPositionId(), 1)
        self.assertEqual(self.application2.get_internshipPositionId(), 2)
        self.assertEqual(self.application3.get_internshipPositionId(), 3)
        self.assertEqual(self.application4.get_internshipPositionId(), 4)
        self.assertEqual(self.application5.get_internshipPositionId(), 5)


    def test_get_status(self):
        self.assertEqual(self.application1.get_status(), 'Pending')
        self.assertEqual(self.application2.get_status(), 'Accepted')
        self.assertEqual(self.application3.get_status(), 'Rejected')
        self.assertEqual(self.application4.get_status(), 'Confirmed')
        self.assertEqual(self.application5.get_status(), 'Refused')

    
    def test_to_dict(self):
        application_dict = self.application1.to_dict()
        expected_dict = {
            'applicationId': 1,
            'studentId': 1,
            'internshipPositionId': 1,
            'status': 'Pending'
        }
        self.assertEqual(application_dict, expected_dict)

        application_dict = self.application2.to_dict()
        expected_dict = {
            'applicationId': 2,
            'studentId': 2,
            'internshipPositionId': 2,
            'status': 'Accepted'
        }
        self.assertEqual(application_dict, expected_dict)

        application_dict = self.application3.to_dict()
        expected_dict = {
            'applicationId': 3,
            'studentId': 3,
            'internshipPositionId': 3,
            'status': 'Rejected'
        }
        self.assertEqual(application_dict, expected_dict)

        application_dict = self.application4.to_dict()
        expected_dict = {
            'applicationId': 4,
            'studentId': 4,
            'internshipPositionId': 4,
            'status': 'Confirmed'
        }
        self.assertEqual(application_dict, expected_dict)

        application_dict = self.application5.to_dict()
        expected_dict = {
            'applicationId': 5,
            'studentId': 5,
            'internshipPositionId': 5,
            'status': 'Refused'
        }
        self.assertEqual(application_dict, expected_dict)


    @patch.object(ApplicationDB, 'insert', return_value=6)
    @patch.object(ApplicationDB, 'close')
    def test_add_application(self, mock_close, mock_insert):
        application = Application.add(3, 4)

        self.assertEqual(application.applicationId, 6)
        self.assertEqual(application.studentId, 3)
        self.assertEqual(application.internshipPositionId, 4)
        self.assertEqual(application.status, 'Pending')

        mock_insert.assert_called_once_with(3, 4, 'Pending')
        mock_close.assert_called_once()

    
    @patch.object(ApplicationDB, 'insert', return_value=None)
    @patch.object(ApplicationDB, 'close')
    def test_add_application_return_none(self, mock_close, mock_insert):
        application = Application.add(3, 4)
        self.assertIsNone(application)
        mock_insert.assert_called_once_with(3, 4, 'Pending')
        mock_close.assert_called_once()


    @patch.object(ApplicationDB, 'insert', side_effect=Exception('Database error'))
    @patch.object(ApplicationDB, 'close')
    def test_add_application_raise_exception(self, mock_close, mock_insert):
        with self.assertRaises(Exception) as context:
            Application.add(3, 4)
        self.assertEqual(str(context.exception), 'Database error')
        mock_insert.assert_called_once_with(3, 4, 'Pending')
        mock_close.assert_called_once()

    
    @patch.object(ApplicationDB, 'get_by_id', return_value={
        'applicationId': 1,
        'studentId': 1,
        'internshipPositionId': 1,
        'status': 'Pending'
    })
    @patch.object(ApplicationDB, 'close')
    def test_get_by_id(self, mock_close, mock_get_by_id):
        application = Application.get_by_id(1)
        self.assertEqual(application.applicationId, 1)
        self.assertEqual(application.studentId, 1)
        self.assertEqual(application.internshipPositionId, 1)
        self.assertEqual(application.status, 'Pending')
        mock_get_by_id.assert_called_once_with(1)
        mock_close.assert_called_once()


    @patch.object(ApplicationDB, 'get_by_id', return_value=None)
    @patch.object(ApplicationDB, 'close')
    def test_get_by_id_not_found(self, mock_close, mock_get_by_id):
        application = Application.get_by_id(1)
        self.assertIsNone(application)
        mock_get_by_id.assert_called_once_with(1)
        mock_close.assert_called_once()
    

    @patch.object(ApplicationDB, 'get_by_id', side_effect=Exception('Database error'))
    @patch.object(ApplicationDB, 'close')
    def test_get_by_id_raise_exception(self, mock_close, mock_get_by_id):
        with self.assertRaises(Exception) as context:
            Application.get_by_id(1)
        self.assertEqual(str(context.exception), 'Database error')
        mock_get_by_id.assert_called_once_with(1)
        mock_close.assert_called_once()


    @patch.object(ApplicationDB, 'get_by_studentId', return_value=[
        {
            'applicationId': 1,
            'studentId': 1,
            'internshipPositionId': 1,
            'status': 'Pending'
        }
    ])
    @patch.object(ApplicationDB, 'close')
    def test_get_by_studentId(self, mock_close, mock_get_by_studentId):
        applications = Application.get_by_studentId(1)
        self.assertEqual(len(applications), 1)
        self.assertEqual(applications[0].applicationId, 1)
        mock_get_by_studentId.assert_called_once_with(1)
        mock_close.assert_called_once()
    

    @patch.object(ApplicationDB, 'get_by_studentId', return_value=[])
    @patch.object(ApplicationDB, 'close')
    def test_get_by_studentId_not_found(self, mock_close, mock_get_by_studentId):
        applications = Application.get_by_studentId(1)
        self.assertEqual(len(applications), 0)
        mock_get_by_studentId.assert_called_once_with(1)
        mock_close.assert_called_once()

    
    @patch.object(ApplicationDB, 'get_by_studentId', side_effect=Exception('Database error'))
    @patch.object(ApplicationDB, 'close')
    def test_get_by_studentId_raise_exception(self, mock_close, mock_get_by_studentId):
        with self.assertRaises(Exception) as context:
            Application.get_by_studentId(1)
        self.assertEqual(str(context.exception), 'Database error')
        mock_get_by_studentId.assert_called_once_with(1)
        mock_close.assert_called_once()


    @patch.object(ApplicationDB, 'get_by_internshipPositionId', return_value=[
        {
            'applicationId': 1,
            'studentId': 1,
            'internshipPositionId': 1,
            'status': 'Pending'
        }
    ])
    @patch.object(ApplicationDB, 'close')
    def test_get_by_internshipPositionId(self, mock_close, mock_get_by_internshipPositionId):
        applications = Application.get_by_internshipPositionId(1)
        self.assertEqual(len(applications), 1)
        self.assertEqual(applications[0].applicationId, 1)
        mock_get_by_internshipPositionId.assert_called_once_with(1)
        mock_close.assert_called_once()

    
    @patch.object(ApplicationDB, 'get_by_internshipPositionId', return_value=[])
    @patch.object(ApplicationDB, 'close')
    def test_get_by_internshipPositionId_not_found(self, mock_close, mock_get_by_internshipPositionId):
        applications = Application.get_by_internshipPositionId(1)
        self.assertEqual(len(applications), 0)
        mock_get_by_internshipPositionId.assert_called_once_with(1)
        mock_close.assert_called_once()

    
    @patch.object(ApplicationDB, 'get_by_internshipPositionId', side_effect=Exception('Database error'))
    @patch.object(ApplicationDB, 'close')
    def test_get_by_internshipPositionId_raise_exception(self, mock_close, mock_get_by_internshipPositionId):
        with self.assertRaises(Exception) as context:
            Application.get_by_internshipPositionId(1)
        self.assertEqual(str(context.exception), 'Database error')
        mock_get_by_internshipPositionId.assert_called_once_with(1)
        mock_close.assert_called_once()


    @patch.object(ApplicationDB, 'get_by_studentId_internshipPositionId', return_value={
        'applicationId': 1,
        'studentId': 1,
        'internshipPositionId': 1,
        'status': 'Pending'
    })
    @patch.object(ApplicationDB, 'close')
    def test_get_by_studentId_internshipPositionId(self, mock_close, mock_get_by_studentId_internshipPositionId):
        application = Application.get_by_studentId_internshipPositionId(1, 1)
        self.assertEqual(application.applicationId, 1)
        self.assertEqual(application.studentId, 1)
        self.assertEqual(application.internshipPositionId, 1)
        self.assertEqual(application.status, 'Pending')
        mock_get_by_studentId_internshipPositionId.assert_called_once_with(1, 1)
        mock_close.assert_called_once()


    @patch.object(ApplicationDB, 'get_by_studentId_internshipPositionId', return_value=None)
    @patch.object(ApplicationDB, 'close')
    def test_get_by_studentId_internshipPositionId_not_found(self, mock_close, mock_get_by_studentId_internshipPositionId):
        application = Application.get_by_studentId_internshipPositionId(1, 1)
        self.assertIsNone(application)
        mock_get_by_studentId_internshipPositionId.assert_called_once_with(1, 1)
        mock_close.assert_called_once()


    @patch.object(ApplicationDB, 'get_by_studentId_internshipPositionId', side_effect=Exception('Database error'))
    @patch.object(ApplicationDB, 'close')
    def test_get_by_studentId_internshipPositionId_raise_exception(self, mock_close, mock_get_by_studentId_internshipPositionId):
        with self.assertRaises(Exception) as context:
            Application.get_by_studentId_internshipPositionId(1, 1)
        self.assertEqual(str(context.exception), 'Database error')
        mock_get_by_studentId_internshipPositionId.assert_called_once_with(1, 1)
        mock_close.assert_called_once()


    @patch.object(InternshipPosition, 'get_by_id', return_value='InternshipPositionInstance')
    def test_get_internshipPosition(self, mock_get_by_id):
        internship_position = self.application1.get_internshipPosition()
        self.assertEqual(internship_position, 'InternshipPositionInstance')
        mock_get_by_id.assert_called_once_with(1)


    @patch.object(InternshipPosition, 'get_by_id', return_value=None)
    def test_get_internshipPosition_not_found(self, mock_get_by_id):
        internship_position = self.application1.get_internshipPosition()
        self.assertIsNone(internship_position)
        mock_get_by_id.assert_called_once_with(1)


    @patch.object(InternshipPosition, 'get_by_id', side_effect=Exception('Database error'))
    def test_get_internshipPosition_raise_exception(self, mock_get_by_id):
        with self.assertRaises(Exception) as context:
            self.application1.get_internshipPosition()
        self.assertEqual(str(context.exception), 'Database error')
        mock_get_by_id.assert_called_once_with(1)


    @patch.object(Student, 'get_by_id', return_value='StudentInstance')
    def test_get_student(self, mock_get_by_id):
        student = self.application1.get_student()
        self.assertEqual(student, 'StudentInstance')
        mock_get_by_id.assert_called_once_with(1)

    
    @patch.object(Student, 'get_by_id', return_value=None)
    def test_get_student_not_found(self, mock_get_by_id):
        student = self.application1.get_student()
        self.assertIsNone(student)
        mock_get_by_id.assert_called_once_with(1)

    
    @patch.object(Student, 'get_by_id', side_effect=Exception('Database error'))
    def test_get_student_raise_exception(self, mock_get_by_id):
        with self.assertRaises(Exception) as context:
            self.application1.get_student()
        self.assertEqual(str(context.exception), 'Database error')
        mock_get_by_id.assert_called_once_with(1)


    @patch.object(ApplicationDB, 'update_status')
    @patch.object(ApplicationDB, 'close')
    def test_update_status(self, mock_close, mock_update_status):
        self.application1.update_status('Accepted')
        mock_update_status.assert_called_once_with(1, 'Accepted')
        mock_close.assert_called_once()

    
    @patch.object(ApplicationDB, 'update_status', side_effect=Exception('Database error'))
    @patch.object(ApplicationDB, 'close')
    def test_update_status_raise_exception(self, mock_close, mock_update_status):
        with self.assertRaises(Exception) as context:
            self.application1.update_status('Accepted')
        self.assertEqual(str(context.exception), 'Database error')
        mock_update_status.assert_called_once_with(1, 'Accepted')
        mock_close.assert_called_once()


    @patch.object(Application, 'update_status')
    def test_pending(self, mock_update_status):
        self.application1.pending()
        mock_update_status.assert_called_once_with("Pending")
    

    @patch.object(Application, 'update_status', side_effect=Exception('Database error'))
    def test_pending_raise_exception(self, mock_update_status):
        with self.assertRaises(Exception) as context:
            self.application1.pending()
        self.assertEqual(str(context.exception), 'Database error')
        mock_update_status.assert_called_once_with("Pending")


    @patch.object(Application, 'update_status')
    def test_accept(self, mock_update_status):
        self.application1.accept()
        mock_update_status.assert_called_once_with("Accepted")


    @patch.object(Application, 'update_status', side_effect=Exception('Database error'))
    def test_accept_raise_exception(self, mock_update_status):
        with self.assertRaises(Exception) as context:
            self.application1.accept()
        self.assertEqual(str(context.exception), 'Database error')
        mock_update_status.assert_called_once_with("Accepted")


    @patch.object(Application, 'update_status')
    def test_reject(self, mock_update_status):
        self.application1.reject()
        mock_update_status.assert_called_once_with("Rejected")


    @patch.object(Application, 'update_status', side_effect=Exception('Database error'))
    def test_reject_raise_exception(self, mock_update_status):
        with self.assertRaises(Exception) as context:
            self.application1.reject()
        self.assertEqual(str(context.exception), 'Database error')
        mock_update_status.assert_called_once_with("Rejected")


    @patch.object(Application, 'update_status')
    def test_confirm(self, mock_update_status):
        self.application1.confirm()
        mock_update_status.assert_called_once_with("Confirmed")


    @patch.object(Application, 'update_status', side_effect=Exception('Database error'))
    def test_confirm_raise_exception(self, mock_update_status):
        with self.assertRaises(Exception) as context:
            self.application1.confirm()
        self.assertEqual(str(context.exception), 'Database error')
        mock_update_status.assert_called_once_with("Confirmed")


    @patch.object(Application, 'update_status')
    def test_refuse(self, mock_update_status):
        self.application1.refuse()
        mock_update_status.assert_called_once_with("Refused")


    @patch.object(Application, 'update_status', side_effect=Exception('Database error'))
    def test_refuse_raise_exception(self, mock_update_status):
        with self.assertRaises(Exception) as context:
            self.application1.refuse()
        self.assertEqual(str(context.exception), 'Database error')
        mock_update_status.assert_called_once_with("Refused")


    def test_is_pending(self):
        application = Application(1, 1, 1, 'Pending')
        application2 = Application(1, 1, 1, 'Accepted')
        self.assertTrue(application.is_pending())
        self.assertFalse(application2.is_pending())


    def test_is_accepted(self):
        application = Application(1, 1, 1, 'Accepted')
        application2 = Application(1, 1, 1, 'Pending')
        self.assertTrue(application.is_accepted())
        self.assertFalse(application2.is_accepted())


    def test_is_rejected(self):
        application = Application(1, 1, 1, 'Rejected')
        application2 = Application(1, 1, 1, 'Pending')
        self.assertTrue(application.is_rejected())
        self.assertFalse(application2.is_rejected())


    def test_is_confirmed(self):
        application = Application(1, 1, 1, 'Confirmed')
        application2 = Application(1, 1, 1, 'Pending')
        self.assertTrue(application.is_confirmed())
        self.assertFalse(application2.is_confirmed())


    def test_is_refused(self):
        application = Application(1, 1, 1, 'Refused')
        application2 = Application(1, 1, 1, 'Pending')
        self.assertTrue(application.is_refused())
        self.assertFalse(application2.is_refused())


if __name__ == '__main__':
    unittest.main()