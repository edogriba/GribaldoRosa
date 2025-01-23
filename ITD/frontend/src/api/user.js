import { Method } from './api';
import { request } from './request';

const UserEndPoint = {
  USER_LOGIN: '/api/userlogin',
};


export const userLogin = async (data, params = {}) => 
  request(`${UserEndPoint.USER_LOGIN}`, Method.POST, data, params);