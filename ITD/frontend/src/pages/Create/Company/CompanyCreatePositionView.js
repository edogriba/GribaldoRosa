import React, {useContext} from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { UserContext } from '../../../context/UserContext';
import CompanyCreatePosition from './CompanyCreatePosition';

const CompanyCreatePositionView = () => {  
    const { user, userLogout } = useContext(UserContext);
    return (
        <div>
            <Navbar user={user} onLogout={userLogout}/>
            <CompanyCreatePosition />
            <Footer />
        </div>

    );
};

export default CompanyCreatePositionView;