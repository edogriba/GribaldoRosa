import React, {useContext} from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { UserContext } from '../../../context/UserContext';
import CompanyTab from './CompanyTab';
import CompanyInternshipList from './CompanyInternshipList';

const CompanyInternships = () => {
    const { user, userLogout } = useContext(UserContext);
    return (
        <div>
            <Navbar user={user} onLogout={userLogout}/>
            <CompanyTab activeTab='internships'/>
            <CompanyInternshipList/>
            <Footer />
        </div>
    );
};

export default CompanyInternships;
