import React from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { CompanyTab } from './CompanyTab';
import CompanyProfileCard from './CompanyProfileCard';
import CompanyProfileTable from './CompanyProfileTable';
import { useContext } from 'react';
import { UserContext } from '../../../context/UserContext'; 

const CompanyProfile = () => {
    const { user, userLogout } = useContext(UserContext);
    return (
        <div className="flex flex-col justify-between min-h-screen dark:bg-gray-900">
            <div>
                <Navbar user={user} onLogout={userLogout}/>
                <CompanyTab activeTab='profile'/>
            </div>
                <div className='flex bg-gray-50'>
                    <CompanyProfileCard />
                    <CompanyProfileTable />
                </div>
            <Footer />
        </div>
    );
};

export default CompanyProfile;
