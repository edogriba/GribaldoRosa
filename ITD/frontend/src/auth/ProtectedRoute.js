import React, { useContext, useState, useEffect } from "react";
import { Navigate } from "react-router-dom";
import { UserContext } from "../context/UserContext";

const ProtectedRoute = ({ children }) => {
  const { user } = useContext(UserContext);

  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (user === null && localStorage.getItem("access_token") !== null) {
      setLoading(true);
    }
    else {
      setLoading(false)
    }
  }, [user]);
    //}, [user, localStorage.getItem("access_token")]);

  if (loading) {
    return (<div>Loading...</div>)
  }

  if (!user) {
    return <Navigate to="/login" />;
  }

  return children; // Render the protected content if authenticated
};

export default ProtectedRoute