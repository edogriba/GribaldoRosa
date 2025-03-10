import React, {useContext, useEffect} from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { UserContext } from '../../../context/UserContext';
import CompanyTab from './CompanyTab';
import CompanyInternshipList from './CompanyInternshipList';
import { useNavigate } from 'react-router-dom';

const CompanyInternships = () => {
    const { user, userLogout } = useContext(UserContext);
    const {navigate} = useNavigate();
    useEffect(() => {
        if(user.type !== 'company') {
            navigate('/login');
        }
    }, [user]);
    return (
        <div className="flex flex-col justify-between min-h-screen dark:bg-gray-900">
            <div>
            <Navbar user={user} onLogout={userLogout}/>
            <CompanyTab activeTab='internships'/>
            <CompanyInternshipList/>
            </div>
            <Footer />
        </div>
    );
};

export default CompanyInternships;
