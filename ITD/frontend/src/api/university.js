import { Method } from './api';
import { request } from './request';

const UniversityEndPoint = {
  GET_UNIVERSITY_LIST: '/api/universitylist',
  UNIVERSITY_REGISTRATION: '/api/register/university'
};


export const getUniversityList = async () =>
  request(`${UniversityEndPoint.GET_UNIVERSITY_LIST}`, Method.GET, null);


export const universityRegistration = async (data) => 
  request(`${UniversityEndPoint.UNIVERSITY_REGISTRATION}`, Method.POST, {data});