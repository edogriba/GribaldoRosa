import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Register from './components/Register';
import RegisterStudent from './components/RegisterStudent';
import RegisterCompany from './components/RegisterCompany';
import RegisterUniversity from './components/RegisterUniversity';
import Login from './components/Login';
import Welcome from './components/Welcome';

function App() {
  const [students, setStudents] = useState([]); 

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/students')
      .then(response => {
        console.log('Backend response:', response.data); 
        setStudents(response.data);
      })
      .catch(error => console.error('Error:', error));
  }, []);

  return (
    <Router>
    <Routes>
      <Route path="/" element={<Welcome />}/>
      <Route path="/register" element={<Register />}/>
      <Route path="register/student" element={<RegisterStudent />}/>
      <Route path="register/company" element={<RegisterCompany />}/>
      <Route path="register/university" element={<RegisterUniversity />}/>
      <Route path="/login" element={<Login />} />
    </Routes>
  </Router>
  );
}

export default App;
