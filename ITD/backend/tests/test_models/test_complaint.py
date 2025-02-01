import unittest
from unittest.mock import patch
from app.models import Complaint
from app.db.dbModels import ComplaintDB


class TestComplaint(unittest.TestCase):

    def setUp(self):
        self.complaint = Complaint(1, 101, 201, '2023-10-01', 'Test complaint content')


    def test_get_complaint_id(self):
        self.assertEqual(self.complaint.get_complaint_id(), 1)


    def test_get_internship_id(self):
        self.assertEqual(self.complaint.get_internship_id(), 101)


    def test_get_source_id(self):
        self.assertEqual(self.complaint.get_source_id(), 201)


    def test_get_date(self):
        self.assertEqual(self.complaint.get_date(), '2023-10-01')


    def test_get_content(self):
        self.assertEqual(self.complaint.get_content(), 'Test complaint content')


    def test_to_dict(self):
        expected_dict = {
            'complaintId': 1,
            'internshipId': 101,
            'sourceId': 201,
            'date': '2023-10-01',
            'content': 'Test complaint content'
        }
        self.assertEqual(self.complaint.to_dict(), expected_dict)


    @patch.object(ComplaintDB, 'insert', return_value=1)
    @patch.object(ComplaintDB, 'close')
    def test_add_complaint(self, mock_close, mock_insert):
        new_complaint = Complaint.add(101, 201, '2023-10-01', 'New complaint content')
        self.assertIsInstance(new_complaint, Complaint)
        self.assertEqual(new_complaint.complaintId, 1)
        self.assertEqual(new_complaint.internshipId, 101)
        self.assertEqual(new_complaint.sourceId, 201)
        self.assertEqual(new_complaint.date, '2023-10-01')
        self.assertEqual(new_complaint.content, 'New complaint content')


    @patch.object(ComplaintDB, 'insert', return_value=None)
    @patch.object(ComplaintDB, 'close')
    def test_add_complaint_returns_none(self, mock_close, mock_insert):
        new_complaint = Complaint.add(101, 201, '2023-10-01', 'New complaint content')
        self.assertIsNone(new_complaint)


    @patch.object(ComplaintDB, 'insert', side_effect=Exception('Database error'))
    @patch.object(ComplaintDB, 'close')
    def test_add_complaint_raises_exception(self, mock_close, mock_insert):
        with self.assertRaises(Exception) as context:
            Complaint.add(101, 201, '2023-10-01', 'New complaint content')
        self.assertEqual(str(context.exception), 'Database error')


    @patch.object(ComplaintDB, 'get_by_internship_id', return_value=[
        {'complaintId': 1, 'internshipId': 101, 'sourceId': 201, 'date': '2023-10-01', 'content': 'Test complaint content'}
    ])
    @patch.object(ComplaintDB, 'close')
    def test_get_by_internship_id(self, mock_close, mock_get_by_internship_id):
        complaints = Complaint.get_by_internship_id(101)
        self.assertEqual(len(complaints), 1)
        self.assertIsInstance(complaints[0], Complaint)
        self.assertEqual(complaints[0].complaintId, 1)
        self.assertEqual(complaints[0].internshipId, 101)
        self.assertEqual(complaints[0].sourceId, 201)
        self.assertEqual(complaints[0].date, '2023-10-01')
        self.assertEqual(complaints[0].content, 'Test complaint content')


    @patch.object(ComplaintDB, 'get_by_internship_id', return_value=None)
    @patch.object(ComplaintDB, 'close')
    def test_get_by_internship_id_returns_empty_list(self, mock_close, mock_get_by_internship_id):
        complaints = Complaint.get_by_internship_id(101)
        self.assertEqual(complaints, [])


    @patch.object(ComplaintDB, 'get_by_internship_id', side_effect=Exception('Database error'))
    @patch.object(ComplaintDB, 'close')
    def test_get_by_internship_id_raises_exception(self, mock_close, mock_get_by_internship_id):
        with self.assertRaises(Exception) as context:
            Complaint.get_by_internship_id(101)
        self.assertEqual(str(context.exception), 'Database error')


if __name__ == '__main__':
    unittest.main()