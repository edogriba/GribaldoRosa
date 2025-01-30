import React from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { UniversityTab } from './UniversityTab';
import UniversityProfileCard from './UniversityProfileCard';
import UniversityProfileTable from './UniversityProfileTable';
import { useContext } from 'react';
import { UserContext } from '../../../context/UserContext'; 

const UniversityProfile = () => {
    const { user, userLogout } = useContext(UserContext);
    return (
        <div className="flex flex-col justify-between min-h-screen dark:bg-gray-900">
            <div>
                <Navbar user={user} onLogout={userLogout}/>
                <UniversityTab activeTab='profile'/>
            </div>
                <div className='flex justify-evenly'>
                    <UniversityProfileCard />
                    <UniversityProfileTable />
                </div>
            <Footer />
        </div>
    );
};

export default UniversityProfile;
