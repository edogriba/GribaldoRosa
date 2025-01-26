import { Method } from './api';
import { request, requestAuth } from './request';

const UserEndPoint = {
  USER_LOGIN: '/api/userlogin',
  USER_LOGOUT: '/api/userlogout',
  USER_AUTHENTICATED: '/api/protected',
};

export const userLogin = async (data) => 
    request(`${UserEndPoint.USER_LOGIN}`, Method.POST, data);

export const userLogout = async () => 
  requestAuth(`${UserEndPoint.USER_LOGOUT}`, Method.POST);

export const userAuthenticated = async () => 
  requestAuth(`${UserEndPoint.USER_AUTHENTICATED}`, Method.GET);