import { Method } from './api';
import { request, requestAuthWithErrorToast } from './request';

const StudentEndPoint = {
  GET_STUDENT_LIST: '/api/studentlist',
  STUDENT_REGISTRATION: '/api/register/student',
  STUDENT_UPDATE: '/api/update/student',
};


export const getStudentsList = async () =>
  request(`${StudentEndPoint.GET_STUDENT_LIST}`, Method.GET, null);


export const studentRegistration = async (data) => 
  request(`${StudentEndPoint.STUDENT_REGISTRATION}`, Method.POST,  data );

export const updateStudent = async (data) =>
  requestAuthWithErrorToast(`${StudentEndPoint.STUDENT_UPDATE}`, Method.POST, data, {}, true);