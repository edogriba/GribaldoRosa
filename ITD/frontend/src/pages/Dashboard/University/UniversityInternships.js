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
        <div>
            <Navbar user={user} onLogout={userLogout}/>
            <UniversityTab activeTab='internships'/>
            <UniversityInternshipList />
            <Footer />
        </div>
    );
};

export default UniversityInternships;