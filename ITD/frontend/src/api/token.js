import { Method } from './api';
import { request } from './request';

const TokenEndPoint = {
  REFRESH_TOKEN: '/api/token/refresh',
};



// Function to refresh the authentication token
// Usage: Call this function to get a new authentication token
export const refreshToken = async () =>
  request(`${TokenEndPoint.REFRESH_TOKEN}`, Method.POST, {});