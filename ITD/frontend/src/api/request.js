import { toast } from 'react-hot-toast';
const buildURL = (baseURL, path, params) => {
  const url = new URL(path, baseURL);

  // Add query parameters if any are provided
  Object.keys(params).forEach((key) =>
    url.searchParams.append(key, params[key])
  );

  return url.toString();
};

const endpoint = process.env.REACT_APP_BACKEND_URL;

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
export async function request(path, method, body, params = {}) {
 
  const headers = {
    "Content-Type": "application/json",
  };

  return window.fetch(buildURL(endpoint, path, params), {
    method: method,
    headers: headers,
    body: body ? JSON.stringify(body) : null,
  });
}

export async function requestAuth(path, method, body, params = {}) {

  const accessToken = localStorage.getItem("access_token");

  const headers = {
    "Content-Type": "application/json",
    "Authorization": `Bearer ${accessToken}` // Attach the access token
  };

  return window.fetch(buildURL(endpoint, path, params), {
    method: method,
    headers: headers,
    body: body ? JSON.stringify(body) : null,
  });
}

export async function requestAuthWithErrorToast(path, method, body, params = {}, customErrorMessage={}) {
  try {
    const response = await requestAuth(path, method, body, params);
    console.log(response);

    /*if (!response.ok ) {
      const message = customErrorMessage || 'An error occurred while processing your request.';
      toast.error(message);
    }*/


    return response;
  } catch (error) {
    // Display a generic error message if the request fails,
    // e.g., due to a network issue or a server error (most likely
    // due to the server being down).
    const message =
      'An error occurred while processing your request. The server might be down or there could be a network issue.';
    //toast.error(message);

    throw error;
  }
}

export async function requestWithErrorToast(path, method, body, params = {}, customErrorMessage) {
  try {
    const response = await request(path, method, body, params);
    console.log(response);

    if (!response.ok) {
      const message = customErrorMessage || 'An error occurred while processing your request.';
      //toast.error(message);
    }

    return response;
  } catch (error) {
    // Display a generic error message if the request fails,
    // e.g., due to a network issue or a server error (most likely
    // due to the server being down).
    const message =
      'An error occurred while processing your request. The server might be down or there could be a network issue.';
    toast.error(message);

    throw error;
  }
}
