import { Method } from './api';
import { request, requestAuth, requestWithErrorToast, requestAuthWithErrorToast } from './request';

const UserEndPoint = {
  USER_LOGIN: '/api/userlogin',
  USER_LOGOUT: '/api/userlogout',
  USER_AUTHENTICATED: '/api/protected',
};

export const userLogin = async (data) => 
    requestAuthWithErrorToast(`${UserEndPoint.USER_LOGIN}`, Method.POST, data, {}, 'Invalid email or password');

export const userLogout = async () => 
  requestAuthWithErrorToast(`${UserEndPoint.USER_LOGOUT}`, Method.POST, {}, {}, 'An error occurred while logging out'); 

export const userAuthenticated = async () => 
  requestAuth(`${UserEndPoint.USER_AUTHENTICATED}`, Method.GET);