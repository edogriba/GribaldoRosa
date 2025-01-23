import React from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { StudentTab } from './StudentTab';
import StudentProfileCard from './StudentProfileCard';

const StudentProfile = () => {
    return (
        <div>
            <Navbar />
            <StudentTab activeTab='profile'/>
            <StudentProfileCard />
            <Footer />
        </div>
    );
};

export default StudentProfile;
