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
  const cookies = document.cookie.split("; ");
  const cookie = cookies.find((c) => c.startsWith(`${cookieName}=`));
  return cookie ? cookie.split("=")[1] : null;
};

/**
 * Sends a request using fetch to the endpoint specified in the .env file.
 *
 * @param {string} path - The URL of the wanted resource.
 * @param {string} method - The HTTP method.
 * @param {Object} body - The request body.
 * @param {Object} params - The query parameters.
 * @param {boolean} includeAuth - Whether to include the Authorization header.
 * @returns {Promise<Response>} - A promise with the response.
 */
export async function request(path, method, body, params = {}, includeAuth = false) {
  // Get the access token from localStorage
  const accessToken = localStorage.getItem("access_token");

  // Get the CSRF token from cookies
  const csrfToken = getCookie("csrf_access_token");

  // Prepare headers
  const headers = {
    "Content-Type": "application/json",
    ...(includeAuth && accessToken ? { Authorization: `Bearer ${accessToken}` } : {}), // Add Authorization header if required
    ...(csrfToken ? { "X-CSRF-TOKEN": csrfToken } : {}), // Add CSRF token header if it exists
  };

  return window.fetch(buildURL(endpoint, path, params), {
    method: method,
    headers: headers,
    credentials: "include", // Include cookies
    body: body ? JSON.stringify(body) : null,
  });
}
