import React, {useContext} from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import {StudentTab} from './StudentTab';
import StudentList from './StudentList';
import { UserContext } from '../../../context/UserContext';


const StudentInternships = () => {
    const { user, userLogout } = useContext(UserContext);
    return (
        <div>
            <Navbar isLoggedIn={!!user} onLogout={userLogout}/>
            <StudentTab activeTab='internships'/>
            <StudentList />
            <Footer />
        </div>
    );
};

export default StudentInternships;