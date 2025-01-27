import { Method } from './api';
import { requestAuth } from './request';

const InternshipEndPoint = {
    POSITION_LIST: '/api/internship/get_by_company',
    INTERNSHIP_LIST: '/api/internship/get_by_student',
};

export const getInternshipList = async (data) => 
  requestAuth(`${InternshipEndPoint.INTERNSHIP_LIST}`, Method.POST,  data );

export const getPositionList = async (data) => 
    requestAuth(`${InternshipEndPoint.POSITION_LIST}`, Method.POST,  data );
  