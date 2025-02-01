import React, { useContext, useEffect } from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { UserContext } from '../../../context/UserContext';
import StudentApplication from './StudentApplication';
import { useNavigate } from 'react-router-dom';

const StudentApplicationView = () => {
    const { user, userLogout } = useContext(UserContext);
    const navigate = useNavigate();
    useEffect(() => {
        if(user.type !== 'student') {
            navigate('/login');
        }
    }, [user]);
    return (
        <div>
            <Navbar user={user} onLogout={userLogout} />
            <StudentApplication />
            <Footer />
        </div>
    );
};

export default StudentApplicationView;