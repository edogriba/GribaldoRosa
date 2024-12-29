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
 * @returns {Promise<Response>} - A promise with the response.
 */
export async function request(path, method, body, params = {}) {
  return window.fetch(buildURL(endpoint, path, params), {
    method: method,
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body, (_, value) => value || undefined),
  });
}
