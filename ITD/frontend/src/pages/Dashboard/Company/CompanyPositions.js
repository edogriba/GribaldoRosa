import React, {useContext, useEffect} from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { UserContext } from '../../../context/UserContext';
import CompanyTab from './CompanyTab';
import CompanyPositionList from './CompanyPositionList';
import { useNavigate } from 'react-router-dom';

const CompanyPositions = () => {
    const { user, userLogout } = useContext(UserContext);
    const navigate = useNavigate();
    useEffect(() => {
        if(user.type !== 'company') {
            navigate('/login');
        }
    }, [user]);
    return (
        <div>
            <Navbar user={user} onLogout={userLogout}/>
            <CompanyTab activeTab='positions'/>
            <CompanyPositionList/>
            <Footer />
        </div>
    );
};

export default CompanyPositions;