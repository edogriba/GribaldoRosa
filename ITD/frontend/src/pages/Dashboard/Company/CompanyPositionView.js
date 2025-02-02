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
        <div className="flex flex-col justify-between min-h-screen">
            <div>
            <Navbar user={user} onLogout={userLogout}/>
            <CompanyPosition/>
            </div>
            <Footer />
        </div>
    );
};

export default CompanyPositionView;