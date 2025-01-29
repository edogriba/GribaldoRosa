import unittest
from unittest.mock import patch
from app.models import InternshipPosition, Company
from app.db.dbModels import InternshipPositionDB

class TestInternshipPosition(unittest.TestCase):

    def setUp(self):
        self.internshipPosition1 = InternshipPosition(
            internshipPositionId=1,
            companyId=1,
            programName='Program A',
            duration=6,
            location='Location A',
            roleTitle='Role A',
            skillsRequired='Skills A',
            compensation=1000,
            benefits='Benefits A',
            languagesRequired='English',
            description='Description A',
            status='Open'
        )

        self.internshipPosition2 = InternshipPosition(
            internshipPositionId=2,
            companyId=2,
            programName='Program B',
            duration=12,
            location='Location B',
            roleTitle='Role B',
            skillsRequired='Skills B',
            compensation=None,
            benefits='Benefits B',
            languagesRequired='Spanish',
            description='Description B',
            status='Closed'
        )

        self.internshipPosition3 = InternshipPosition(
            internshipPositionId=3,
            companyId=3,
            programName='Program C',
            duration=9,
            location='Location C',
            roleTitle='Role C',
            skillsRequired='Skills C',
            compensation=1500,
            benefits=None,
            languagesRequired='French',
            description='Description C',
            status='Open'
        )

        self.internshipPosition4 = InternshipPosition(
            internshipPositionId=4,
            companyId=4,
            programName='Program D',
            duration=18,
            location='Location D',
            roleTitle='Role D',
            skillsRequired='Skills D',
            compensation=None,
            benefits=None,
            languagesRequired='German',
            description='Description D',
            status='Closed'
        )

        
    def test_get_internshipPositionId(self):
        self.assertEqual(self.internshipPosition1.get_internshipPositionId(), 1)
        self.assertEqual(self.internshipPosition2.get_internshipPositionId(), 2)
        self.assertEqual(self.internshipPosition3.get_internshipPositionId(), 3)
        self.assertEqual(self.internshipPosition4.get_internshipPositionId(), 4)
        

    def test_get_companyId(self):
        self.assertEqual(self.internshipPosition1.get_companyId(), 1)
        self.assertEqual(self.internshipPosition2.get_companyId(), 2)
        self.assertEqual(self.internshipPosition3.get_companyId(), 3)
        self.assertEqual(self.internshipPosition4.get_companyId(), 4)

    
    def test_get_programName(self):
        self.assertEqual(self.internshipPosition1.get_programName(), 'Program A')
        self.assertEqual(self.internshipPosition2.get_programName(), 'Program B')
        self.assertEqual(self.internshipPosition3.get_programName(), 'Program C')
        self.assertEqual(self.internshipPosition4.get_programName(), 'Program D')

    
    def test_get_duration(self):
        self.assertEqual(self.internshipPosition1.get_duration(), 6)
        self.assertEqual(self.internshipPosition2.get_duration(), 12)
        self.assertEqual(self.internshipPosition3.get_duration(), 9)
        self.assertEqual(self.internshipPosition4.get_duration(), 18)

    
    def test_get_location(self):
        self.assertEqual(self.internshipPosition1.get_location(), 'Location A')
        self.assertEqual(self.internshipPosition2.get_location(), 'Location B')
        self.assertEqual(self.internshipPosition3.get_location(), 'Location C')
        self.assertEqual(self.internshipPosition4.get_location(), 'Location D')

    
    def test_get_roleTitle(self):
        self.assertEqual(self.internshipPosition1.get_roleTitle(), 'Role A')
        self.assertEqual(self.internshipPosition2.get_roleTitle(), 'Role B')
        self.assertEqual(self.internshipPosition3.get_roleTitle(), 'Role C')
        self.assertEqual(self.internshipPosition4.get_roleTitle(), 'Role D')


    def test_get_skillsRequired(self):
        self.assertEqual(self.internshipPosition1.get_skillsRequired(), 'Skills A')
        self.assertEqual(self.internshipPosition2.get_skillsRequired(), 'Skills B')
        self.assertEqual(self.internshipPosition3.get_skillsRequired(), 'Skills C')
        self.assertEqual(self.internshipPosition4.get_skillsRequired(), 'Skills D')

    
    def test_get_compensation(self):
        self.assertEqual(self.internshipPosition1.get_compensation(), 1000)
        self.assertIsNone(self.internshipPosition2.get_compensation())
        self.assertEqual(self.internshipPosition3.get_compensation(), 1500)
        self.assertIsNone(self.internshipPosition4.get_compensation())

    
    def test_get_benefits(self):
        self.assertEqual(self.internshipPosition1.get_benefits(), 'Benefits A')
        self.assertEqual(self.internshipPosition2.get_benefits(), 'Benefits B')
        self.assertIsNone(self.internshipPosition3.get_benefits())
        self.assertIsNone(self.internshipPosition4.get_benefits())

    
    def test_get_languagesRequired(self):
        self.assertEqual(self.internshipPosition1.get_languagesRequired(), 'English')
        self.assertEqual(self.internshipPosition2.get_languagesRequired(), 'Spanish')
        self.assertEqual(self.internshipPosition3.get_languagesRequired(), 'French')
        self.assertEqual(self.internshipPosition4.get_languagesRequired(), 'German')

    
    def test_get_description(self):
        self.assertEqual(self.internshipPosition1.get_description(), 'Description A')
        self.assertEqual(self.internshipPosition2.get_description(), 'Description B')
        self.assertEqual(self.internshipPosition3.get_description(), 'Description C')
        self.assertEqual(self.internshipPosition4.get_description(), 'Description D')

    
    def test_get_status(self):
        self.assertEqual(self.internshipPosition1.get_status(), 'Open')
        self.assertEqual(self.internshipPosition2.get_status(), 'Closed')
        self.assertEqual(self.internshipPosition3.get_status(), 'Open')
        self.assertEqual(self.internshipPosition4.get_status(), 'Closed')

    
    def test_to_dict(self):
        self.assertEqual(self.internshipPosition1.to_dict(), {
            'internshipPositionId': 1,
            'companyId': 1,
            'programName': 'Program A',
            'duration': 6,
            'location': 'Location A',
            'roleTitle': 'Role A',
            'skillsRequired': 'Skills A',
            'compensation': 1000,
            'benefits': 'Benefits A',
            'languagesRequired': 'English',
            'description': 'Description A',
            'status': 'Open'
        })

        self.assertEqual(self.internshipPosition2.to_dict(), {
            'internshipPositionId': 2,
            'companyId': 2,
            'programName': 'Program B',
            'duration': 12,
            'location': 'Location B',
            'roleTitle': 'Role B',
            'skillsRequired': 'Skills B',
            'compensation': None,
            'benefits': 'Benefits B',
            'languagesRequired': 'Spanish',
            'description': 'Description B',
            'status': 'Closed'
        })

        self.assertEqual(self.internshipPosition3.to_dict(), {
            'internshipPositionId': 3,
            'companyId': 3,
            'programName': 'Program C',
            'duration': 9,
            'location': 'Location C',
            'roleTitle': 'Role C',
            'skillsRequired': 'Skills C',
            'compensation': 1500,
            'benefits': None,
            'languagesRequired': 'French',
            'description': 'Description C',
            'status': 'Open'
        })

        self.assertEqual(self.internshipPosition4.to_dict(), {
            'internshipPositionId': 4,
            'companyId': 4,
            'programName': 'Program D',
            'duration': 18,
            'location': 'Location D',
            'roleTitle': 'Role D',
            'skillsRequired': 'Skills D',
            'compensation': None,
            'benefits': None,
            'languagesRequired': 'German',
            'description': 'Description D',
            'status': 'Closed'
        })


    @patch.object(InternshipPositionDB, 'insert', return_value=3)
    @patch.object(InternshipPositionDB, 'close')
    def test_add_internshipPosition(self, mock_close, mock_insert):
        internship = InternshipPosition.add(
            companyId=1,
            programName='Program C',
            duration=3,
            location='Location C',
            roleTitle='Role C',
            skillsRequired='Skills C',
            compensation=1500,
            benefits='Benefits C',
            languagesRequired='French',
            description='Description C'
        )

        self.assertEqual(internship.internshipPositionId, 3)
        self.assertEqual(internship.companyId, 1)
        self.assertEqual(internship.programName, 'Program C')
        self.assertEqual(internship.duration, 3)
        self.assertEqual(internship.location, 'Location C')
        self.assertEqual(internship.roleTitle, 'Role C')
        self.assertEqual(internship.skillsRequired, 'Skills C')
        self.assertEqual(internship.compensation, 1500)
        self.assertEqual(internship.benefits, 'Benefits C')
        self.assertEqual(internship.languagesRequired, 'French')
        self.assertEqual(internship.description, 'Description C')
        self.assertEqual(internship.status, 'Open')

        mock_insert.assert_called_once_with(
            companyId=1,
            programName='Program C',
            duration=3,
            location='Location C',
            roleTitle='Role C',
            skillsRequired='Skills C',
            compensation=1500,
            benefits='Benefits C',
            languagesRequired='French',
            description='Description C',
            status='Open'
        )
        mock_close.assert_called_once()


    @patch.object(InternshipPositionDB, 'insert', return_value=None)
    @patch.object(InternshipPositionDB, 'close')
    def test_add_internshipPosition_returns_none(self, mock_close, mock_insert):
        internship = InternshipPosition.add(
            companyId=1,
            programName='Program C',
            duration=3,
            location='Location C',
            roleTitle='Role C',
            skillsRequired='Skills C',
            compensation=1500,
            benefits='Benefits C',
            languagesRequired='French',
            description='Description C'
        )

        self.assertIsNone(internship)
        mock_insert.assert_called_once_with(
            companyId=1,
            programName='Program C',
            duration=3,
            location='Location C',
            roleTitle='Role C',
            skillsRequired='Skills C',
            compensation=1500,
            benefits='Benefits C',
            languagesRequired='French',
            description='Description C',
            status='Open'
        )
        mock_close.assert_called_once()


    @patch.object(InternshipPositionDB, 'insert', side_effect=Exception('Database error'))
    @patch.object(InternshipPositionDB, 'close')
    def test_add_internshipPosition_raises_exception(self, mock_close, mock_insert):
        with self.assertRaises(Exception) as context:
            InternshipPosition.add(
                companyId=1,
                programName='Program C',
                duration=3,
                location='Location C',
                roleTitle='Role C',
                skillsRequired='Skills C',
                compensation=1500,
                benefits='Benefits C',
                languagesRequired='French',
                description='Description C'
            )

        self.assertTrue('Database error' in str(context.exception))
        mock_insert.assert_called_once_with(
            companyId=1,
            programName='Program C',
            duration=3,
            location='Location C',
            roleTitle='Role C',
            skillsRequired='Skills C',
            compensation=1500,
            benefits='Benefits C',
            languagesRequired='French',
            description='Description C',
            status='Open'
        )
        mock_close.assert_called_once()


    @patch.object(InternshipPositionDB, 'get_by_id', return_value={
        'internshipPositionId': 1,
        'companyId': 1,
        'programName': 'Program A',
        'duration': 6,
        'location': 'Location A',
        'roleTitle': 'Role A',
        'skillsRequired': 'Skills A',
        'compensation': 1000,
        'benefits': 'Benefits A',
        'languagesRequired': 'English',
        'description': 'Description A',
        'status': 'Open'
    })
    @patch.object(InternshipPositionDB, 'close')
    def test_get_by_id(self, mock_close, mock_get_by_id):
        internship = InternshipPosition.get_by_id(1)
        self.assertIsNotNone(internship)
        self.assertEqual(internship.internshipPositionId, 1)
        self.assertEqual(internship.companyId, 1)
        self.assertEqual(internship.programName, 'Program A')
        self.assertEqual(internship.duration, 6)
        self.assertEqual(internship.location, 'Location A')
        self.assertEqual(internship.roleTitle, 'Role A')
        self.assertEqual(internship.skillsRequired, 'Skills A')
        self.assertEqual(internship.compensation, 1000)
        self.assertEqual(internship.benefits, 'Benefits A')
        self.assertEqual(internship.languagesRequired, 'English')
        self.assertEqual(internship.description, 'Description A')
        self.assertEqual(internship.status, 'Open')
        mock_get_by_id.assert_called_once_with(1)
        mock_close.assert_called_once()


    @patch.object(InternshipPositionDB, 'get_by_id', return_value=None)
    @patch.object(InternshipPositionDB, 'close')
    def test_get_by_id_returns_none(self, mock_close, mock_get_by_id):
        internship = InternshipPosition.get_by_id(99)
        self.assertIsNone(internship)
        mock_get_by_id.assert_called_once_with(99)
        mock_close.assert_called_once()


    @patch.object(InternshipPositionDB, 'get_by_id', side_effect=Exception('Database error'))
    @patch.object(InternshipPositionDB, 'close')
    def test_get_by_id_raises_exception(self, mock_close, mock_get_by_id):
        with self.assertRaises(Exception) as context:
            InternshipPosition.get_by_id(1)
        self.assertTrue('Database error' in str(context.exception))
        mock_get_by_id.assert_called_once_with(1)
        mock_close.assert_called_once()


    @patch.object(InternshipPositionDB, 'get_by_companyId', return_value=[
        {
            'internshipPositionId': 1,
            'companyId': 1,
            'programName': 'Program A',
            'duration': 6,
            'location': 'Location A',
            'roleTitle': 'Role A',
            'skillsRequired': 'Skills A',
            'compensation': 1000,
            'benefits': 'Benefits A',
            'languagesRequired': 'English',
            'description': 'Description A',
            'status': 'Open'
        },
        {
            'internshipPositionId': 2,
            'companyId': 1,
            'programName': 'Program B',
            'duration': 12,
            'location': 'Location B',
            'roleTitle': 'Role B',
            'skillsRequired': 'Skills B',
            'compensation': None,
            'benefits': 'Benefits B',
            'languagesRequired': 'Spanish',
            'description': 'Description B',
            'status': 'Closed'
        }
    ])
    @patch.object(InternshipPositionDB, 'close')
    def test_get_by_companyId(self, mock_close, mock_get_by_companyId):
        internships = InternshipPosition.get_by_companyId(1)
        self.assertEqual(len(internships), 2)

        self.assertEqual(internships[0].internshipPositionId, 1)
        self.assertEqual(internships[0].companyId, 1)
        self.assertEqual(internships[0].programName, 'Program A')
        self.assertEqual(internships[0].duration, 6)
        self.assertEqual(internships[0].location, 'Location A')
        self.assertEqual(internships[0].roleTitle, 'Role A')
        self.assertEqual(internships[0].skillsRequired, 'Skills A')
        self.assertEqual(internships[0].compensation, 1000)
        self.assertEqual(internships[0].benefits, 'Benefits A')
        self.assertEqual(internships[0].languagesRequired, 'English')
        self.assertEqual(internships[0].description, 'Description A')
        self.assertEqual(internships[0].status, 'Open')

        self.assertEqual(internships[1].internshipPositionId, 2)
        self.assertEqual(internships[1].companyId, 1)
        self.assertEqual(internships[1].programName, 'Program B')
        self.assertEqual(internships[1].duration, 12)
        self.assertEqual(internships[1].location, 'Location B')
        self.assertEqual(internships[1].roleTitle, 'Role B')
        self.assertEqual(internships[1].skillsRequired, 'Skills B')
        self.assertIsNone(internships[1].compensation)
        self.assertEqual(internships[1].benefits, 'Benefits B')
        self.assertEqual(internships[1].languagesRequired, 'Spanish')
        self.assertEqual(internships[1].description, 'Description B')
        self.assertEqual(internships[1].status, 'Closed')

        mock_get_by_companyId.assert_called_once_with(1)
        mock_close.assert_called_once()

    
    @patch.object(InternshipPositionDB, 'get_by_companyId', return_value=[])
    @patch.object(InternshipPositionDB, 'close')
    def test_get_by_companyId_returns_empty_list(self, mock_close, mock_get_by_companyId):
        internships = InternshipPosition.get_by_companyId(99)
        self.assertEqual(len(internships), 0)
        mock_get_by_companyId.assert_called_once_with(99)
        mock_close.assert_called_once()

    
    @patch.object(InternshipPositionDB, 'get_by_companyId', side_effect=Exception('Database error'))
    @patch.object(InternshipPositionDB, 'close')
    def test_get_by_companyId_raises_exception(self, mock_close, mock_get_by_companyId):
        with self.assertRaises(Exception) as context:
            InternshipPosition.get_by_companyId(1)
        self.assertTrue('Database error' in str(context.exception))
        mock_get_by_companyId.assert_called_once_with(1)
        mock_close.assert_called_once()


    @patch.object(InternshipPositionDB, 'get_by_program_name', return_value=[
        {
            'internshipPositionId': 1,
            'companyId': 1,
            'programName': 'Program A',
            'duration': 6,
            'location': 'Location A',
            'roleTitle': 'Role A',
            'skillsRequired': 'Skills A',
            'compensation': 1000,
            'benefits': 'Benefits A',
            'languagesRequired': 'English',
            'description': 'Description A',
            'status': 'Open'
        },
        {
            'internshipPositionId': 2,
            'companyId': 2,
            'programName': 'Program A',
            'duration': 12,
            'location': 'Location B',
            'roleTitle': 'Role B',
            'skillsRequired': 'Skills B',
            'compensation': None,
            'benefits': 'Benefits B',
            'languagesRequired': 'Spanish',
            'description': 'Description B',
            'status': 'Closed'
        }
    ])
    @patch.object(InternshipPositionDB, 'close')
    def test_get_by_programName(self, mock_close, mock_get_by_program_name):
        internships = InternshipPosition.get_by_programName('Program A')
        self.assertEqual(len(internships), 2)

        self.assertEqual(internships[0].internshipPositionId, 1)
        self.assertEqual(internships[0].companyId, 1)
        self.assertEqual(internships[0].programName, 'Program A')
        self.assertEqual(internships[0].duration, 6)
        self.assertEqual(internships[0].location, 'Location A')
        self.assertEqual(internships[0].roleTitle, 'Role A')
        self.assertEqual(internships[0].skillsRequired, 'Skills A')
        self.assertEqual(internships[0].compensation, 1000)
        self.assertEqual(internships[0].benefits, 'Benefits A')
        self.assertEqual(internships[0].languagesRequired, 'English')
        self.assertEqual(internships[0].description, 'Description A')
        self.assertEqual(internships[0].status, 'Open')

        self.assertEqual(internships[1].internshipPositionId, 2)
        self.assertEqual(internships[1].companyId, 2)
        self.assertEqual(internships[1].programName, 'Program A')
        self.assertEqual(internships[1].duration, 12)
        self.assertEqual(internships[1].location, 'Location B')
        self.assertEqual(internships[1].roleTitle, 'Role B')
        self.assertEqual(internships[1].skillsRequired, 'Skills B')
        self.assertIsNone(internships[1].compensation)
        self.assertEqual(internships[1].benefits, 'Benefits B')
        self.assertEqual(internships[1].languagesRequired, 'Spanish')
        self.assertEqual(internships[1].description, 'Description B')
        self.assertEqual(internships[1].status, 'Closed')

        mock_get_by_program_name.assert_called_once_with('Program A')
        mock_close.assert_called_once()


    @patch.object(InternshipPositionDB, 'get_by_program_name', return_value=[])
    @patch.object(InternshipPositionDB, 'close')
    def test_get_by_programName_returns_empty_list(self, mock_close, mock_get_by_program_name):
        internships = InternshipPosition.get_by_programName('Program A')
        self.assertEqual(len(internships), 0)
        mock_get_by_program_name.assert_called_once_with('Program A')
        mock_close.assert_called_once()

    
    @patch.object(InternshipPositionDB, 'get_by_program_name', side_effect=Exception('Database error'))
    @patch.object(InternshipPositionDB, 'close')
    def test_get_by_programName_raises_exception(self, mock_close, mock_get_by_program_name):
        with self.assertRaises(Exception) as context:
            InternshipPosition.get_by_programName('Program A')
        self.assertTrue('Database error' in str(context.exception))
        mock_get_by_program_name.assert_called_once_with('Program A')
        mock_close.assert_called_once()

    
    @patch.object(Company, 'get_by_id', return_value=Company(id=1, 
                                                             companyName='Company A', 
                                                             email='email@example.com', 
                                                             password='password', 
                                                             logoPath=None, 
                                                             description='Description A', 
                                                             location='Location A'))
    def test_get_company(self, mock_get_by_id):
        company = self.internshipPosition1.get_company()
        self.assertIsNotNone(company)
        self.assertEqual(company.id, 1)
        self.assertEqual(company.companyName, 'Company A')
        self.assertEqual(company.email, 'email@example.com')
        self.assertEqual(company.password, 'password')
        self.assertIsNone(company.logoPath)
        self.assertEqual(company.description, 'Description A')
        self.assertEqual(company.location, 'Location A')
        mock_get_by_id.assert_called_once_with(1)


    @patch.object(Company, 'get_by_id', return_value=None)
    def test_get_company_returns_none(self, mock_get_by_id):
        company = self.internshipPosition1.get_company()
        self.assertIsNone(company)
        mock_get_by_id.assert_called_once_with(1)


    @patch.object(Company, 'get_by_id', side_effect=Exception('Database error'))
    def test_get_company_raises_exception(self, mock_get_by_id):
        with self.assertRaises(Exception) as context:
            self.internshipPosition1.get_company()
        self.assertTrue('Database error' in str(context.exception))
        mock_get_by_id.assert_called_once_with(1)

    
    @patch.object(InternshipPositionDB, 'update_status', return_value=True)
    @patch.object(InternshipPositionDB, 'close')
    def test_close_internshipPosition(self, mock_close, mock_update_status):
        result = self.internshipPosition1.close()
        self.assertTrue(result)
        mock_update_status.assert_called_once_with(self.internshipPosition1.internshipPositionId, status='Closed')
        mock_close.assert_called_once()


    @patch.object(InternshipPositionDB, 'update_status', return_value=False)
    @patch.object(InternshipPositionDB, 'close')
    def test_close_internshipPosition_returns_false(self, mock_close, mock_update_status):
        result = self.internshipPosition1.close()
        self.assertFalse(result)
        mock_update_status.assert_called_once_with(self.internshipPosition1.internshipPositionId, status='Closed')
        mock_close.assert_called_once()


    @patch.object(InternshipPositionDB, 'update_status', side_effect=Exception('Database error'))
    @patch.object(InternshipPositionDB, 'close')
    def test_close_internshipPosition_raises_exception(self, mock_close, mock_update_status):
        with self.assertRaises(Exception) as context:
            self.internshipPosition1.close()
        self.assertTrue('Database error' in str(context.exception))
        mock_update_status.assert_called_once_with(self.internshipPosition1.internshipPositionId, status='Closed')
        mock_close.assert_called_once()

    
    def test_is_open(self):
        self.assertTrue(self.internshipPosition1.is_open())
        self.assertFalse(self.internshipPosition2.is_open())
        self.assertTrue(self.internshipPosition3.is_open())
        self.assertFalse(self.internshipPosition4.is_open())


    def test_is_closed(self):
        self.assertFalse(self.internshipPosition1.is_closed())
        self.assertTrue(self.internshipPosition2.is_closed())
        self.assertFalse(self.internshipPosition3.is_closed())
        self.assertTrue(self.internshipPosition4.is_closed())
    

if __name__ == '__main__':
    unittest.main()