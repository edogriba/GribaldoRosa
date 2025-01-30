import React, {useContext} from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import {UniversityTab} from './UniversityTab';
import UniversityInternshipList from './UniversityInternshipList';
import { UserContext } from '../../../context/UserContext';


const UniversityInternships = () => {
    const { user, userLogout } = useContext(UserContext);
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