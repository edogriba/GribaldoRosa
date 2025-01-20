import {
  getUniversityList,
  universityRegistration
} from './university';

import {
  getStudentsList,
  studentRegistration
} from './student'

import {
  userLogin
} from './user'

import { example } from './example';

export const Method = {
  GET: 'GET',
  POST: 'POST',
  DELETE: 'DELETE',
  PUT: 'PUT',
  PATCH: 'PATCH',
};

export const api = {
  example,
  getUniversityList,
  getStudentsList,
  studentRegistration,
  universityRegistration,
  userLogin
};
