import React, {useContext} from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import StudentTab from './StudentTab';
import StudentApplicationList from './StudentApplicationList';
import { UserContext } from '../../../context/UserContext';


const StudentApplications = () => {
    const { user, userLogout } = useContext(UserContext);
    return (
        <div>
            <Navbar user={user} onLogout={userLogout}/>
            <StudentTab activeTab='applications'/>
            <StudentApplicationList />
            <Footer />
        </div>
    );
};

export default StudentApplications;