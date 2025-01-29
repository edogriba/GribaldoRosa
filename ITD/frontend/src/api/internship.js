import { Method } from './api';
import { requestAuth, requestAuthWithErrorToast } from './request';

const InternshipEndPoint = {
    POSITION_LIST: '/api/internship/get_by_company',
    POSITION: '/api/internship/get_by_id',
    CREATE_POSITION: '/api/internship/post',
    CLOSE_POSITION: '/api/internship/close'
};


export const getPositionList = async (data) => 
    requestAuth(`${InternshipEndPoint.POSITION_LIST}`, Method.POST,  data );
  
export const getPosition = async (data) => 
  requestAuth(`${InternshipEndPoint.POSITION}`, Method.POST,  data );

export const createPosition = async (data) => 
  requestAuthWithErrorToast(`${InternshipEndPoint.CREATE_POSITION}`, Method.POST,  data);

export const closePosition = async (data) => 
  requestAuthWithErrorToast(`${InternshipEndPoint.CLOSE_POSITION}`, Method.POST,  data);
