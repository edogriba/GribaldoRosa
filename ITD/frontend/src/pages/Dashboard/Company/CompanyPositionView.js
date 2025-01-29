import React, {useContext} from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { UserContext } from '../../../context/UserContext';
import CompanyPosition from './CompanyPosition';


const CompanyPositionView = () => {
    const { user, userLogout } = useContext(UserContext);
    return (
        <div>
            <Navbar user={user} onLogout={userLogout}/>
            <CompanyPosition/>
            <Footer />
        </div>
    );
};

export default CompanyPositionView;