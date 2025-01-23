import { Method } from './api';
import { request } from './request';

const UserEndPoint = {
  USER_LOGIN: '/api/userlogin',
};


export const userLogin = async (data) => 
  request(`${UserEndPoint.USER_LOGIN}`, Method.POST, data);