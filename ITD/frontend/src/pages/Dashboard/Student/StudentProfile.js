import React from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { StudentTab } from './StudentTab';

const StudentProfile = () => {
    return (
        <div>
            <Navbar/>
            <StudentTab activeTab='profile'/>
            
            <Footer />
        </div>
    );
};

export default StudentProfile;
