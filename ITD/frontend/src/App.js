import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Register from './pages/Register/Register';
import RegisterStudent from './pages/Register/RegisterStudent/RegisterStudent';
import RegisterCompany from './pages/Register/RegisterCompany/RegisterCompany';
import RegisterUniversity from './pages/Register/RegisterUniversity/RegisterUniversity';
import Login from './pages/Login/Login'
import Welcome from './pages/Welcome/Welcome';

function App() {
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
