import React, {useContext, useEffect} from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import {UniversityTab} from './UniversityTab';
import UniversityInternshipList from './UniversityInternshipList';
import { UserContext } from '../../../context/UserContext';
import { useNavigate } from 'react-router-dom';


const UniversityInternships = () => {
    const { user, userLogout } = useContext(UserContext);
    const navigate = useNavigate();
    useEffect(() => {
        if(user.type !== 'university') {
            navigate('/login');
        }
    }, [user]);
    return (
        <div className='flex flex-col justify-between min-h-screen dark:bg-gray-900'>
            <div>
            <Navbar user={user} onLogout={userLogout}/>
            <UniversityTab activeTab='internships'/>
            <UniversityInternshipList />
            </div>
            <Footer />
        </div>
    );
};

export default UniversityInternships;