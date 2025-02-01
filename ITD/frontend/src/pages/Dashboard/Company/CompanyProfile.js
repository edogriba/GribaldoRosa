import React, { useContext, useEffect} from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { CompanyTab } from './CompanyTab';
import CompanyProfileCard from './CompanyProfileCard';
import CompanyProfileTable from './CompanyProfileTable';
import { UserContext } from '../../../context/UserContext'; 
import { useNavigate } from 'react-router-dom';

const CompanyProfile = () => {
    const { user, userLogout } = useContext(UserContext);
    const navigate = useNavigate();
    useEffect(() => {   
        if(user.type !== 'company') {
            navigate('/login');
        }
    }, [user]);
    return (
        <div className="flex flex-col justify-between min-h-screen dark:bg-gray-900">
            <div>
                <Navbar user={user} onLogout={userLogout}/>
                <CompanyTab activeTab='profile'/>
            </div>
                <div className='flex p-5 justify-evenly'>
                    <CompanyProfileCard />
                    <CompanyProfileTable />
                </div>
            <Footer />
        </div>
    );
};

export default CompanyProfile;
