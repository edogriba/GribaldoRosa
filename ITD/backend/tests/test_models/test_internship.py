import unittest
from unittest.mock import patch
from app.models import Internship
from app.db.dbModels import InternshipDB


class TestInternship(unittest.TestCase):

    def setUp(self):
        self.internship1 = Internship(
            internshipId=1,
            internshipPositionId=1,
            applicationId=1,
            status='Ongoing'
        )

        self.internship2 = Internship(
            internshipId=2,
            internshipPositionId=2,
            applicationId=2,
            status='Finished'
        )


    def test_get_internshipId(self):
        self.assertEqual(self.internship1.get_internshipId(), 1)
        self.assertEqual(self.internship2.get_internshipId(), 2)


    def test_get_internshipPositionId(self):
        self.assertEqual(self.internship1.get_internshipPositionId(), 1)
        self.assertEqual(self.internship2.get_internshipPositionId(), 2)


    def test_get_applicationId(self):
        self.assertEqual(self.internship1.get_applicationId(), 1)
        self.assertEqual(self.internship2.get_applicationId(), 2)


    def test_get_status(self):
        self.assertEqual(self.internship1.get_status(), 'Ongoing')
        self.assertEqual(self.internship2.get_status(), 'Finished')


    def test_to_dict(self):
        self.assertEqual(self.internship1.to_dict(), {
            'internshipId': 1,
            'internshipPositionId': 1,
            'applicationId': 1,
            'status': 'Ongoing',
        })
        self.assertEqual(self.internship2.to_dict(), {
            'internshipId': 2,
            'internshipPositionId': 2,
            'applicationId': 2,
            'status': 'Finished',
        })


    @patch.object(InternshipDB, 'insert', return_value=3)
    @patch.object(InternshipDB, 'close')
    def test_add(self, mock_close, mock_insert):
        new_internship = Internship.add(3, 3)
        self.assertEqual(new_internship.internshipId, 3)
        self.assertEqual(new_internship.internshipPositionId, 3)
        self.assertEqual(new_internship.applicationId, 3)
        self.assertEqual(new_internship.status, 'Ongoing')
        mock_insert.assert_called_once_with(internshipPositionId=3, applicationId=3, status='Ongoing')
        mock_close.assert_called_once()

    
    @patch.object(InternshipDB, 'insert', return_value=None)
    @patch.object(InternshipDB, 'close')
    def test_add_returns_none(self, mock_close, mock_insert):
        new_internship = Internship.add(3, 3)
        self.assertIsNone(new_internship)
        mock_insert.assert_called_once_with(internshipPositionId=3, applicationId=3, status='Ongoing')
        mock_close.assert_called_once()


    @patch.object(InternshipDB, 'insert', side_effect=Exception('Database error'))
    @patch.object(InternshipDB, 'close')
    def test_add_raises_exception(self, mock_close, mock_insert):
        with self.assertRaises(Exception) as context:
            Internship.add(3, 3)
        self.assertEqual(str(context.exception), 'Database error')
        mock_insert.assert_called_once_with(internshipPositionId=3, applicationId=3, status='Ongoing')
        mock_close.assert_called_once()


    @patch.object(InternshipDB, 'get_by_id', return_value={
        'internshipId': 1,
        'internshipPositionId': 1,
        'applicationId': 1,
        'status': 'Ongoing',
    })
    @patch.object(InternshipDB, 'close')
    def test_get_by_id(self, mock_close, mock_get_by_id):
        internship = Internship.get_by_id(1)
        self.assertEqual(internship.internshipId, 1)
        self.assertEqual(internship.internshipPositionId, 1)
        self.assertEqual(internship.applicationId, 1)
        self.assertEqual(internship.status, 'Ongoing')
        mock_get_by_id.assert_called_once_with(1)
        mock_close.assert_called_once()

    
    @patch.object(InternshipDB, 'get_by_id', return_value=None)
    @patch.object(InternshipDB, 'close')
    def test_get_by_id_returns_none(self, mock_close, mock_get_by_id):
        internship = Internship.get_by_id(1)
        self.assertIsNone(internship)
        mock_get_by_id.assert_called_once_with(1)
        mock_close.assert_called_once()

    
    @patch.object(InternshipDB, 'get_by_id', side_effect=Exception('Database error'))
    @patch.object(InternshipDB, 'close')
    def test_get_by_id_raises_exception(self, mock_close, mock_get_by_id):
        with self.assertRaises(Exception) as context:
            Internship.get_by_id(1)
        self.assertEqual(str(context.exception), 'Database error')
        mock_get_by_id.assert_called_once_with(1)
        mock_close.assert_called_once()


    @patch.object(InternshipDB, 'get_by_application_id', return_value=
        {'internshipId': 1, 'internshipPositionId': 1, 'applicationId': 1, 'status': 'Ongoing'})
    @patch.object(InternshipDB, 'close')
    def test_get_by_applicationId(self, mock_close, mock_get_by_application_id):
        internship = Internship.get_by_applicationId(1)
        self.assertEqual(internship.internshipId, 1)
        self.assertEqual(internship.internshipPositionId, 1)
        self.assertEqual(internship.applicationId, 1)
        self.assertEqual(internship.status, 'Ongoing')
        mock_get_by_application_id.assert_called_once_with(1)
        mock_close.assert_called_once()


    @patch.object(InternshipDB, 'get_by_application_id', return_value=None)
    @patch.object(InternshipDB, 'close')
    def test_get_by_applicationId_returns_empty_list(self, mock_close, mock_get_by_application_id):
        internship = Internship.get_by_applicationId(1)
        self.assertIsNone(internship)
        mock_get_by_application_id.assert_called_once_with(1)
        mock_close.assert_called_once()


    @patch.object(InternshipDB, 'get_by_application_id', side_effect=Exception('Database error'))
    @patch.object(InternshipDB, 'close')
    def test_get_by_applicationId_raises_exception(self, mock_close, mock_get_by_application_id):
        with self.assertRaises(Exception) as context:
            Internship.get_by_applicationId(1)
        self.assertEqual(str(context.exception), 'Database error')
        mock_get_by_application_id.assert_called_once_with(1)
        mock_close.assert_called_once()


    @patch.object(InternshipDB, 'get_by_internshipPosition_id', return_value=[
        {'internshipId': 1, 'internshipPositionId': 1, 'applicationId': 1, 'status': 'Ongoing'},
        {'internshipId': 2, 'internshipPositionId': 1, 'applicationId': 2, 'status': 'Finished'}
    ])
    @patch.object(InternshipDB, 'close')
    def test_get_by_internshipPositionId(self, mock_close, mock_get_by_internshipPosition_id):
        internships = Internship.get_by_internshipPositionId(1)
        self.assertEqual(len(internships), 2)
        self.assertEqual(internships[0].internshipId, 1)
        self.assertEqual(internships[0].internshipPositionId, 1)
        self.assertEqual(internships[0].applicationId, 1)
        self.assertEqual(internships[0].status, 'Ongoing')
        self.assertEqual(internships[1].internshipId, 2)
        self.assertEqual(internships[1].internshipPositionId, 1)
        self.assertEqual(internships[1].applicationId, 2)
        self.assertEqual(internships[1].status, 'Finished')
        mock_get_by_internshipPosition_id.assert_called_once_with(1)
        mock_close.assert_called_once()

    
    @patch.object(InternshipDB, 'get_by_internshipPosition_id', return_value=[])
    @patch.object(InternshipDB, 'close')
    def test_get_by_internshipPositionId_returns_empty_list(self, mock_close, mock_get_by_internshipPosition_id):
        internships = Internship.get_by_internshipPositionId(1)
        self.assertEqual(internships, [])
        mock_get_by_internshipPosition_id.assert_called_once_with(1)
        mock_close.assert_called_once()

    
    @patch.object(InternshipDB, 'get_by_internshipPosition_id', side_effect=Exception('Database error'))
    @patch.object(InternshipDB, 'close')
    def test_get_by_internshipPositionId_raises_exception(self, mock_close, mock_get_by_internshipPosition_id):
        with self.assertRaises(Exception) as context:
            Internship.get_by_internshipPositionId(1)
        self.assertEqual(str(context.exception), 'Database error')
        mock_get_by_internshipPosition_id.assert_called_once_with(1)
        mock_close.assert_called_once()


    @patch.object(InternshipDB, 'get_by_applicationId_internshipPositionId', return_value=
        {'internshipId': 1, 'internshipPositionId': 1, 'applicationId': 1, 'status': 'Ongoing'})
    @patch.object(InternshipDB, 'close')
    def test_get_by_applicationId_internshipPositionId(self, mock_close, mock_get_by_applicationId_internshipPositionId):
        internship = Internship.get_by_applicationId_internshipPositionId(1, 1)
        self.assertEqual(internship.internshipId, 1)
        self.assertEqual(internship.internshipPositionId, 1)
        self.assertEqual(internship.applicationId, 1)
        self.assertEqual(internship.status, 'Ongoing')
        mock_get_by_applicationId_internshipPositionId.assert_called_once_with(1, 1)
        mock_close.assert_called_once()

    
    @patch.object(InternshipDB, 'get_by_applicationId_internshipPositionId', return_value=None)
    @patch.object(InternshipDB, 'close')
    def test_get_by_applicationId_internshipPositionId_returns_none(self, mock_close, mock_get_by_applicationId_internshipPositionId):
        internship = Internship.get_by_applicationId_internshipPositionId(1, 1)
        self.assertIsNone(internship)
        mock_get_by_applicationId_internshipPositionId.assert_called_once_with(1, 1)
        mock_close.assert_called_once()

    
    @patch.object(InternshipDB, 'get_by_applicationId_internshipPositionId', side_effect=Exception('Database error'))
    @patch.object(InternshipDB, 'close')
    def test_get_by_applicationId_internshipPositionId_raises_exception(self, mock_close, mock_get_by_applicationId_internshipPositionId):
        with self.assertRaises(Exception) as context:
            Internship.get_by_applicationId_internshipPositionId(1, 1)
        self.assertEqual(str(context.exception), 'Database error')
        mock_get_by_applicationId_internshipPositionId.assert_called_once_with(1, 1)
        mock_close.assert_called_once()


    @patch.object(InternshipDB, 'update_status')
    @patch.object(InternshipDB, 'close')
    def test_update_status(self, mock_close, mock_update_status):
        self.internship1.update_status('Finished')
        self.assertEqual(self.internship1.status, 'Finished')
        mock_update_status.assert_called_once_with(self.internship1.internshipId, 'Finished')
        mock_close.assert_called_once()


    @patch.object(InternshipDB, 'update_status', side_effect=Exception('Database error'))
    @patch.object(InternshipDB, 'close')
    def test_update_status_raises_exception(self, mock_close, mock_update_status):
        with self.assertRaises(Exception) as context:
            self.internship1.update_status('Finished')
        self.assertEqual(str(context.exception), 'Database error')
        mock_update_status.assert_called_once_with(self.internship1.internshipId, 'Finished')
        mock_close.assert_called_once()
    

    @patch.object(Internship, 'update_status')
    def test_make_ongoing(self, mock_update_status):
        self.internship1.make_ongoing()
        mock_update_status.assert_called_once_with('Ongoing')

    
    @patch.object(Internship, 'update_status', side_effect=Exception('Database error'))
    def test_make_ongoing_raises_exception(self, mock_update_status):
        with self.assertRaises(Exception) as context:
            self.internship1.make_ongoing()
        self.assertEqual(str(context.exception), 'Database error')
        mock_update_status.assert_called_once_with('Ongoing')

    
    @patch.object(Internship, 'update_status')
    def test_make_finished(self, mock_update_status):
        self.internship1.finish()
        mock_update_status.assert_called_once_with('Finished')


    @patch.object(Internship, 'update_status', side_effect=Exception('Database error'))
    def test_make_finished_raises_exception(self, mock_update_status):
        with self.assertRaises(Exception) as context:
            self.internship1.finish()
        self.assertEqual(str(context.exception), 'Database error')
        mock_update_status.assert_called_once_with('Finished')
    

    def test_is_ongoing(self):
        self.assertTrue(self.internship1.is_ongoing())
        self.assertFalse(self.internship2.is_ongoing())


    def test_is_finished(self):
        self.assertFalse(self.internship1.is_finished())
        self.assertTrue(self.internship2.is_finished())


    @patch.object(InternshipDB, 'get_preview_by_company_id', return_value=[
        {
            'student_name': 'John Doe',
            'student_photoPath': 'path/to/photo.jpg',
            'internshipId': 1,
            'roleTitle': 'Software Engineer',
            'status': 'Ongoing'
        },
        {
            'student_name': 'Jane Smith',
            'student_photoPath': None,
            'internshipId': 2,
            'roleTitle': 'Data Scientist',
            'status': 'Finished'
        }
    ])
    @patch.object(InternshipDB, 'close')
    def test_get_preview_by_companyId(self, mock_close, mock_get_preview_by_company_id):
        previews = Internship.get_preview_by_companyId(1)
        self.assertEqual(len(previews), 2)
        self.assertEqual(previews[0]['student_name'], 'John Doe')
        self.assertEqual(previews[0]['student_photoPath'], 'path/to/photo.jpg')
        self.assertEqual(previews[0]['internshipId'], 1)
        self.assertEqual(previews[0]['roleTitle'], 'Software Engineer')
        self.assertEqual(previews[0]['status'], 'Ongoing')
        self.assertEqual(previews[1]['student_name'], 'Jane Smith')
        self.assertIsNone(previews[1]['student_photoPath'])
        self.assertEqual(previews[1]['internshipId'], 2)
        self.assertEqual(previews[1]['roleTitle'], 'Data Scientist')
        self.assertEqual(previews[1]['status'], 'Finished')
        mock_get_preview_by_company_id.assert_called_once_with(1)
        mock_close.assert_called_once()

    
    @patch.object(InternshipDB, 'get_preview_by_company_id', return_value=[])
    @patch.object(InternshipDB, 'close')
    def test_get_preview_by_companyId_returns_empty_list(self, mock_close, mock_get_preview_by_company_id):
        previews = Internship.get_preview_by_companyId(1)
        self.assertEqual(previews, [])
        mock_get_preview_by_company_id.assert_called_once_with(1)
        mock_close.assert_called_once()

    
    @patch.object(InternshipDB, 'get_preview_by_company_id', side_effect=Exception('Database error'))
    @patch.object(InternshipDB, 'close')
    def test_get_preview_by_companyId_raises_exception(self, mock_close, mock_get_preview_by_company_id):
        with self.assertRaises(Exception) as context:
            Internship.get_preview_by_companyId(1)
        self.assertEqual(str(context.exception), 'Database error')
        mock_get_preview_by_company_id.assert_called_once_with(1)
        mock_close.assert_called_once()


    @patch.object(InternshipDB, 'get_preview_by_student_id', return_value=[
        {
            'company_name': 'Tech Corp',
            'company_photoPath': 'path/to/company_photo.jpg',
            'internshipId': 1,
            'roleTitle': 'Software Engineer',
            'status': 'Ongoing'
        },
        {
            'company_name': 'Data Inc',
            'company_photoPath': None,
            'internshipId': 2,
            'roleTitle': 'Data Scientist',
            'status': 'Finished'
        }
    ])
    @patch.object(InternshipDB, 'close')
    def test_get_preview_by_studentId(self, mock_close, mock_get_preview_by_student_id):
        previews = Internship.get_preview_by_studentId(1)
        self.assertEqual(len(previews), 2)
        self.assertEqual(previews[0]['company_name'], 'Tech Corp')
        self.assertEqual(previews[0]['company_photoPath'], 'path/to/company_photo.jpg')
        self.assertEqual(previews[0]['internshipId'], 1)
        self.assertEqual(previews[0]['roleTitle'], 'Software Engineer')
        self.assertEqual(previews[0]['status'], 'Ongoing')
        self.assertEqual(previews[1]['company_name'], 'Data Inc')
        self.assertIsNone(previews[1]['company_photoPath'])
        self.assertEqual(previews[1]['internshipId'], 2)
        self.assertEqual(previews[1]['roleTitle'], 'Data Scientist')
        self.assertEqual(previews[1]['status'], 'Finished')
        mock_get_preview_by_student_id.assert_called_once_with(1)
        mock_close.assert_called_once()

    
    @patch.object(InternshipDB, 'get_preview_by_student_id', return_value=[])
    @patch.object(InternshipDB, 'close')
    def test_get_preview_by_studentId_returns_empty_list(self, mock_close, mock_get_preview_by_student_id):
        previews = Internship.get_preview_by_studentId(1)
        self.assertEqual(previews, [])
        mock_get_preview_by_student_id.assert_called_once_with(1)
        mock_close.assert_called_once()

    
    @patch.object(InternshipDB, 'get_preview_by_student_id', side_effect=Exception('Database error'))
    @patch.object(InternshipDB, 'close')
    def test_get_preview_by_studentId_raises_exception(self, mock_close, mock_get_preview_by_student_id):
        with self.assertRaises(Exception) as context:
            Internship.get_preview_by_studentId(1)
        self.assertEqual(str(context.exception), 'Database error')
        mock_get_preview_by_student_id.assert_called_once_with(1)
        mock_close.assert_called_once()


    @patch.object(InternshipDB, 'get_preview_by_university_id', return_value=[
        {
            'student_name': 'Alice Johnson',
            'company_name': 'Innovate LLC',
            'internshipId': 1,
            'roleTitle': 'Product Manager',
            'status': 'Ongoing'
        },
        {
            'student_name': 'Bob Brown',
            'company_name': 'Tech Solutions',
            'internshipId': 2,
            'roleTitle': 'Backend Developer',
            'status': 'Finished'
        }
    ])
    @patch.object(InternshipDB, 'close')
    def test_get_preview_by_universityId(self, mock_close, mock_get_preview_by_university_id):
        previews = Internship.get_preview_by_universityId(1)
        self.assertEqual(len(previews), 2)
        self.assertEqual(previews[0]['student_name'], 'Alice Johnson')
        self.assertEqual(previews[0]['company_name'], 'Innovate LLC')
        self.assertEqual(previews[0]['internshipId'], 1)
        self.assertEqual(previews[0]['roleTitle'], 'Product Manager')
        self.assertEqual(previews[0]['status'], 'Ongoing')
        self.assertEqual(previews[1]['student_name'], 'Bob Brown')
        self.assertEqual(previews[1]['company_name'], 'Tech Solutions')
        self.assertEqual(previews[1]['internshipId'], 2)
        self.assertEqual(previews[1]['roleTitle'], 'Backend Developer')
        self.assertEqual(previews[1]['status'], 'Finished')
        mock_get_preview_by_university_id.assert_called_once_with(1)
        mock_close.assert_called_once()

    
    @patch.object(InternshipDB, 'get_preview_by_university_id', return_value=[])
    @patch.object(InternshipDB, 'close')
    def test_get_preview_by_universityId_returns_empty_list(self, mock_close, mock_get_preview_by_university_id):
        previews = Internship.get_preview_by_universityId(1)
        self.assertEqual(previews, [])
        mock_get_preview_by_university_id.assert_called_once_with(1)
        mock_close.assert_called_once()

    
    @patch.object(InternshipDB, 'get_preview_by_university_id', side_effect=Exception('Database error'))
    @patch.object(InternshipDB, 'close')
    def test_get_preview_by_universityId_raises_exception(self, mock_close, mock_get_preview_by_university_id):
        with self.assertRaises(Exception) as context:
            Internship.get_preview_by_universityId(1)
        self.assertEqual(str(context.exception), 'Database error')
        mock_get_preview_by_university_id.assert_called_once_with(1)
        mock_close.assert_called_once()

if __name__ == '__main__':
    unittest.main()