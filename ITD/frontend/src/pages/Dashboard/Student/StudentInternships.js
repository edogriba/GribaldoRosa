import React from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { StudentTab } from './StudentTab';

const StudentInternships = () => {
    return (
        <div>
            <Navbar/>
            <StudentTab activeTab='internships'/>
            
            <Footer />
        </div>
    );
};

export default StudentInternships;