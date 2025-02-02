import React, { createContext, useState, useEffect } from "react";
import { api } from "../api/api"; 
import toast from "react-hot-toast";

export const UserContext = createContext();

const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null); 
  const [loading, setLoading] = useState(true); 

  const userLogin = async (response) => {
    try {
      if (response.status === 200) {
        const userData = await response.json();
        const accessToken = userData.access_token;

        if (accessToken) {
          localStorage.setItem("access_token", accessToken);
          setUser(userData.user); 
        } 
      }
      else {
        throw new Error("Login failed with status " + response.status); 
      }
    } catch (error) {
      throw new Error("Login failed");
    }
  };

  const userRegistration = async (response) => {
    try {
      
      if (response.status === 201) {
        const userData = await response.json();
        const accessToken = userData.access_token; 

        if (accessToken) {
          localStorage.setItem("access_token", accessToken);
          setUser(userData.user); 
          toast.success("Registration successful");
        } 
      } 
      else {
        throw new Error("Registration failed with status " + response.status); 
      }
    } catch (error) {
      console.error("Registration failed:", error.message);
      throw new Error("Registration failed");
    }
  };

  const userLogout = async () => {
    try {
      await api.userLogout(); 
      localStorage.removeItem("access_token");
      setUser(null);
      toast.success("Logout successful");
    } catch (error) {
      console.error("Logout failed:", error.message);
      toast.error("Logout failed");
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

        const response = await api.userAuthenticated()

        if (response.status === 200) {
          const data = await response.json();
          setUser(data.user); 
        } 
        else if (response.status === 401) {
          localStorage.removeItem("access_token");
          console.log("Token has expired")
        }
        else {
          console.error("Failed to validate access token:", response.status);
        }
        setLoading(false);

      } catch (error) {
        console.error('Error initializing user:', error.message);
      }
      
    };

    initializeUser();
  }, []);

  
  return (
    <UserContext.Provider value={{ user, userLogin, userLogout, userRegistration, loading }}>
      {children}
    </UserContext.Provider>
  );
};

export default UserProvider;
