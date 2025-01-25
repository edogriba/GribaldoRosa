import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import UserProvider from "./context/UserContext"; 
import ProtectedRoute from "./auth/ProtectedRoute"
import Register from './pages/Register/Register';
import RegisterStudent from './pages/Register/Student/RegisterStudent';
import RegisterCompany from './pages/Register/Company/RegisterCompany';
import RegisterUniversity from './pages/Register/University/RegisterUniversity';
import Login from './pages/Login/Login'
import Welcome from './pages/Welcome/Welcome';
import HomeStudent from './pages/Home/Student/HomeStudent';
import HomeCompany from './pages/Home/Company/HomeCompany';
import HomeUniversity from './pages/Home/University/HomeUniversity';
import StudentProfile from './pages/Dashboard/Student/StudentProfile';
import CompanyProfile from './pages/Dashboard/Company/CompanyProfile';
import UniversityProfile from './pages/Dashboard/University/UniversityProfile';
import StudentApplications from './pages/Dashboard/Student/StudentApplications';
import StudentSearch from './pages/Search/Student/StudentSearch';
import StudentUpdate from './pages/Update/Student/StudentUpdate';
import StudentInternships from './pages/Dashboard/Student/StudentInternships';
import About from './pages/About/About';
import NotFound from './pages/NotFound';
import './assets/index.css';

function App() {
  return (
    <UserProvider>
      <Router>
        <Routes>
          <Route path="/" element={<Welcome />}/>
          <Route path="/register" element={<Register />}/>
          <Route path="register/student" element={<RegisterStudent />}/>
          <Route path="register/company" element={<RegisterCompany />}/>
          <Route path="register/university" element={<RegisterUniversity />}/>
          <Route path='/about' element={<About />}/>
          <Route path="/login" element={<Login />} />
          <Route path="/students/home" element={<ProtectedRoute><HomeStudent /></ProtectedRoute>} />
          <Route path="/companies/home" element={<ProtectedRoute><HomeCompany /></ProtectedRoute>} />
          <Route path="/universities/home" element={<ProtectedRoute><HomeUniversity /></ProtectedRoute>} />
          <Route path="/students/dashboard/profile" element={<ProtectedRoute><StudentProfile /></ProtectedRoute>} />
          <Route path="/companies/dashboard/profile" element={<ProtectedRoute><CompanyProfile /></ProtectedRoute>} />
          <Route path="/universities/dashboard/profile" element={<ProtectedRoute><UniversityProfile /></ProtectedRoute>} />
          <Route path="/students/update" element={<ProtectedRoute><StudentUpdate /></ProtectedRoute>} />
          <Route path="/students/search" element={<ProtectedRoute><StudentSearch /></ProtectedRoute>} />
          <Route path="/students/dashboard/applications" element={<ProtectedRoute><StudentApplications /></ProtectedRoute>} />
          <Route path="/students/dashboard/internships" element={<ProtectedRoute><StudentInternships /></ProtectedRoute>} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </Router>
      </UserProvider>
  );
}

export default App;
