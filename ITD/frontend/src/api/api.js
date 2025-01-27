import {
  getUniversityList,
  universityRegistration
} from './university';

import {
  getStudentsList,
  studentRegistration
} from './student'

import {
  companyRegistration
} from './company'

import {
  userLogin, 
  userLogout, 
  userAuthenticated
} from './user'


import { example } from './example';
import { getInternshipList, getPositionList } from './internship';

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
  getInternshipList,
  getPositionList
};
