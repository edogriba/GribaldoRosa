import {
  getUniversityList,
  universityRegistration
} from './university';

import {
  getStudentsList,
  studentRegistration,
  getInternshipListStudent
} from './student'

import {
  companyRegistration,
} from './company'

import {
  userLogin, 
  userLogout, 
  userAuthenticated
} from './user'

import { 
  getApplicationListCompany, 
  getApplicationListStudent,
  getApplicationStudent,
  getApplicationCompany,
  acceptApplication,
  rejectApplication,
  assessApplication
} from './application';


import { example } from './example';

import { 
  getPositionList,
  getPosition,
  createPosition, 
  closePosition 
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
  getPositionList,
  getPosition,
  createPosition, 
  closePosition,
  getApplicationListCompany,
  getApplicationListStudent,
  getInternshipListStudent, 
  getApplicationStudent,
  getApplicationCompany,
  acceptApplication,
  rejectApplication,
  assessApplication
};
