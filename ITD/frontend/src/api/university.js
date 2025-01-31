import { Method } from './api';
import { request, requestAuthWithErrorToast } from './request';

const UniversityEndPoint = {
  GET_UNIVERSITY_LIST: '/api/universitylist',
  UNIVERSITY_REGISTRATION: '/api/register/university',
  UNIVERSITY_UPDATE: '/api/update/university',
};


export const getUniversityList = async () =>
  request(`${UniversityEndPoint.GET_UNIVERSITY_LIST}`, Method.GET, null);


export const universityRegistration = async (data) => 
  request(`${UniversityEndPoint.UNIVERSITY_REGISTRATION}`, Method.POST, data, {}, true);

export const updateUniversity = async (data) =>
  requestAuthWithErrorToast(`${UniversityEndPoint.UNIVERSITY_UPDATE}`, Method.POST, data, {}, true);