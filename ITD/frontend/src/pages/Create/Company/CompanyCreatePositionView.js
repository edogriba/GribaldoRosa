import React, {useContext, useEffect} from 'react';
import Navbar from '../../../components/Navbar';
import { useNavigate } from 'react-router-dom';
import Footer from '../../../components/Footer';
import { UserContext } from '../../../context/UserContext';
import CompanyCreatePosition from './CompanyCreatePosition';

const CompanyCreatePositionView = () => {  
    const { user, userLogout } = useContext(UserContext);
    const { navigate } = useNavigate();
    useEffect(() => {
        if(user.type !== 'company') {
            navigate('/login');
        }
    }, [user]);
    return (
        <div>
            <Navbar user={user} onLogout={userLogout}/>
            <CompanyCreatePosition />
            <Footer />
        </div>

    );
};

export default CompanyCreatePositionView;