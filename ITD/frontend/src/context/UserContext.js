import React, { createContext, useState, useEffect } from "react";
import { api } from "../api/api"; // Replace with your actual API utilities

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
        console.log(userData.user)
        setUser(userData.user); // Set user context
        
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
      setUser(null);
      fetchUser(); // Fetch the user to update the context
      console.log("Logout successful");
    } catch (error) {
      console.error("Logout failed:", error.message);
    }
  };

  // Function to fetch the authenticated user on app load
  const fetchUser = async () => {
    try {
      const response = await api.userAuthenticated(); // Call /api/protected endpoint
      if (response.status === 200) {
        setUser(response.user); // Set user context
      } else {
        console.log("User not authenticated");
        setUser(null);
      }
    } catch (error) {
      console.error("Failed to fetch user session:", error.message);
      setUser(null);
    } finally {
      setLoading(false); // Stop the loading spinner
    }
  };

  // Automatically load the user on app initialization
  useEffect(() => {
    fetchUser();
  }, []);

  return (
    <UserContext.Provider value={{ user, userLogin, userLogout, loading }}>
      {children}
    </UserContext.Provider>
  );
};

export default UserProvider;
