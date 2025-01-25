const buildURL = (baseURL, path, params) => {
  const url = new URL(path, baseURL);

  // Add query parameters if any are provided
  Object.keys(params).forEach((key) =>
    url.searchParams.append(key, params[key])
  );

  return url.toString();
};

const endpoint = process.env.REACT_APP_BACKEND_URL;

// Helper function to extract a specific cookie
const getCookie = (cookieName) => {
  const cookies = document.cookie.split('; ');
  const cookie = cookies.find((c) => c.startsWith(`${cookieName}=`));
  return cookie ? cookie.split('=')[1] : null;
};

/**
 * Sends a request using fetch to the endpoint specified in the .env file.
 *
 * @param {string} path - The URL of the wanted resource.
 * @param {string} method - The HTTP method.
 * @param {Object} body - The request body.
 * @param {Object} params - The query parameters.
 * @returns {Promise<Response>} - A promise with the response.
 */
export async function request(path, method, body = null, params = {}) {
  // Get the CSRF token from cookies
  const csrfToken = getCookie('csrf_access_token');
  console.log(buildURL(endpoint, path, params), {
    method: method,
    headers: {
      'Content-Type': 'application/json',
      ...(csrfToken && { 'X-CSRF-TOKEN': csrfToken }), // Include CSRF token if available
    },
    credentials: 'include',
    body: body ? JSON.stringify(body) : null,
  })
  console.log("CSRF Token:", csrfToken); 
  return window.fetch(buildURL(endpoint, path, params), {
    method: method,
    headers: {
      'Content-Type': 'application/json',
      ...(csrfToken && { 'X-CSRF-TOKEN': csrfToken }), // Include CSRF token if available
    },
    credentials: 'include',
    body: body ? JSON.stringify(body) : null,
  });
}
