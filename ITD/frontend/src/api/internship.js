import { Method } from './api';
import { requestAuth, requestAuthWithErrorToast } from './request';

const InternshipEndPoint = {
    POSITION_LIST_COMPANY: '/api/internship_position/get_by_company',
    POSITION_LIST_STUDENT: '/api/internship_position/get_by_student',
    POSITION: '/api/internship_position/get_by_id',
    CREATE_POSITION: '/api/internship_position/post',
    CLOSE_POSITION: '/api/internship_position/close',
    INTERNSHIP_LIST_STUDENT: '/api/internship/get_by_student',
    INTERNSHIP_LIST_COMPANY: '/api/internship/get_by_company',
    INTERNSHIP_LIST_UNIVERSITY: '/api/internship/get_by_university'
  };


export const getPositionListCompany = async (data) => 
    requestAuth(`${InternshipEndPoint.POSITION_LIST_COMPANY}`, Method.POST,  data );

export const getPositionListStudent = async (data) => 
  requestAuth(`${InternshipEndPoint.POSITION_LIST_STUDENT}`, Method.POST,  data );
  
export const getPosition = async (data) => 
  requestAuth(`${InternshipEndPoint.POSITION}`, Method.POST,  data );

export const createPosition = async (data) => 
  requestAuthWithErrorToast(`${InternshipEndPoint.CREATE_POSITION}`, Method.POST,  data);

export const closePosition = async (data) => 
  requestAuthWithErrorToast(`${InternshipEndPoint.CLOSE_POSITION}`, Method.POST,  data);

export const getInternshipListStudent = async (data) => 
  requestAuth(`${InternshipEndPoint.INTERNSHIP_LIST_STUDENT}`, Method.POST,  data );

export const getInternshipListCompany = async (data) => 
  requestAuth(`${InternshipEndPoint.INTERNSHIP_LIST_COMPANY}`, Method.POST,  data );

export const getInternshipListUniversity = async (data) =>
  requestAuth(`${InternshipEndPoint.INTERNSHIP_LIST_UNIVERSITY}`, Method.POST, data);