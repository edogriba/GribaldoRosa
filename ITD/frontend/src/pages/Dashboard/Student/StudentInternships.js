import React from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import StudentTab from './StudentTab';
import StudentList from './StudentList';
const StudentInternships = () => {
    return (
        <div>
            <Navbar/>
            <StudentTab activeTab='internships'/>
            <StudentList />
            <Footer />
        </div>
    );
};

export default StudentInternships;