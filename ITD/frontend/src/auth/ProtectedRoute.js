import React, { useContext } from "react";
import { Navigate } from "react-router-dom";
import { UserContext } from "../context/UserContext";

const ProtectedRoute = ({ children }) => {
  const { user, loading } = useContext(UserContext); // Access `loading` from context

  // Show a loading spinner or message while the user state is being initialized
  if (loading) {
    return <div>Loading...</div>;
  }
  
  // Redirect to login if no user is authenticated
  if (!user) {
    return <Navigate to="/login" />;
  }

  // Render the protected content if authenticated
  return children;
};

export default ProtectedRoute;
