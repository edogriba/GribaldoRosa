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
    INTERNSHIP_LIST_UNIVERSITY: '/api/internship/get_by_university',
    INTERNSHIP: '/api/internship/get_by_id',
    FINISH_INTERNSHIP: '/api/internship/finish',
    SEARCH_NO_FILTERS: '/api/search_without_filters',
    GET_FILTERS: '/api/search/filters',
    SEARCH_WITH_FILTERS: '/api/search_with_filters',
    CREATE_COMPLAINT: '/api/complaint/create',
    CREATE_ASSESSMENT: '/api/assessment/create',
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

export const getInternship = async (data) =>
  requestAuth(`${InternshipEndPoint.INTERNSHIP}`, Method.POST, data);

export const finishInternship = async (data) =>
  requestAuthWithErrorToast(`${InternshipEndPoint.FINISH_INTERNSHIP}`, Method.POST, data);

export const getFilters = async () =>
  requestAuthWithErrorToast(`${InternshipEndPoint.GET_FILTERS}`, Method.GET);

export const searchNoFilters = async () =>
  requestAuthWithErrorToast(`${InternshipEndPoint.SEARCH_NO_FILTERS}`, Method.GET);

export const searchFilters = async (data) =>
  requestAuthWithErrorToast(`${InternshipEndPoint.SEARCH_WITH_FILTERS}`, Method.POST, data);

export const addComplaint = async (data) =>
  requestAuthWithErrorToast(`${InternshipEndPoint.CREATE_COMPLAINT}`, Method.POST, data);

export const createAssessment = async (data) =>
  requestAuthWithErrorToast(`${InternshipEndPoint.CREATE_ASSESSMENT}`, Method.POST, data);