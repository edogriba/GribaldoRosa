import React from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import StudentTab from './StudentTab';
import StudentList from './StudentList';

const StudentApplications = () => {

    return (
        <div>
            <Navbar/>
            <StudentTab activeTab='applications'/>
            <StudentList />
            <Footer />
        </div>
    );
};

export default StudentApplications;