import { Method } from './api';
import { request } from './request';

const StudentEndPoint = {
  GET_STUDENT_LIST: '/studentlist',
  STUDENT_REGISTRATION: '/register/student'
};


export const getStudentsList = async () =>
  request(`${StudentEndPoint.GET_STUDENT_LIST}`, Method.GET, null);


export const studentRegistration = async (data) => 
  request(`${StudentEndPoint.STUDENT_REGISTRATION}`, Method.POST, { data });