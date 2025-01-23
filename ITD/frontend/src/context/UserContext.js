import React, { createContext, useState, useEffect } from "react";

export const UserContext = createContext();

const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  // Utility function to safely access localStorage
  const isLocalStorageAvailable = () => {
    try {
      const testKey = "__test__";
      localStorage.setItem(testKey, "test");
      localStorage.removeItem(testKey);
      return true;
    } catch (error) {
      console.warn("localStorage is not available:", error);
      return false;
    }
  };

  useEffect(() => {
    if (isLocalStorageAvailable()) {
      // Check localStorage for user data on initial load
      const savedUser = localStorage.getItem("user");
      if (savedUser) {
        try {
          setUser(JSON.parse(savedUser));
        } catch (error) {
          console.error("Failed to parse user from localStorage:", error);
          setUser(null); // Fallback to null if parsing fails
          localStorage.removeItem("user"); // Clear invalid data
        }
      }
    }
  }, []);

  const loginUser = (userData) => {
    setUser(userData);
    if (isLocalStorageAvailable()) {
      localStorage.setItem("user", JSON.stringify(userData));
    }
  };

  const logoutUser = () => {
    setUser(null);
    if (isLocalStorageAvailable()) {
      localStorage.removeItem("user");
      localStorage.removeItem("token");
    }
  };

  return (
    <UserContext.Provider value={{ user, loginUser, logoutUser }}>
      {children}
    </UserContext.Provider>
  );
};

export default UserProvider;
