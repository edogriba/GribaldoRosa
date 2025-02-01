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
import CompanyPositions from './pages/Dashboard/Company/CompanyPositions';  
import StudentSearch from './pages/Search/Student/StudentSearch';
import CompanyCreatePositionView from './pages/Create/Company/CompanyCreatePositionView';
import StudentUpdate from './pages/Update/Student/StudentUpdate';
import CompanyUpdate from './pages/Update/Company/CompanyUpdate';
import UniversityUpdate from './pages/Update/University/UniversityUpdate';
import StudentInternships from './pages/Dashboard/Student/StudentInternships';
import About from './pages/About/About';
import NotFound from './pages/NotFound';
import './assets/index.css';
import CompanyInternships from './pages/Dashboard/Company/CompanyInternships';
import { Toaster } from 'react-hot-toast';
import UniversityInternships from './pages/Dashboard/University/UniversityInternships';
import CompanyPositionView from './pages/Dashboard/Company/CompanyPositionView';
import StudentApplicationView from './pages/Dashboard/Student/StudentApplicationView';
import CompanyApplicationView from './pages/Dashboard/Company/CompanyApplicationView';
import CompanyInternship from './pages/Dashboard/Company/CompanyInternship';
import StudentInternship from './pages/Dashboard/Student/StudentInternship';
import UniversityInternship from './pages/Dashboard/University/UniversityInternship';
import StudentPositionView from './pages/Search/Student/StudentPositionView';
function App() {
  return (
    <UserProvider> 
      <Toaster position="top-center" />
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
          <Route path="/companies/update" element={<ProtectedRoute><CompanyUpdate /></ProtectedRoute>} />
          <Route path="/universities/update" element={<ProtectedRoute><UniversityUpdate /></ProtectedRoute>} />
          <Route path="/students/search" element={<ProtectedRoute><StudentSearch /></ProtectedRoute>} />
          <Route path="/students/search/:positionId" element={<ProtectedRoute><StudentPositionView /></ProtectedRoute>} />
          <Route path="/companies/create-position" element={<ProtectedRoute><CompanyCreatePositionView /></ProtectedRoute>} />
          <Route path="/students/dashboard/applications" element={<ProtectedRoute><StudentApplications /></ProtectedRoute>} />
          <Route path="/students/dashboard/applications/:applicationId" element={<ProtectedRoute><StudentApplicationView /></ProtectedRoute>} />
          <Route path="/students/dashboard/internships" element={<ProtectedRoute><StudentInternships /></ProtectedRoute>} />
          <Route path="/students/dashboard/internships/:internshipId" element={<ProtectedRoute><StudentInternship /></ProtectedRoute>} />
          <Route path="/companies/dashboard/internships" element={<ProtectedRoute><CompanyInternships/></ProtectedRoute>} />
          <Route path="/companies/dashboard/internships/:internshipId" element={<ProtectedRoute><CompanyInternship /></ProtectedRoute>} />
          <Route path="/companies/dashboard/positions" element={<ProtectedRoute><CompanyPositions /></ProtectedRoute>} />
          <Route path="/universities/dashboard/internships" element={<ProtectedRoute><UniversityInternships /></ProtectedRoute>} />
          <Route path="/universities/dashboard/internships/:internshipId" element={<ProtectedRoute><UniversityInternship /></ProtectedRoute>} />
          <Route path="/companies/dashboard/positions/:positionId" element={<ProtectedRoute><CompanyPositionView /></ProtectedRoute>} />
          <Route path="/companies/dashboard/positions/:positionId/applications/:applicationId" element={<ProtectedRoute><CompanyApplicationView /></ProtectedRoute>} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </Router>
    </UserProvider>
  );
}

export default App;
