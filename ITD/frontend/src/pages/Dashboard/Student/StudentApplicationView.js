import React, { useContext } from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { UserContext } from '../../../context/UserContext';
import StudentApplication from './StudentApplication';

const StudentApplicationView = () => {
    const { user, userLogout } = useContext(UserContext);
    return (
        <div>
            <Navbar user={user} onLogout={userLogout} />
            <StudentApplication />
            <Footer />
        </div>
    );
};

export default StudentApplicationView;