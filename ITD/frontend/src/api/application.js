import { Method } from './api';
import { requestAuthWithErrorToast } from './request';

const ApplicationEndPoint = {
    APPLICATION_LIST_COMPANY: '/api/application/get_by_internship_position',
    APPLICATION_LIST_STUDENT: '/api/application/get_by_student',
    APPLICATION: '/api/application/get_by_id',
    ACCEPT_APPLICATION: '/api/application/accept',
    ASSESS_APPLICATION: '/api/application/assess',
    REJECT_APPLICATION: '/api/application/reject'
};

export const getApplicationListCompany = async (data) => 
  requestAuthWithErrorToast(`${ApplicationEndPoint.APPLICATION_LIST_COMPANY}`, Method.POST,  data);

export const getApplicationListStudent = async (data) =>
  requestAuthWithErrorToast(`${ApplicationEndPoint.APPLICATION_LIST_STUDENT}`, Method.POST, data);

export const getApplicationStudent = async (data) => 
  requestAuthWithErrorToast(`${ApplicationEndPoint.APPLICATION}`, Method.POST, data);

export const getApplicationCompany = async (data) =>
  requestAuthWithErrorToast(`${ApplicationEndPoint.APPLICATION}`, Method.POST, data);

export const acceptApplication = async (data) =>
  requestAuthWithErrorToast(`${ApplicationEndPoint.ACCEPT_APPLICATION}`, Method.POST, data);

export const assessApplication = async (data) =>
  requestAuthWithErrorToast(`${ApplicationEndPoint.ASSESS_APPLICATION}`, Method.POST, data);

export const rejectApplication = async (data) =>
  requestAuthWithErrorToast(`${ApplicationEndPoint.REJECT_APPLICATION}`, Method.POST, data);