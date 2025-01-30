import React, { useContext } from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { UserContext } from '../../../context/UserContext';
import CompanyApplication from './CompanyApplication';

const CompanyApplicationView = () => {
    const { user, userLogout } = useContext(UserContext);
    return (
        <div>
            <Navbar user={user} onLogout={userLogout} />
            <CompanyApplication />
            <Footer />
        </div>
    );
};

export default CompanyApplicationView;