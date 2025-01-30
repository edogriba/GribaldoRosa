import { Method } from './api';
import { request, requestAuth } from './request';

const StudentEndPoint = {
  GET_STUDENT_LIST: '/api/studentlist',
  STUDENT_REGISTRATION: '/api/register/student',
  INTERNSHIP_LIST: '/api/internship/get_by_student'
};


export const getStudentsList = async () =>
  request(`${StudentEndPoint.GET_STUDENT_LIST}`, Method.GET, null);


export const studentRegistration = async (data) => 
  request(`${StudentEndPoint.STUDENT_REGISTRATION}`, Method.POST,  data );


export const getInternshipListStudent = async (data) => 
  requestAuth(`${StudentEndPoint.INTERNSHIP_LIST}`, Method.POST,  data );