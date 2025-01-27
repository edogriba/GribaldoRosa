import React, {useContext} from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import {StudentTab} from './StudentTab';
import StudentInternshipList from './StudentInternshipList';
import { UserContext } from '../../../context/UserContext';


const StudentInternships = () => {
    const { user, userLogout } = useContext(UserContext);
    return (
        <div>
            <Navbar user={user} onLogout={userLogout}/>
            <StudentTab activeTab='internships'/>
            <StudentInternshipList />
            <Footer />
        </div>
    );
};

export default StudentInternships;