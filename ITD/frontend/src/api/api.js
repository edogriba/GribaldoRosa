import {
  getUniversityList,
  universityRegistration,
  updateUniversity
} from './university';

import {
  getStudentsList,
  studentRegistration,
  updateStudent
} from './student'

import {
  companyRegistration,
  updateCompany
} from './company'

import {
  userLogin, 
  userLogout, 
  userAuthenticated,
} from './user'

import { 
  getApplicationListCompany, 
  getApplicationListStudent,
  getApplicationStudent,
  getApplicationCompany,
  acceptApplication,
  rejectApplication,
  assessApplication,
  createApplication,
  refuseApplication,
  confirmApplication
} from './application';


import { example } from './example';

import { 
  getPositionListCompany,
  getPositionListStudent,
  getPosition,
  createPosition, 
  closePosition,
  getInternshipListStudent,
  getInternshipListCompany,
  getInternshipListUniversity,
  getInternship,
  finishInternship,
  searchNoFilters,
  searchFilters,
  getFilters,
  addComplaint,
  createAssessment,
} from './internship';

export const Method = {
  GET: 'GET',
  POST: 'POST',
  DELETE: 'DELETE',
  PUT: 'PUT',
  PATCH: 'PATCH',
};

export const api = {
  example,
  userAuthenticated,
  getUniversityList,
  getStudentsList,
  studentRegistration,
  companyRegistration,
  universityRegistration,
  userLogin, 
  userLogout,
  getPositionListCompany,
  getPositionListStudent,
  getPosition,
  createPosition, 
  closePosition,
  getApplicationListCompany,
  getApplicationListStudent,
  getApplicationStudent,
  getApplicationCompany,
  acceptApplication,
  rejectApplication,
  assessApplication,
  getInternshipListStudent,
  getInternshipListCompany,
  getInternshipListUniversity,
  updateStudent,
  updateCompany,
  updateUniversity,
  getInternship,
  finishInternship,
  searchNoFilters,
  searchFilters,
  getFilters,
  createApplication,
  addComplaint,
  createAssessment,
  confirmApplication,
  refuseApplication
};
