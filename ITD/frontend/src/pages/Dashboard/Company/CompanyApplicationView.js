import React, { useContext, useEffect } from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { UserContext } from '../../../context/UserContext';
import CompanyApplication from './CompanyApplication';
import { useNavigate } from 'react-router-dom';

const CompanyApplicationView = () => {
    const { user, userLogout } = useContext(UserContext);
    const {navigate} = useNavigate();
    useEffect(() => {
        if(user.type !== 'company') {
            navigate('/login');
        }
    }, [user]);
    return (
        <div>
            <Navbar user={user} onLogout={userLogout} />
            <CompanyApplication />
            <Footer />
        </div>
    );
};

export default CompanyApplicationView;