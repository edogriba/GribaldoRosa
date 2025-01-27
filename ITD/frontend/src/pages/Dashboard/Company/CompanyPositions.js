import React, {useContext} from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { UserContext } from '../../../context/UserContext';
import CompanyTab from './CompanyTab';
import CompanyPositionList from './CompanyPositionList';
import { api } from '../../../api/api';


const CompanyPositions = () => {
    const { user, userLogout } = useContext(UserContext);
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