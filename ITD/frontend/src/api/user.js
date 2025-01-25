import { Method } from './api';
import { request } from './request';

const UserEndPoint = {
  USER_LOGIN: '/api/userlogin',
  USER_LOGOUT: '/api/userlogout',
  USER_AUTHENTICATED: '/api/protected',
};

export const userLogin = async (data) => 
  request(`${UserEndPoint.USER_LOGIN}`, Method.POST, data);

export const userLogout = async () => 
  request(`${UserEndPoint.USER_LOGOUT}`, Method.POST);

export const userAuthenticated = async () => 
  request(`${UserEndPoint.USER_AUTHENTICATED}`, Method.GET);