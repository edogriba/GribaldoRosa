import React, {useContext, useEffect} from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { UserContext } from '../../../context/UserContext';
import CompanyPosition from './CompanyPosition';
import { useNavigate } from 'react-router-dom';

const CompanyPositionView = () => {
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
            <CompanyPosition/>
            <Footer />
        </div>
    );
};

export default CompanyPositionView;