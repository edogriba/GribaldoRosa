import React, {useContext, useEffect} from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import {StudentTab} from './StudentTab';
import StudentInternshipList from './StudentInternshipList';
import { UserContext } from '../../../context/UserContext';
import { useNavigate } from 'react-router-dom';


const StudentInternships = () => {
    const { user, userLogout } = useContext(UserContext);
    const {navigate} = useNavigate();
    useEffect(() => {
        if(user.type !== 'student') {
            navigate('/login');
        }
    }, [user]);
    return (
        <div className="flex flex-col justify-between min-h-screen">
            <div>
                <Navbar user={user} onLogout={userLogout}/>
                <StudentTab activeTab='internships'/>
                <StudentInternshipList />
            </div>
            <Footer />
        </div>
    );
};

export default StudentInternships;