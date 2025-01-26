import { Method } from './api';
import { request } from './request';

const CompanyEndPoint = {
  COMPANY_REGISTRATION: '/api/register/company'
};

export const companyRegistration = async (data) => 
  request(`${CompanyEndPoint.COMPANY_REGISTRATION}`, Method.POST,  data);