import unittest
from unittest.mock import patch
from app.db.dbModels import AssessmentDB
from app.models import Assessment


class TestAssessment(unittest.TestCase):

    def setUp(self):
        self.assessment = Assessment(1, 101, '2023-10-01', 'https://www.assessment.com')

    def test_get_assessment_id(self):
        self.assertEqual(self.assessment.get_assessment_id(), 1)

    def test_get_application_id(self):
        self.assertEqual(self.assessment.get_application_id(), 101)

    def test_get_date(self):
        self.assertEqual(self.assessment.get_date(), '2023-10-01')

    def test_get_link(self):
        self.assertEqual(self.assessment.get_link(), 'https://www.assessment.com')

    def test_to_dict(self):
        expected_dict = {
            'assessmentId': 1,
            'applicationId': 101,
            'date': '2023-10-01',
            'link': 'https://www.assessment.com'
        }
        self.assertEqual(self.assessment.to_dict(), expected_dict)


    @patch.object(AssessmentDB, 'insert', return_value=1)
    @patch.object(AssessmentDB, 'close')
    def test_add_assessment(self, mock_close, mock_insert):
        new_assessment = Assessment.add(101, '2023-10-01', 'https://www.assessment.com')
        self.assertIsInstance(new_assessment, Assessment)
        self.assertEqual(new_assessment.assessmentId, 1)
        self.assertEqual(new_assessment.applicationId, 101)
        self.assertEqual(new_assessment.date, '2023-10-01')
        self.assertEqual(new_assessment.link, 'https://www.assessment.com')

    
    @patch.object(AssessmentDB, 'insert', return_value=None)
    @patch.object(AssessmentDB, 'close')
    def test_add_assessment_returns_none(self, mock_close, mock_insert):
        new_assessment = Assessment.add(101, '2023-10-01', 'https://www.assessment.com')
        self.assertIsNone(new_assessment)

    
    @patch.object(AssessmentDB, 'get_last_assessment_by_application_id', return_value={'assessmentId': 1, 'applicationId': 101, 'date': '2023-10-01', 'link': 'https://www.assessment.com'})
    @patch.object(AssessmentDB, 'close')
    def test_get_last_assessment_by_application_id(self, mock_get_last_assessment_by_application_id, mock_close):
        last_assessment = Assessment.get_last_assessment_by_application_id(101)
        self.assertIsInstance(last_assessment, Assessment)
        self.assertEqual(last_assessment.assessmentId, 1)
        self.assertEqual(last_assessment.applicationId, 101)
        self.assertEqual(last_assessment.date, '2023-10-01')
        self.assertEqual(last_assessment.link, 'https://www.assessment.com')

    
    @patch.object(AssessmentDB, 'get_last_assessment_by_application_id', return_value=None)
    @patch.object(AssessmentDB, 'close')
    def test_get_last_assessment_by_application_id_returns_none(self, mock_get_last_assessment_by_application_id, mock_close):
        last_assessment = Assessment.get_last_assessment_by_application_id(101)
        self.assertIsNone(last_assessment)

    
    @patch.object(AssessmentDB, 'get_last_assessment_by_application_id', side_effect=Exception)
    @patch.object(AssessmentDB, 'close')
    def test_get_last_assessment_by_application_id_raises_exception(self, mock_get_last_assessment_by_application_id, mock_close):
        with self.assertRaises(Exception):
            Assessment.get_last_assessment_by_application_id(101)
            
    