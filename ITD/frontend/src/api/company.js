import { Method } from './api';
import { request, requestAuthWithErrorToast} from './request';

const CompanyEndPoint = {
  COMPANY_REGISTRATION: '/api/register/company',
  UPDATE_COMPANY: '/api/update/company',
};

export const companyRegistration = async (data) => 
  request(`${CompanyEndPoint.COMPANY_REGISTRATION}`, Method.POST,  data, {}, true);

export const updateCompany = async (data) =>  
  requestAuthWithErrorToast(`${CompanyEndPoint.UPDATE_COMPANY}`, Method.POST, data, {}, true);