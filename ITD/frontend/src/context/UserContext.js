import React, { createContext, useState, useEffect } from "react";
import { api } from "../api/api"; // Replace with your actual API utilities
import { userAuthenticated } from "../api/user";

export const UserContext = createContext();

const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null); // Stores the authenticated user's data
  const [loading, setLoading] = useState(true); // Tracks whether the app is still loading user info

  // Function to log in the user
  const userLogin = async (dataUser) => {
    try {
      const response = await api.userLogin(dataUser); // Call backend
      // Debug response
      if (response.status === 200) {
        const userData = await response.json();
        console.log(userData)
        const accessToken = userData.access_token; // Ensure your backend returns this
        const refreshToken = userData.refresh_token; // Assuming the backend returns a refresh token

      // Securely store the refresh token (e.g., HttpOnly cookie)
        localStorage.setItem('refresh_token', refreshToken);
        const tokenPayload = JSON.parse(atob(accessToken.split(".")[1])); // Decode JWT payload
        console.log("Token Payload:", tokenPayload);
        if (tokenPayload.exp * 1000 < Date.now()) {
            console.error("Token is expired!");
        }
        if (accessToken) {
          localStorage.setItem("access_token", accessToken);
          setUser(userData.user); // Set user context
        }
        else {
          throw new Error("No access token received " + response.status); // Handle errors
        }
      }
      else {
        throw new Error("Login failed with status " + response.status); // Handle errors
      }
    } catch (error) {
      console.error("Login failed:", error.message);
      throw new Error("Login failed");
    }
  };

  // Function to log out the user
  const userLogout = async () => {
    try {
      await api.userLogout(); // Call logout endpoint to clear cookies on the server
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      setUser(null);
      //fetchUser(); // Fetch the user to update the context
      console.log("Logout successful");
    } catch (error) {
      console.error("Logout failed:", error.message);
    }
  };
  const initializeUser = async () => {
    const accessToken = localStorage.getItem("access_token");

    if (!accessToken) {
      console.log("No access token found. User is not logged in.");
      return;
    }

    try {
      // Validate the access token by calling a protected route
      const response = await api.userAuthenticated()

      if (response.status === 200) {
        const data = await response.json();
        setUser(data.user); // Set user context or state
        console.log("User initialized:", data.user);
      } else if (response.status === 401) {
        console.log("Access token expired. Attempting to refresh...");
        await refreshToken(); // Refresh token and try again
      } else {
        console.error("Failed to validate access token:", response.status);
      }
    } catch (error) {
      console.error("Error initializing user:", error.message);
    }
  };

  const refreshToken = async () => {
    try {
      const refreshToken = localStorage.getItem('refresh_token');
      if (!refreshToken) {
        console.error('Refresh token not found. Logging out...');
        setUser(null);
        localStorage.removeItem('access_token');
        return;
      }
  
      const response = await api.refreshToken({ refreshToken }); // Send refresh token to backend
      if (response.status === 200) {
        const data = await response.json();
        const newAccessToken = data.access_token;
  
        if (newAccessToken) {
          localStorage.setItem('access_token', newAccessToken);
          console.log('Access token refreshed.');
          // Optionally, retry the original request with the new access token
        }
      } else {
        console.error('Failed to refresh token. Logging out...');
        localStorage.removeItem('access_token');
        setUser(null);
      }
    } catch (error) {
      console.error('Error refreshing token:', error.message);
    }
  };

  // Automatically load the user on app initialization
  useEffect(() => {
    const initializeUserAndRefreshToken = async () => {
      try {
        const accessToken = localStorage.getItem('access_token');
        if (accessToken) {
          // Try to initialize the user
          await initializeUser(); 
        }
        setLoading(false);
      } catch (error) {
        console.error('Error initializing user:', error.message);
        setLoading(false); 
      }
    };

    initializeUserAndRefreshToken();
  }, []);

  return (
    <UserContext.Provider value={{ user, userLogin, userLogout, loading }}>
      {children}
    </UserContext.Provider>
  );
};

export default UserProvider;
