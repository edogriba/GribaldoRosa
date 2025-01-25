import React, { createContext, useState, useEffect } from "react";
import { api } from "../api/api"; // Replace with your actual API utilities

export const UserContext = createContext();

const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null); // Stores the authenticated user's data
  const [loading, setLoading] = useState(true); // Indicates if the app is loading
  // Function to log in the user
  const userLogin = async (dataUser) => {
    try {
      const response = await api.userLogin(dataUser); // Call backend
      // Debug response
      if (response.status === 200) {
        const userData = await response.json();
        console.log(userData)

        const accessToken = userData.access_token; // Ensure your backend returns this

        if (accessToken) {
          localStorage.setItem("access_token", accessToken);
          setUser(userData.user); // Set user context
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
      setUser(null);

      console.log("Logout successful");
    } catch (error) {
      console.error("Logout failed:", error.message);
    }
  };


  // Automatically load the user on app initialization
  useEffect(() => {
    const initializeUser = async () => {
      try {
        const accessToken = localStorage.getItem("access_token");

        if (!accessToken) {
          console.log("No access token found. User is not logged in.");
          setLoading(false);
          return;
        }

        // Validate the access token by calling a protected route
        const response = await api.userAuthenticated()

        if (response.status === 200) {
          const data = await response.json();
          setUser(data.user); // Set user context or state
        } 
        else if (response.status === 401) {
          localStorage.removeItem("access_token");
          console.log("Token has expired")
        }
        else {
          console.error("Failed to validate access token:", response.status);
        }

      } catch (error) {
        console.error('Error initializing user:', error.message);
      }
      setLoading(false);
    };

    initializeUser();
  }, []);

  
  return (
    <UserContext.Provider value={{ user, userLogin, userLogout, loading }}>
      {children}
    </UserContext.Provider>
  );
};

export default UserProvider;
