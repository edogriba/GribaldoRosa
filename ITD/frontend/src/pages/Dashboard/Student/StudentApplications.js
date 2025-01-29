import React, {useContext} from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import StudentTab from './StudentTab';
import StudentApplicationList from './StudentApplicationList';
import { UserContext } from '../../../context/UserContext';


const StudentApplications = () => {
    const { user, userLogout } = useContext(UserContext);
    return (
        <div className="flex flex-col justify-between min-h-screen">
            <div>
                <Navbar user={user} onLogout={userLogout}/>
                <StudentTab activeTab='applications'/>
                <StudentApplicationList />
            </div>
            <Footer />
        </div>
    );
};

export default StudentApplications;