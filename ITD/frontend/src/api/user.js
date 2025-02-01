import { Method } from './api';
import { requestAuth, requestWithErrorToast, requestAuthWithErrorToast } from './request';

const UserEndPoint = {
  USER_LOGIN: '/api/userlogin',
  USER_LOGOUT: '/api/userlogout',
  USER_AUTHENTICATED: '/api/protected',
};

export const userLogin = async (data) => 
    requestWithErrorToast(`${UserEndPoint.USER_LOGIN}`, Method.POST, data, {}, false);

export const userLogout = async () => 
  requestAuthWithErrorToast(`${UserEndPoint.USER_LOGOUT}`, Method.POST, {}, {}, false); 

export const userAuthenticated = async () => 
  requestAuth(`${UserEndPoint.USER_AUTHENTICATED}`, Method.GET);